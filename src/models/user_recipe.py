from init import db, ma
from marshmallow import fields
from datetime import datetime, timezone

class UserRecipe(db.Model):
    __tablename__ = "user_recipes"

    user_recipe_id = db.Column(db.Integer, primary_key=True)
    # Create Foreign Key that references 'users' table
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    # Create Foreign Key that references 'recipes' table
    recipe_id =db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)

    # relationships
    user = db.relationship("User", back_populates="user_recipes")
    recipe = db.relationship("Recipe", back_populates="user_recipes")

# Create schema for UserRecipe 
class UserRecipeSchema(ma.Schema):
    recipe = fields.Nested("RecipeSchema", only=["name", "description", "recipe_ingredients"])

    class Meta:
        fields = ("user_recipe_id", "recipe")

# To handle a single user_recipe object
user_recipe_schema = UserRecipeSchema()

# To handle a list of user_recipe objects
user_recipes_schema = UserRecipeSchema(many=True)