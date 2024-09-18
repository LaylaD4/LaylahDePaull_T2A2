from init import db, ma
from marshmallow import fields

class ShoppingList(db.Model):
    __tablename__ = "shopping_lists"

    shopping_list_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    # Create Foreign Key that references 'users' table
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="shopping_lists")
    items = db.relationship("ShoppingListItem", back_populates="shopping_list", cascade="all, delete-orphan")


class ShoppingListSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["user_id", "username"])
    items = fields.List(fields.Nested("ShoppingListItemSchema"))
    class Meta:
        fields = ("shopping_list_id", "name", "created_at", "user", "items")