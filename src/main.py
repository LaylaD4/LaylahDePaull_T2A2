import os
from flask import Flask


# For flask app, need to import the previously initialised (in init.py) instances or objects of:
from init import db, ma, bcrypt, jwt

# For Blueprints, need to import db_commands
from controllers.cli_controllers import db_commands

# Create (define) a flask app inside a function (Application factories)
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
    
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)

    return app
