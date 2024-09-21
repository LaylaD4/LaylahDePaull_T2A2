from flask import Blueprint, request
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

# /recipes - GET - Fetch all recipes containing 'Vegan' in their name
@recipe_bp.route("/vegan", methods=["GET"])
def get_vegan_recipes():
    # Use ilike for a case-insensitive search of 'Vegan' in the recipe name
    stmt = db.select(Recipe).filter(Recipe.name.ilike("%Vegan%"))
    vegan_recipes = db.session.scalars(stmt)
    return recipes_schema.dump(vegan_recipes)


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
    print(f"Recipe ID: {recipe.recipe_id}")

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


# /recipes/<int:recipe_id> - DELETE - delete a recipe
@recipe_bp.route("/<int:recipe_id>", methods=["DELETE"])
@jwt_required()
def delete_recipe(recipe_id):
    # First get the user_id from the JWT token, to make sure they are authorised to delete recipe, eg they created it, and is NOT predefined.
    user_id = get_jwt_identity()

    # Now fetch the user from the database
    stmt = db.Select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)

    # fetch recipe from database
    stmt = db.select(Recipe).filter_by(recipe_id=recipe_id)
    recipe = db.session.scalar(stmt)

    # Check if recipe exists
    if not recipe:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' was not found"}, 404
    
    # Check if the recipe is predefined, and the user is not an admin
    if recipe.is_predefined and not user.is_admin:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' is predefined; only admins can delete predefined recipes."}, 403
    
    
    # Check if the user is the creator of the recipe or is_admin
    if recipe.user_id != user.user_id and not user.is_admin:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' was not created by you; you can only delete recipes that you yourself have created."}, 403

    # Delete recipe
    db.session.delete(recipe)
    db.session.commit()
    return {"message": f"The recipe: {recipe.name} was successfully deleted."}, 200
   

# /recipes/<int:recipe_id> - PUT, PATCH - edit a recipe: if you would like to add or delete an ingredient, change an existing ingredients amount and/or unit, or change the recipe name or description.
@recipe_bp.route("/<int:recipe_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_recipe(recipe_id):
    # Get the information from the request
    body_data = request.get_json()

    # Fetch the recipe from the database
    stmt = db.select(Recipe).filter_by(recipe_id=recipe_id)
    recipe = db.session.scalar(stmt)

    if not recipe:
        return {"error": f"Recipe with the recip_id of '{recipe_id}' was not found"}, 404

    # Now get the user_id from the JWT token, to make sure they are authorised to update the recipe, eg they created it, and is NOT predefined.
    user_id = get_jwt_identity()
    
    # Now fetch the user from the database
    stmt = db.select(User).filter_by(user_id=user_id)
    user = db.session.scalar(stmt)

    # Check if the recipe is predifined, and the user is not admin
    if recipe.is_predefined and not user.is_admin:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' is predefined; only admins can update predefined recipes."}, 403

    # Check if the user is the creator of the recipe or is admin
    if recipe.user_id != user.user_id and not user.is_admin:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' was not created by you; you can only update recipes that you yourself have created."}, 403

    # If the user would like to update the name or description of the recipe, either or both, or none.
    if "name" in body_data:
        recipe.name = body_data.get("name")
    if "description" in body_data:
        recipe.description = body_data.get("description")

    # If the user would like to add, update, or delete any ingredients
    ingredients = body_data.get("ingredients", [])
    for ingredient_data in ingredients:
        name = ingredient_data.get("name")
        amount = ingredient_data.get("amount")
        unit = ingredient_data.get("unit")
        delete = ingredient_data.get("delete", False)

        # Fetch the ingredient from the database
        stmt = db.select(Ingredient).filter_by(name=name)
        ingredient = db.session.scalar(stmt)
        
        # If the ingredient does not already exist in the database, create it, and add plus commit to get ingredient_id
        if not ingredient:
            ingredient = Ingredient(name=name)
            db.session.add(ingredient)
            db.session.commit()  # Commit to get the new ingredient additions ingredient_id

        # Fetch the recipe-ingredient association from the database
        stmt = db.select(RecipeIngredient).filter_by(recipe_id=recipe.recipe_id, ingredient_id=ingredient.ingredient_id)
        recipe_ingredient = db.session.scalar(stmt)

        # If the user has delete set to true in request, delete the ingredient (recipe_ingredient) from recipe.
        if delete:
            if recipe_ingredient:
                db.session.delete(recipe_ingredient)
        else:
            # If the recipe-ingredient association already exists, update the existing recipe-ingredient association's amount and unit, if the user has provided it in request
            if recipe_ingredient:
                if amount is not None:
                    recipe_ingredient.amount = amount
                if unit is not None:
                    recipe_ingredient.unit = unit
            # Otherwise add the new recipe-ingredient association to database (recipe_ingredients table) if it doesn't already exist        
            else:
                new_recipe_ingredient = RecipeIngredient(
                    recipe_id=recipe.recipe_id,
                    ingredient_id=ingredient.ingredient_id,
                    amount=amount,
                    unit=unit
                )
                db.session.add(new_recipe_ingredient)

    # Commit all changes
    db.session.commit()  
    # Return the update recipe
    return recipe_schema.dump(recipe), 200


    


    

    
