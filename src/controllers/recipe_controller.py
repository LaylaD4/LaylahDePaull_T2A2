from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.recipe import Recipe, recipe_schema, recipes_schema
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient
from models.user import User

recipe_bp = Blueprint("recipes", __name__, url_prefix="/recipes")

# /recipes - GET - Fetch all recipes and their ingredients
@recipe_bp.route("/", methods=["GET"])
def get_all_recipes():
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt)
    return recipes_schema.dump(recipes)

# /recipes/<id> - GET - fetch a specific recipe
@recipe_bp.route("/<int:recipe_id>", methods=["GET"])
def get_a_recipe(recipe_id):
    stmt = db.select(Recipe).filter_by(recipe_id=recipe_id)
    # stmt = db.select(Recipe).where(Recipe.recipe_id==recipe_id) - Another way to write it.
    recipe = db.session.scalar(stmt)
    if recipe:
        return recipe_schema.dump(recipe)
    else:
        return {"error": f"The Recipe you have requested with the recipe id of '{recipe_id}' was not found."}, 404
    
# /recipes - POST - create a new recipe with a user that is logged in and authenticated (JWT)
@recipe_bp.route("/", methods=["POST"])
@jwt_required() 
def create_recipe():
    # Get the data from the body of the request
    body_data = request.get_json()

    # Create a new recipe with the user ID from JWT
    recipe = Recipe(
        name = body_data.get("name"),
        description = body_data.get("description"),
        user_id = get_jwt_identity()  
    )

    # Add the recipe to the session and commit to generate the necessary recipe_id value
    db.session.add(recipe)
    db.session.commit()

    # Now need to handle the ingredients that go into the recipe
    ingredients = body_data.get("ingredients", [])
    for ingredient_data in ingredients:
        name = ingredient_data.get("name")
        amount = ingredient_data.get("amount")
        unit = ingredient_data.get("unit")

        # Check if an ingredient by name already exists in the Ingredient table (database)
        ingredient = db.session.execute(db.select(Ingredient).filter_by(name=name)).scalar()

        if not ingredient:
            # Add new ingredient if it doesn't exist
            ingredient = Ingredient(name=name)
            db.session.add(ingredient)
            db.session.commit()  # Need to commit to get the ingredient_id

        # Create recipe-ingredient association for RecipeIngredient table
        recipe_ingredient = RecipeIngredient(
            recipe_id = recipe.recipe_id,
            ingredient_id = ingredient.ingredient_id,
            amount = amount,
            unit = unit
        )
        db.session.add(recipe_ingredient)

    # Commit all changes
    db.session.commit()

    # Return the created recipe as a response
    return recipe_schema.dump(recipe), 201