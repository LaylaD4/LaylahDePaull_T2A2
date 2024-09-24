from flask_jwt_extended import get_jwt_identity

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