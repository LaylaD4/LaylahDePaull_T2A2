from init import db, ma
from marshmallow import fields, validate
from marshmallow.validate import Length, And, Regexp

class Ingredient(db.Model):
    __tablename__ = "ingredients"
    
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationships
    recipe_ingredients = db.relationship("RecipeIngredient", back_populates="ingredient")
    

# Ingredient Schema
class IngredientSchema(ma.Schema):
    # Validate
    name = fields.String(required=True, validate=And(Length(min=4, error="Please add the ingredient's name, it must be longer that 4 letters."), Regexp("^(?:[A-Z][a-z]*)(?: [A-Z][a-z]*)*$", error="The ingredient name must start with a capital letter, with all following words, also being capitalised, the name should only have alphabet characters too.")))
    class Meta:
        fields = ("ingredient_id", "name")
