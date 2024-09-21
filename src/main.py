import os
from flask import Flask


# For flask app, need to import the previously initialised (in init.py) instances or objects of:
from init import db, ma, bcrypt, jwt

# For Blueprints, need to import db_commands
from controllers.cli_controllers import db_commands
from controllers.auth_controller import auth_bp
from controllers.recipe_controller import recipe_bp

# Create (define) a flask app inside a function (Application factories)
def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
    
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register Blueprints
    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(recipe_bp)

    return app
