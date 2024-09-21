from init import db, ma
from marshmallow import fields
from datetime import datetime, timezone

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


class RecipeSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["username"])
    ingredients = fields.List(fields.Nested("RecipeIngredientSchema", only=["ingredient", "amount", "unit"]))

    class Meta:
        fields = ("recipe_id", "name", "description", "is_predefined", "created_at", "user", "ingredients")
        ordered = True

# To handle a single recipe object
recipe_schema = RecipeSchema()

# To handle a list of recipe objects
recipes_schema = RecipeSchema(many=True)