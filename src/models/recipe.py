from init import db, ma
from marshmallow import fields, validates, ValidationError
from datetime import datetime, timezone
from marshmallow.validate import Length, And, Regexp, OneOf

VALID_DESCRIPTIONS = ("Keto", "Vegan", "Paleo", "Standard", "Vegetarian", "Low Carb", "Pescatarian", "Gluten Free", "Dairy Free")

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
    recipe_ingredients = db.relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete")
    user_recipes = db.relationship("UserRecipe", back_populates="recipe", cascade="delete, all")

class RecipeSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["username"])
    recipe_ingredients = fields.List(fields.Nested("RecipeIngredientSchema", only=["ingredient", "amount", "unit", "delete"]))

    # Validation: name, description
    name = fields.String(required=True, validate=And(Length(min=4, error="The name of the recipe must be at least 4 characters long."), Regexp("^[A-Z][A-Za-z0-9 ]+$", error="The recipe name must start with a capital letter, and have alphanumeric characters.")))
    description = fields.String(required=True)

    # Makes sure only (description) :
    @validates("description")
    def validate_description(self, value):
        # Split the given description into individual words
        words = value.split(", ")
        
        # Ensure each word is valid and capitalised, separated by a comma (,)
        for word in words:
            if word not in VALID_DESCRIPTIONS:
                raise ValidationError(f"The '{word}' is not a valid description for a Recipe. The only valid options are: {', '.join(VALID_DESCRIPTIONS)}. Please pick one or more that accurately describes your Recipe. Note; The descriptions are case sensitive, and use a comma (,) to separate each word eg; 'Gluten Free, Keto'.")
        
        # If the value is valid - return
        return value

    class Meta:
        fields = ("recipe_id", "name", "description", "is_predefined", "created_at", "user", "recipe_ingredients")
        ordered = True

# To handle a single recipe object
recipe_schema = RecipeSchema()

# To handle a list of recipe objects
recipes_schema = RecipeSchema(many=True)