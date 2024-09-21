from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient

db_commands = Blueprint("db", __name__)

# Command to create tables, eg; 'flask db create'.
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("seed")
def seed_tables():
    # Create and seed users
    users = [
        User(
            username="layla_admin",
            email="admin@mealplanner.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True
        ),
        User(
            username="elise04",
            email="elisebc04@email.com",
            password=bcrypt.generate_password_hash("qwerty12").decode("utf-8")
        )
    ]

    # Add and commit users
    db.session.add_all(users)
    db.session.commit()

    # Create and seed ingredients
    ingredients = [
        Ingredient(name="Almond Flour"),
        Ingredient(name="Butter"),
        Ingredient(name="Eggs"),
        Ingredient(name="Cream Cheese"),
        Ingredient(name="Blueberries"),
        Ingredient(name="Coconut Oil"),
        Ingredient(name="Baking Powder"),
        Ingredient(name="Cashew Yoghurt"),
        Ingredient(name="Maple Syrup")
    ]

    # Add and commit ingredients
    db.session.add_all(ingredients)
    db.session.commit()

    # Create and seed recipes
    recipes = [
        Recipe(
            name="Keto Pancakes",
            description="Breakfast, Keto, Gluten Free",
            is_predefined=True,
            # user_id=1  # Admin
            user = users[0] # Admin
        ),
        Recipe(
            name="Vegan Pancakes",
            description="Breakfast, Vegan, Gluten Free, Dairy Free",
            is_predefined=True,
            # user_id=1  # Admin
            user = users[0] # Admin
        )
    ]

    # Add and commit recipes
    db.session.add_all(recipes)
    db.session.commit()

    # Create and seed recipe-ingredient associations
    recipe_ingredients = [
        RecipeIngredient(
            recipe_id=1,  # Keto Pancakes
            ingredient_id=1,  # Almond Flour
            amount=200,
            unit="grams"
        ),
        RecipeIngredient(
            recipe_id=1,
            ingredient_id=2,  # Butter
            amount=25,
            unit="grams"
        ),
        RecipeIngredient(
            recipe_id=1,
            ingredient_id=3,  # Eggs
            amount=4,
            unit="large"
        ),
        RecipeIngredient(
            recipe_id=1,
            ingredient_id=4,  # Cream Cheese
            amount=150,
            unit="grams"
        ),
        RecipeIngredient(
            recipe_id=1,
            ingredient_id=5,  # Blueberries
            amount=50,
            unit="grams"
        ),
        RecipeIngredient(
            recipe_id=2,  # Vegan Pancakes
            ingredient_id=1,  # Almond Flour
            amount=300,
            unit="grams"
        ),
        RecipeIngredient(
            recipe_id=2,
            ingredient_id=6,  # Coconut Oil
            amount=50,
            unit="mls"
        ),
        RecipeIngredient(
            recipe_id=2,
            ingredient_id=7,  # Baking Powder
            amount=1,
            unit="tsp"
        ),
        RecipeIngredient(
            recipe_id=2,
            ingredient_id=8,  # Cashew Yoghurt
            amount=0.5,
            unit="cup"
        ),
        RecipeIngredient(
            recipe_id=2,
            ingredient_id=9,  # Maple Syrup
            amount=20,
            unit="mls"
        )
    ]

    # Add RecipeIngredient associations to the session
    db.session.add_all(recipe_ingredients)
    # Commit
    db.session.commit()

    print("Tables seeded")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")
