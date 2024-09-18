from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient
from models.shopping_list import ShoppingList
from models.shopping_list_item import ShoppingListItem
from datetime import datetime, timezone

db_commands = Blueprint("db", __name__)

# Command to create tables, eg; 'flask db create'.
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

# Command to seed tables, eg; 'flask db seed'.
@db_commands.cli.command("seed")
def seed_tables():
    # Create a list of User instances
    users = [
        User(
            username = "layla_admin",
            email = "admin@mealplanner.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin = True
        ), User(
            username = "elise04",
            email = "elisebc04@email.com",
            password = bcrypt.generate_password_hash("qwerty12").decode("utf-8")
        )
    ]

    # Add the users list
    db.session.add_all(users)

    # Create a list of Ingredient instances
    ingredients = [
        Ingredient(name="Almond Flour"),
        Ingredient(name="Butter"),
        Ingredient(name="Eggs"),
        Ingredient(name="Cream Cheese"),
        Ingredient(name="Blueberries"),
        Ingredient(name="Coconut Oil"),
        Ingredient(name="Baking Powder"),
        Ingredient(name="Cashew Yoghurt"),
        Ingredient(name="Maple Syrup"),
    ]
     # Add the ingredients list
    db.session.add_all(ingredients)

    # Create a list of Recipe instances
    recipes = [
        Recipe(
            name="Keto Pancakes",
            description="Breakfast, Keto, Gluten Free",
            is_predefined=True,
            created_at=datetime.now(timezone.utc).date(),
            user_id=1  # Recipe associated with admin user
        ),
        Recipe(
            name="Vegan Pancakes",
            description="Breakfast, Vegan, Gluten Free, Dairy Free",
            is_predefined=True,
            created_at=datetime.now(timezone.utc).date(),
            user_id=1 # Recipe associated with admin user
        )
    ]
    # Add recipes list
    db.session.add_all(recipes)

    # Commit the changes for users, ingredients, and recipes.
    db.session.commit()

    # Create ShoppingLists for each recipe
    shopping_lists = [
        ShoppingList(name="Keto Pancakes Ingredients", user_id=1),
        ShoppingList(name="Vegan Pancakes Ingredients", user_id=1)
    ]
    db.session.add_all(shopping_lists)

    # Commit to generate IDs for shopping lists
    db.session.commit()

    # Create RecipeIngredient associations
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
    
    # Commit changes to add RecipeIngredient associations
    db.session.commit()

    # Create ShoppingListItems for each ShoppingList
    shopping_list_items = [
        # Items for Keto Pancakes
        ShoppingListItem(
            amount=200,
            unit="grams",
            shopping_list_id=1,  # Keto Pancakes Ingredients
            ingredient_id=1      # Almond Flour
        ),
        ShoppingListItem(
            amount=25,
            unit="grams",
            shopping_list_id=1,  # Keto Pancakes Ingredients
            ingredient_id=2      # Butter
        ),
        ShoppingListItem(
            amount=4,
            unit="large",
            shopping_list_id=1,  # Keto Pancakes Ingredients
            ingredient_id=3      # Eggs
        ),
        ShoppingListItem(
            amount=150,
            unit="grams",
            shopping_list_id=1,  # Keto Pancakes Ingredients
            ingredient_id=4      # Cream Cheese
        ),
        ShoppingListItem(
            amount=50,
            unit="grams",
            shopping_list_id=1,  # Keto Pancakes Ingredients
            ingredient_id=5      # Blueberries
        ),
        # Items for Vegan Pancakes
        ShoppingListItem(
            amount=300,
            unit="grams",
            shopping_list_id=2,  # Vegan Pancakes Ingredients
            ingredient_id=1      # Almond Flour
        ),
        ShoppingListItem(
            amount=50,
            unit="mls",
            shopping_list_id=2,  # Vegan Pancakes Ingredients
            ingredient_id=6      # Coconut Oil
        ),
        ShoppingListItem(
            amount=1,
            unit="tsp",
            shopping_list_id=2,  # Vegan Pancakes Ingredients
            ingredient_id=7      # Baking Powder
        ),
        ShoppingListItem(
            amount=0.5,
            unit="cup",
            shopping_list_id=2,  # Vegan Pancakes Ingredients
            ingredient_id=8      # Cashew Yoghurt
        ),
        ShoppingListItem(
            amount=20,
            unit="mls",
            shopping_list_id=2,  # Vegan Pancakes Ingredients
            ingredient_id=9      # Maple Syrup
        )
    ]
    db.session.add_all(shopping_list_items)
    
    # Commit changes to add ShoppingListItems
    db.session.commit()

    # Send an acknowledgment message
    print("Tables seeded")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")