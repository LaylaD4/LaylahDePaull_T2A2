from init import db, ma
from marshmallow import fields

class Recipe(db.Model):
    __tablename__ = "recipes"
    
    recipe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    is_predefined = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Date)
    # Create Foreign Key that references 'users' table
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="recipes")
    ingredients = db.relationship("RecipeIngredient", back_populates="recipe")


class RecipeSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["user_id", "username"])
    ingredients = fields.List(fields.Nested("RecipeIngredientSchema", only=["ingredient", "amount", "unit"]))

    class Meta:
        fields = ("recipe_id", "name", "description", "is_predefined", "created_at", "user", "ingredients")
    

# To handle a single recipe object
recipe_schema = RecipeSchema()

# To handle a list of recipe objects
recipes_schema = RecipeSchema(many=True)