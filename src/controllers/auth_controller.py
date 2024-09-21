from flask import Blueprint, request
from models.user import User, user_schema, users_schema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# /auth/register - POST - Register a user account
@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # Get the data from the body of the request
        body_data = request.get_json()
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


# /auth - GET - Retrieve all users that currently have accounts, only admin is permitted to do this.
@auth_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_users():
    # Get the user_id from the current user
    user_id = get_jwt_identity()

    # Retrieve the current users details from the database, in particular need the is_admin attribute to make check
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)

    # Check if the current user is admin
    if not user.is_admin:
        return {"message": "You do not have permission to view all user's accounts."}, 403
    
    # Fetch all current users from the database
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return users_schema.dump(users)


# Delete User - Need to cascade, and delete all user recipes, when a user is deleted.
# /auth/<int:user_id> - DELETE - Register a user account
@auth_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    # First get the user_id from JWT token of the user making the request
    current_user_id = get_jwt_identity()

    # Need to fetch the current user from database, in particular the attribute is_admin to make that check below.
    stmt = db.select(User).filter_by(user_id=current_user_id)
    current_user = db.session.scalar(stmt)
    
    # Fetch the user from the database that is to be deleted
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)

    # Check first if the user exists
    if not user:
        return {"error": f"User with the user_id of '{user_id}' was not found."}, 404
    
    # Delete the user with 'user_id' only if current_user is the user, or is_admin
    if current_user.user_id == user.user_id or current_user.is_admin:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"The user with the user_id of '{user_id}' and name {user.username} has been successfully deleted."}, 200
    else:
        return {"message": f"You do not have permission to delete the user with the user_id of '{user_id}' and name {user.username}, you only have permission to delete your own account."}, 403
    

# Update User, eg; email, username, or password
# /auth/<int:user_id> - PUT, PATCH - Edit a user's account, eg; username, email, password.
@auth_bp.route("/<int:user_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_user(user_id):
    # First get the user_id from JWT token of the user making the request to update
    current_user_id = get_jwt_identity()

    # Need to fetch the current users details from the database, in particular the attribute is_admin to make a check below
    stmt = db.select(User).filter_by(user_id=current_user_id)
    current_user = db.session.scalar(stmt)

    # Need to fetch the user with user_id from the database that is to be updated
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)

    # Need to check first if the user even exists
    if not user:
        return {"error": f"User with the user_id of '{user_id}' was not found."}, 404
    
    # Update the details of the user with user_id only if the user owns the account, or is admin
    if current_user.user_id == user.user_id or current_user.is_admin:
        # Get the details from the body of the request
        body_data = request.get_json()

        # Update the username if requested
        if "username" in body_data:
            user.username = body_data.get("username")
        
        # Update the email if requested
        if "email" in body_data:
            user.email = body_data.get("email")

        # Update the password if requested
        if "password" in body_data:
            password = body_data.get("password")
            # Hash the password
            if password:
                user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Add and commit the changes
        db.session.add(user)
        db.session.commit()

        return {"message": f"You have successfully updated the user with user_id of '{user_id}'"}, 200
    else:
        return {"message": f"You do not have permission to update the user with the user_id of '{user_id}' and name {user.username}, you only have permission to update your own account details."}, 403
    




