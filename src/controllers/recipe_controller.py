from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.recipe import Recipe, recipe_schema, recipes_schema
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient
from models.user import User
from utils import authorise_as_admin

recipe_bp = Blueprint("recipes", __name__, url_prefix="/recipes")

# /recipes - GET - Fetch all recipes and their ingredients
@recipe_bp.route("/", methods=["GET"])
def get_all_recipes():
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt)
    return recipes_schema.dump(recipes)
    
# /recipes - GET - Fetch all recipes containing 'Vegan' in their description
@recipe_bp.route("/vegan", methods=["GET"])
def get_vegan_recipes():
    # Use ilike for a case-insensitive search of 'Vegan' in the recipe description
    stmt = db.select(Recipe).filter(Recipe.description.ilike("%Vegan%"))
    vegan_recipes = db.session.scalars(stmt).all()
    if not vegan_recipes: 
        return {"message": "Currently, there are no Vegan recipes in the Meal Planner database"}
    # Return all Vegan recipes
    return recipes_schema.dump(vegan_recipes)

# /recipes - GET - Fetch all recipes containing 'Keto' in their description
@recipe_bp.route("/keto", methods=["GET"])
def get_keto_recipes():
    # Use ilike for a case-insensitive search of 'Keto' in the recipe description
    stmt = db.select(Recipe).filter(Recipe.description.ilike("%Keto%"))
    keto_recipes = db.session.scalars(stmt).all()
    if not keto_recipes:
        return {"message": "Currently, there are no Keto recipes in the Meal Planner database"}
    # Return all Keto recipes
    return recipes_schema.dump(keto_recipes)

# /recipes - GET - Fetch all recipes containing 'Gluten Free' in their description
@recipe_bp.route("/gluten-free", methods=["GET"])
def get_gluten_free_recipes():
    # Use ilike for a case-insensitive search of 'Gluten' in the recipe description
    stmt = db.select(Recipe).filter(Recipe.description.ilike("%Gluten%"))
    gluten_free_recipes = db.session.scalars(stmt).all()
    if not gluten_free_recipes:
        return {"message": "Currently, there are no Gluten Free recipes in the Meal Planner database"}
    # Return all Gluten Free recipes
    return recipes_schema.dump(gluten_free_recipes)


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
    # Get the data from the body of the request - note: wrapped request.get_json() in: recipe_schema.load() for validation.
    body_data = recipe_schema.load(request.get_json())

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
    recipe_ingredients = body_data.get("recipe_ingredients", [])
    for ingredient_data in recipe_ingredients:
        name = ingredient_data["ingredient"].get("name")
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
    # Get the current_user_id from the JWT token, to make sure they are authorised to delete recipe, eg they created it, and is NOT predefined.
    current_user_id = int(get_jwt_identity()) # Need to convert to int (as token is str)

    # Check if the user is admin
    is_admin = authorise_as_admin()

    # fetch recipe from database
    stmt = db.select(Recipe).filter_by(recipe_id=recipe_id)
    recipe = db.session.scalar(stmt)

    # Check if recipe exists
    if not recipe:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' was not found"}, 404
    
    # Check if the recipe is predefined, and the user is not an admin
    if recipe.is_predefined and not is_admin:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' is predefined; only admins can delete predefined recipes."}, 403
    
    
    # Check if the user is the creator of the recipe or is_admin
    if recipe.user_id != current_user_id and not is_admin:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' was not created by you; you can only delete recipes that you yourself have created."}, 403

    # Delete recipe
    db.session.delete(recipe)
    db.session.commit()
    return {"message": f"The recipe: {recipe.name} was successfully deleted."}, 200
   

# /recipes/<int:recipe_id> - PUT, PATCH - edit a recipe: if you would like to add or delete an ingredient, change an existing ingredients amount and/or unit, or change the recipe name or description.
@recipe_bp.route("/<int:recipe_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_recipe(recipe_id):
    # Get the information from the request - Need to accept partial inputs, as only editing parts of recipe.
    body_data = recipe_schema.load(request.get_json(), partial=True)

    # Fetch the recipe from the database
    stmt = db.select(Recipe).filter_by(recipe_id=recipe_id)
    recipe = db.session.scalar(stmt)

    if not recipe:
        return {"error": f"Recipe with the recipe_id of '{recipe_id}' was not found"}, 404

    # Now get the user_id from the JWT token, to make sure they are authorised to update the recipe, eg they created it, and is NOT predefined.
    user_id = int(get_jwt_identity()) # Token is string, needs to be converted to int
    
    # Check if the user is admin
    is_admin = authorise_as_admin()

    # Check if the recipe is predefined, and the user is not admin
    if recipe.is_predefined and not is_admin:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' is predefined; only admins can update predefined recipes."}, 403

    # Check if the user is the creator of the recipe or is admin
    if recipe.user_id != user_id and not is_admin:
        return {"error": f"The Recipe with the recipe_id of '{recipe_id}' was not created by you; you can only update recipes that you yourself have created."}, 403

    # If the user would like to update the name or description of the recipe, either or both, or none.
    if "name" in body_data:
        recipe.name = body_data.get("name")
    if "description" in body_data:
        recipe.description = body_data.get("description")

    # If the user would like to add, update, or delete any ingredients, iterate through ingredient data (json request).
    recipe_ingredients = body_data.get("recipe_ingredients", [])
    for ingredient_data in recipe_ingredients:
        delete = ingredient_data.get("delete", False) # If delete is not provided in body_data, it defaults to False
        
        # If deleting an ingredient from a recipe, or updating a recipe's amount must make sure the user has included the ingredients name
        if delete:
            if "ingredient" not in ingredient_data or "name" not in ingredient_data["ingredient"]:
                return {"error": "The ingredients name must be provided, for the ingredient to be deleted."}, 400
            name = ingredient_data["ingredient"].get("name")
        # If not deleting an ingredient, just updating an ingredient:
        else:
            # Can not update an ingredient, if a name is not provided
            if "ingredient" not in ingredient_data or "name" not in ingredient_data["ingredient"]:
                return {"error": "The ingredients name must be provided, for the ingredient's amount or unit to be updated."}, 400
            name = ingredient_data["ingredient"].get("name")
            amount = ingredient_data.get("amount")
            unit = ingredient_data.get("unit")


        # Fetch the ingredient from the database, search by name
        stmt = db.select(Ingredient).filter_by(name=name)
        ingredient = db.session.scalar(stmt)
        
        # If the ingredient does not already exist in the database, create it, and add plus commit to get the ingredient_id
        if not ingredient:
            ingredient = Ingredient(name=name)
            db.session.add(ingredient)
            db.session.commit() 

        # Fetch the recipe-ingredient association from the database
        stmt = db.select(RecipeIngredient).filter_by(recipe_id=recipe.recipe_id, ingredient_id=ingredient.ingredient_id)
        recipe_ingredient = db.session.scalar(stmt)

        # If the user has delete set to true in request, and recipe-ingredient association exists, delete the ingredient (recipe_ingredient) from recipe.
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

