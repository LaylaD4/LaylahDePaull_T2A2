from init import db, ma
from marshmallow import fields, validate

class Ingredient(db.Model):
    __tablename__ = "ingredients"
    
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationships
    recipe_ingredients = db.relationship("RecipeIngredient", back_populates="ingredient")
    

# Ingredient Schema
class IngredientSchema(ma.Schema):
    # Validate
    name = fields.String(required=True, validate=validate.Length(min=2, error="Please add the ingredient's name."))
    class Meta:
        fields = ("ingredient_id", "name")
