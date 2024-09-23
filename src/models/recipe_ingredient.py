from init import db, ma
from marshmallow import fields, validate
from marshmallow.validate import Length, And, Regexp, Range

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
    ingredient = fields.Nested("IngredientSchema", only=["name"])
    delete = fields.Boolean(missing=False)
    # Validate
    amount = fields.Float(required=True, validate=validate.Range(min=0.1, error="Please enter an amount that is a positive number, and greter than 0.1."))
    unit = fields.String(required=True, validate=And(Length(min=1, error="The unit of the ingredient you are entering must be at least 1 character long."), Regexp("^[A-Za-z ]+$", error="The ingredients unit must only have alphabet characters.")))

    class Meta:
        fields = ("ingredient", "amount", "unit", "delete")


