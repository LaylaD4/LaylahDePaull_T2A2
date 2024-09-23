from init import db, ma
from marshmallow import fields, validate
from datetime import datetime, timezone
from marshmallow.validate import Length, And, Regexp

class Recipe(db.Model):
    __tablename__ = "recipes"
    
    recipe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    is_predefined = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Date, default=lambda: datetime.now(timezone.utc).date())
    # Create Foreign Key that references 'users' table
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="recipes")
    ingredients = db.relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete") # Change to recipe_ingredients, makes relationship clearer.
    user_recipes = db.relationship("UserRecipe", back_populates="recipe", cascade="delete, all")

class RecipeSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["username"])
    ingredients = fields.List(fields.Nested("RecipeIngredientSchema", only=["ingredient", "amount", "unit", "delete"]))

    # Validation: name, description
    name = fields.String(required=True, validate=Length(min=4, error="The name of the recipe must be at least 4 characters long."))
    description = fields.String(required=True, validate=Length(min=4, error="The description of the recipe must be at least 4 characters long, please add keywords like Keto, Vegan, Gluten Free, to describe your recipe."))

    class Meta:
        fields = ("recipe_id", "name", "description", "is_predefined", "created_at", "user", "ingredients")
        ordered = True

# To handle a single recipe object
recipe_schema = RecipeSchema()

# To handle a list of recipe objects
recipes_schema = RecipeSchema(many=True)