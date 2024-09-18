from init import db, ma
from marshmallow import fields

class ShoppingListItem(db.Model):
    __tablename__ = "shopping_list_items"
    shopping_list_item_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    # Create Foreign Key that references 'shopping_lists' table
    shopping_list_id = db.Column(db.Integer, db.ForeignKey("shopping_lists.shopping_list_id"), nullable=False)
    # Create Foreign Key that references 'ingredients' table
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.ingredient_id"), nullable=False)

    # Relationships
    shopping_list = db.relationship("ShoppingList", back_populates="items")
    ingredient = db.relationship("Ingredient", back_populates="shopping_list_items")


class ShoppingListItemSchema(ma.Schema):
    ingredient = fields.Nested("IngredientSchema", only=["ingredient_id", "name"])
    
    class Meta:
        fields = ("shopping_list_item_id", "ingredient", "amount", "unit")
