from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Create SQLAlchemy object to interact with the database
db = SQLAlchemy()
# Create Marshmallow object to define schemas
ma = Marshmallow()
# Create Bcrypt object to handle password hashing
bcrypt = Bcrypt()
# Create JWTManager object, to handle JSON Web Tokens (JWT) for authentication.
jwt = JWTManager()