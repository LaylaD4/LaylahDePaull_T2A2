from init import db, ma
from marshmallow import fields

# Intermediary table for many-to-many relationship between Recipe and Ingredients
class RecipeIngredient(db.Model):
    __tablename__ = "recipe_ingredients"
    recipe_ingredient_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    # Create Foreign Key that references 'recipes' table
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)
    # Create Foreign Key that references 'ingredients' table
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.ingredient_id"), nullable=False)

    # Relationships
    recipe = db.relationship("Recipe", back_populates="ingredients")
    ingredient = db.relationship("Ingredient", back_populates="recipe_ingredients")


class RecipeIngredientSchema(ma.Schema):
    ingredient = fields.Nested("IngredientSchema", only=["ingredient_id", "name"])

    class Meta:
        fields = ("recipe_ingredient_id", "ingredient", "amount", "unit")


