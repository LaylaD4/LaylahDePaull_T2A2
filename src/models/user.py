from init import db, ma
from datetime import datetime, timezone
from marshmallow import fields, validate
from marshmallow.validate import Length, And, Regexp


# Create model for users table
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=lambda: datetime.now(timezone.utc).date())
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships
    recipes = db.relationship("Recipe", back_populates="user", cascade="all, delete") # If a user gets deleted, all recipes will be deleted.
    user_recipes = db.relationship("UserRecipe", back_populates="user", cascade="all, delete") # If a user gets deleted, all user_recipes will be deleted.

# Create schema for users table
class UserSchema(ma.Schema):
    username = fields.String(required=True, validate=validate.Length(min=4, error="Your username must be at least 4 characters long."))
    email = fields.String(required=True, validate=validate.Email(error="Your email address must be in a valid format, eg; name@example.com."))
    password = fields.String(
        required=True,
        validate=And(
            Length(min=6, error="Your password must be at least 6 characters long."),
            Regexp("^[A-Z].*$", error="Your password must start with an uppercase letter."),
            Regexp(".*\\d.*$", error="Your password must contain at least one number."),
            Regexp(".*[&*#@!$%^&*()_+={}\\[\\]:;\"'<>,.?/~`-].*$", error="Your password must contain at least one special character, eg; &, $, !.")
        )
    )

    class Meta:
        fields = ("user_id", "username", "email", "password", "created_at", "is_admin")
        ordered = True

# To handle a single user object
user_schema = UserSchema(exclude=["password"])

# To handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])

