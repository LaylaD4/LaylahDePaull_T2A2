from flask_jwt_extended import get_jwt_identity

import functools

from init import db
from models.user import User

def authorise_as_admin():
    # Get the user_id from get_jwt_identity
    user_id = get_jwt_identity()
    # Fetch the user from the database
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)
    # Check whether the user is admin or not
    return user.is_admin

# Creating a decorator for authorise_as_admin
def auth_as_admin_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # Get the user_id from get_jwt_identity
        user_id = get_jwt_identity()
        # Fetch the user from the database
        stmt = db.select(User).filter_by(user_id=user_id)
        user = db.session.scalar(stmt)
        # If user is admin
        if user.is_admin:
            # Allow the decorator fn to execute
            return fn(*args, **kwargs)
        # Else
        else:
            # Return error
            return {"error": "You do not have permission to perform this action."}, 403
    return wrapper