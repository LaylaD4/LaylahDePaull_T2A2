from flask import Blueprint
from init import db, bcrypt
from models.user import User

db_commands = Blueprint("db", __name__)

# Command to create tables, eg; 'flask db create'.
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

# Command to seed tables, eg; 'flask db seed'.
@db_commands.cli.command("seed")
def seed_tables():
    # Create a list of User instances
    users = [
        User(
            username = "layla_admin",
            email = "admin@mealplanner.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin = True
        ), User(
            username = "elise04",
            email = "elisebc04@email.com",
            password = bcrypt.generate_password_hash("qwerty12").decode("utf-8")
        )
    ]

    # Add the users list
    db.session.add_all(users)
    # Commit the changes
    db.session.commit()
    # Send an acknowledgment message
    print("Tables seeded")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")