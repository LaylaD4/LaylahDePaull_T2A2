from flask import Blueprint, request
from models.user import User, user_schema, users_schema, UserSchema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from utils import authorise_as_admin, auth_as_admin_decorator

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# /auth/register - POST - Register a new user account
@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # Get the data from the body of the request
        body_data = UserSchema().load(request.get_json()) # Need to validate, however need password too (excluded in user_schema)
        
        # Create a user instance from the User model
        user = User(
            username = body_data.get("username"),
            email = body_data.get("email")
        )
        # Hash the password
        password = body_data.get("password")
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        # Add and commit to the database
        db.session.add(user)
        db.session.commit()
        # Return acknowledgement (need user_schema, singular, as only registering one user at a time)
        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"More information is required, please enter your {err.orig.diag.column_name}"}, 400
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "The email address already exists. Please try again."}, 400

# /auth/login - POST - Login to a user account      
@auth_bp.route("/login", methods=["POST"])
def login_user():
    # Get the data from the body of the request
    body_data = request.get_json()
    # Find the user in the database with that email address
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    # If the user exists and check the password is correct, check database password (user.password) against request password body_data.get("password")
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # Create a JWT token
        token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
        # Respond back
        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    else:
        return {"error": "Invalid email or password was entered."}, 400


# /auth/users - GET - Retrieve all users that currently have accounts, only admin is permitted to do this; using @auth_as_admin_decorator to make check.
@auth_bp.route("/users", methods=["GET"])
@jwt_required()
@auth_as_admin_decorator
def get_all_users():
    # Fetch all current users from the database
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return users_schema.dump(users)


# DELETE User - Cascade delete all user recipes when a user is deleted.
# /auth/users/<int:user_id> - DELETE - Delete a user account
@auth_bp.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    # Get user id from JWT token trying to make deletion
    current_user_id = int(get_jwt_identity()) # need to convert to a int, as tokens stored as str

    # Check if the user is admin
    is_admin = authorise_as_admin()

    # Fetch the user from the database that is to be deleted (based on the user_id passed)
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)

    # If the user with user_id exists:
    if user:
        # Check if the user to be deleted is the current user or is_admin
        if user.user_id == current_user_id or is_admin:
            # Delete the user, cascading will delete related user recipes
            db.session.delete(user)
            db.session.commit()
            return {"message": f"The user '{user.username}' with user_id '{user_id}' has been successfully deleted."}, 200
        else:
            # Return an error if they don't have permission to delete
            return {"error": "You do not have permission to delete this user."}, 403
    else:
        # Return an error if the user with user_id does not exist
        return {"error": f"No user found with user_id '{user_id}'."}, 404
    

# /auth/users - PUT, PATCH - Edit a user's account, only; username, password.
@auth_bp.route("/users", methods=["PUT", "PATCH"])
@jwt_required()
def update_user():
    # Fetch the body of the request
    body_data = UserSchema().load(request.get_json(), partial=True) # We may not be updating all fields.

    # Check if the user is trying to change their email - Not 
    if "email" in body_data:
        return {"error": "Please contact us at: admin@mealplanner.com, if you would like to change your email address."}, 403
    
    if "is_admin" in body_data:
        return {"error": "You are not allowed to change your admin status."}, 403
    
    # Get password, if user is updating
    password = body_data.get("password")
    # Fetch the user from the database
    stmt = db.select(User).filter_by(user_id=get_jwt_identity())
    user = db.session.scalar(stmt)

    # Check if the user exists:
    if user:
        # If the user wants to update their username or not
        user.username = body_data.get("username") or user.username
        # If the user wants to update their password
        if password:
            # Hash the password
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        
        # Commit the changes
        db.session.commit()
        return user_schema.dump(user)
    else:
        # If the user doesn't exist:
        return {"error": "The user does not exist."}, 404

# /auth/users/<int:user_id> - PUT, PATCH - Admin only; to edit a user's account details, that is; username, email, and is_admin
@auth_bp.route("/users/<int:user_id>", methods=["PUT", "PATCH"])
@jwt_required()
@auth_as_admin_decorator
def admin_update_user(user_id):
    # Fetch the body of the request
    body_data = UserSchema().load(request.get_json(), partial=True) # We may not be updating all fields.

    if "password" in body_data:
        return {"error": "You are not allowed to change a users password."}, 403

    # Fetch the user from the database that is to be updated
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)

    # Check if the user exists:
    if user:
        # If updating user's username or not:
        user.username = body_data.get("username") or user.username
        # If udating user's email or not:
        user.email = body_data.get("email") or user.email
        # If updating user's is_admin status to true or false:
        if "is_admin" in body_data:
            user.is_admin = body_data["is_admin"]

        # Commit the changes
        db.session.commit()
        return user_schema.dump(user)
    else:
        # If the user doesn't exist:
        return {"error": f"The user with the user_id of '{user_id}' does not exist."}, 404




