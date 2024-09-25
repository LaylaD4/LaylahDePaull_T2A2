import os
from flask import Flask
from marshmallow.exceptions import ValidationError


# For flask app, need to import the previously initialised (in init.py) instances or objects of:
from init import db, ma, bcrypt, jwt

# For Blueprints, need to import db_commands
from controllers.cli_controllers import db_commands
from controllers.auth_controller import auth_bp
from controllers.recipe_controller import recipe_bp
from controllers.user_recipe_controller import user_recipe_bp

# Create (define) a flask app inside a function (Application factories)
def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    # Global error handler, whenever there is Marshmallow Validation errors when input data does not comply with defined schema.
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400
    
    # Global error handler, whenever there is a bad request - 400 error
    @app.errorhandler(400)
    def bad_request(err):
        return {"error": "This is a bad request. Please check the information you have entered in correct."}, 400

    # Global error handle, whenever there is an unauthorised request - 401 error
    @app.errorhandler(401)
    def unauthorised(err):
        return {"error": "You are not an authorised user."}, 401
    
    # Global error handler, whenever there is a user is forbidden access certain information - 403 error.
    @app.errorhandler(403)
    def forbidden(err):
        return {"error": "You do not have permission to access this information."}, 403
    
    # Global error handler, whenever there is information that is not found - 404 error.
    @app.errorhandler(404)
    def not_found(err):
        return {"error": "The requested information was not found."}, 404
    
    # Global error handler, whenever there is information given that can not be processed - 422 error.
    @app.errorhandler(422)
    def unprocessable_entity(err):
        return {"error": "There was an issue with your request. Please check the information you have submitted."}, 422
    
    # Global error handler, whenever there is an internal server issue (eg database connection error, contraint violations, timeouts) - 500 error.
    @app.errorhandler(500)
    def internal_server_error(err):
        return {"error": "An unexpected error occurred. Please try again later."}, 500
    
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register Blueprints
    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(recipe_bp)
    app.register_blueprint(user_recipe_bp)

    return app
