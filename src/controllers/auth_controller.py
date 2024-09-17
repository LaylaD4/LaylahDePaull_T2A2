from flask import Blueprint, request
from models.user import User, user_schema
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

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
        
    