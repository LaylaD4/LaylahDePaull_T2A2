from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.user_recipe import UserRecipe, UserRecipeSchema, user_recipes_schema
from models.recipe import Recipe

user_recipe_bp = Blueprint("user_recipes", __name__, url_prefix="/user-recipes")

# /user-recipes - POST - Add a recipe to user's list. (user_recipes)
@user_recipe_bp.route("/", methods=["POST"])
@jwt_required()
def add_user_recipe():
    # Get the user_id from the JWT token
    user_id = get_jwt_identity()
    # Fetch the data from the body of the request (eg; the recipe_id that is to be added the users recipes)
    body_data = request.get_json()
    # Get the recipe_id from the request
    recipe_id = body_data.get("recipe_id")

    # Check if the request has a recipe_id
    if not recipe_id:
        return {"error": "Please include a Recipe ID in your request."}, 400
    
    # Need to check if the recipe with that recipe_id exists in the database
    stmt = db.select(Recipe).filter_by(recipe_id=recipe_id)
    recipe = db.session.scalar(stmt)
    
    if not recipe:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' was not found"}, 404
    
    # Check if the recipe is already in the users recipe list, so no duplicates.
    stmt = db.select(UserRecipe).filter_by(user_id=user_id, recipe_id=recipe_id)
    existing_recipe = db.session.scalar(stmt)
    if existing_recipe:
        return {"message": f"You already have the recipe with recipe_id of '{recipe_id}' in your shopping list"}, 409


    # If the recipe exists, create a new UserRecipe instance
    user_recipe = UserRecipe(user_id=user_id, recipe_id=recipe_id)

    # Add and commit the user_recipe to the database
    db.session.add(user_recipe)
    db.session.commit()

    return {"message":f"The recipe with the recipe_id of '{recipe_id} was added to your recipe shopping list."}, 201


# /user-recipes - GET - Fetch all recipes (only by name) a user has in their recipe list (user_recipes).
@user_recipe_bp.route("/", methods=["GET"])
@jwt_required()
def get_user_recipes():
    user_id = get_jwt_identity()
    stmt = db.select(UserRecipe).filter_by(user_id=user_id)
    user_recipes = db.session.scalars(stmt).all() # Need to call .all() to convert result to a list.

    # Check if user has any recipes in their list
    if not user_recipes:
        return {"message": "You currently have no recipes stored in your shopping list."}, 200
    
    # Create a new schema instance to retreive or serialise only the recipe's name
    user_recipe_name_schema = UserRecipeSchema(only=["recipe.name"])
    return user_recipe_name_schema.dump(user_recipes, many=True), 200

# /user-recipes/shopping-list - GET - Create a shopping list, by fetching all the ingredients for the recipes a user has in their recipe list (user_recipes).
@user_recipe_bp.route("/shopping-list", methods=["GET"])
@jwt_required()
def get_shopping_list():
    # Get the user id from the JWT token
    user_id = get_jwt_identity()
    
    # Fetch all the users recipes using their the users user_id
    stmt = db.select(UserRecipe).filter_by(user_id=user_id)
    user_recipes = db.session.scalars(stmt).all() # Need to call .all() to convert result to a list.

    # Check if the user has any recipes in their list
    if not user_recipes:
        return {"message": "You currently have no recipes stored in your shopping list."}, 200

    # Create a list to store all shopping list ingredients
    ingredients_list = []

    # Use UserRecipeSchema to serialise user recipes and get ingredients
    user_recipe_data = user_recipes_schema.dump(user_recipes)
    
    # Loop through serialised user recipes to gather ingredients
    for user_recipe in user_recipe_data:
        recipe_ingredients = user_recipe['recipe'].get("recipe_ingredients", [])
        ingredients_list.append(recipe_ingredients)  # Add ingredients to the list

    return {"Shopping List Items": ingredients_list}, 200



# /user-recipes/<int:recipe_id> - DELETE - delete a recipe from a users recipe list.
@user_recipe_bp.route("/<int:recipe_id>", methods=["DELETE"])
@jwt_required()
def delete_user_recipes(recipe_id):
    # Fetch the user id in the JWT token
    user_id = get_jwt_identity()

    # Need to check if the recipe exists in the the users list first
    stmt = db.select(UserRecipe).filter_by(user_id=user_id, recipe_id=recipe_id)
    users_recipe = db.session.scalar(stmt)

    # If the recipe is not in the users list
    if not users_recipe:
        return {"error": f"The recipe with recipe_id of '{recipe_id}' was not found in your list"}, 404
    
    # Delete the recipe from the users list, and commit the changes
    db.session.delete(users_recipe)
    db.session.commit()

    return {"message": f"The recipe with the recipe_id of '{recipe_id}' was successfully deleted from your list."}, 200

