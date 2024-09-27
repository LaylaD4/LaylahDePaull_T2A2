# DOCUMENTATION

## R1. Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

My API is designed to help people plan and prepare healthy, home-cooked meals more easily. In Australia, approximately 13 million adults and 1.3 million children and adolescents are overweight or obese, according to the Australian Bureau of Statistics (ABS) [1]. Obesity significantly increases the risk of chronic diseases such as heart attack, stroke, type 2 diabetes, and certain cancers; many of which are preventable through better dietary choices [2]. While fast food and processed foods offer convenience in our fast paced lives, they contribute to a growing health crisis, placing a massive burden on the healthcare system and, sadly, reducing both the quality and length of life of many people.

Given the rising prevalence of diet related illnesses, it is more crucial than ever to encourage people to consume wholesome, real food prepared at home. However, the demands of modern life often make it challenging for individuals and families to find the time to plan and prepare nutritious meals or to organise all the necessary ingredients.

This API provides a solution by allowing users to create, store, and manage their own recipes (CRUD functionality) or access a wide variety of predefined healthy recipes (with updates and deletions restricted to admin users). Additionally, users can explore recipes created by other users, catering to diverse dietary preferences such as Keto, Low Carb, Paleo, Vegan, Vegetarian, Pescatarian, Dairy-Free, and Gluten-Free. Users can also generate shopping lists based on the recipes they have saved, whether self-created or predefined, saving time and eliminating the hassle of manually creating shopping lists. Therefore, my API addresses the following problems for families and individuals:


**1. Time Management:** Meal planning, shopping for ingredients, and preparing meals can be time consuming, especially for individuals or families with heavy work schedules and other commitments. As a result, eating healthy, home-cooked meals often becomes a lower priority. The challenge is finding the time to consistently plan and prepare nutritious and varied meals that are enjoyable, without dedicating significant time and effort. My Healthy Meal Planner API alleviates this burden by simplifying the entire meal planning process. Users can choose to create their own tailored recipes when they have time, or they can browse through the many predefined (admin-created) or user-created recipes already available in the database. Once they have selected and stored their preferred recipes, they can generate shopping lists with the exact ingredients and amounts needed for each recipe. This flexibility allows users to efficiently plan meals and avoid unnecessary trips to the shops, ensuring that meal planning becomes a more manageable and less time consuming task.


**2. Dietary Preferences/Restrictions:** In today’s world, there is a growing number of dietary preferences and restrictions, such as Keto, Low Carb, Vegan, Gluten Free, and Dairy Free diets. Finding recipes that meet specific dietary needs can be challenging and time-consuming. My Healthy Meal Planner API addresses this by categorising each recipe in the database according to dietary preferences such as Keto, Vegan, Paleo, Standard, Vegetarian, Low Carb, Pescatarian, Gluten Free, and Dairy Free. This categorisation allows users to filter and select recipes that meet their dietary needs quickly and efficiently, ensuring they are presented only with relevant recipes that align with their dietary requirements and preferences.


**3. Food/Ingredient Management:** When shopping for ingredients, it’s easy to forget necessary items, purchase unnecessary ingredients, or overbuy, leading to food waste and discouragement from cooking at home. My Healthy Meal Planner API helps users manage their ingredients more effectively by generating shopping lists based on the recipes they plan to cook. This ensures that users buy only the ingredients they need and in the exact amounts required for their meals, reducing food waste and unnecessary spending. The API supports users in making cooking at home more economical, environmentally friendly, and less stressful.


**4. Addressing Obesity Crisis:** The obesity crisis, is driven by fast food and processed meals [3], and has led to a surge in the many chronic diseases I mentioned above. With millions of Australians affected, it’s more important than ever to encourage healthier eating habits. My Healthy Meal Planner API addresses this by simplifying the preparation of nutritious, home cooked, unprocessed healthy meals. By providing access to a variety of recipes tailored to dietary preferences like Keto and Low Carb, and by generating precise shopping lists, the API makes it easier for users to choose healthy meals over unhealthy ultraproccessed options. This allows for better dietary choices, helping to combat obesity and reduce the associated health risks.


**References:**  

1. [Overweight and obesity](https://www.aihw.gov.au/reports/overweight-obesity/overweight-and-obesity/contents/overweight-and-obesity#how_common_overweight)<br>
2. [Health Risks of Overweight & Obesity](https://www.niddk.nih.gov/health-information/weight-management/adult-overweight-obesity/health-risks#:~:text=Excess%20fat%20may%20also%20damage,%2C%20kidney%20disease%2C%20and%20death.)<br>
3. [Macronutrient (im)balance drives energy intake in an obesogenic food environment: An ecological analysis](https://pubmed.ncbi.nlm.nih.gov/36321270/)

## R2. Describe the way tasks are allocated and tracked in your project.

For my Healthy Meal Planner API, I used [Trello](https://trello.com/b/zpkuS1jz/api-webserver), a visual management tool, to allocate and track tasks throughout the project. I took full advantage of Trello's card and checklist system, which provided a clear and organised method for managing the tasks required to complete my API. By adopting Trello as my task management tool, which follows a visual project management style closely related to Kanban, I adhered to Agile principles that guided my workflow, ensuring efficiency, flexibility, and continuous improvement.

To manage the development process of my API, I created a series of Trello cards, each representing a specific feature or functionality that I needed to implement. Each Trello card included a brief description of the task and a detailed checklist of the related subtasks necessary to complete that feature or functionality. By using Trello, my cards or tasks were organised into columns representing different stages of progress throughout my API project, that is; "To Do," "In Progress," and "Done."

Throughout the build of my API, the use of Agile principles, in particular Kanban methodology, allowed me to manage tasks effectively. Using Kanban's core practices of "Visualising Work", "Limiting Work In Progress WIP", "Managing Flow", and "Continuous Improvement", I was able to keep track of progress, focus on one task at a time, quickly address any issues, and continuously refine the development process of my API to enhance efficiency and adaptability. Below are some examples of how I implemented some of Kanban's core practices:

- **Visualising Work:**
For my Healthy Meal Planner API, I used Trello’s board to clearly visualise all the tasks I needed to complete. For example, I created a Trello card titled "User Account feature" that included subtasks like "Create User model and Schema", "Create user controller", "Implement Registration endpoint", and so on. This card was moved through the columns from "To Do" to "In Progress" to "Done," allowing me to easily track the progress of this essential feature from start to finish.

- **Limiting Work In Progress:**
To maintain focus and efficiency, I was careful to limit the number of tasks I had at any one time in the "In Progress" column. For instance, while working on the "Recipe Management" feature, which is at the core of my API's functionality, I ensured that I only had this task active. This meant completing all subtasks like "Create Recipe model," "Create Recipe Schema", "Implement get all recipes endpoint", "Implement create a recipe endpoint", and so on before moving on to the next feature. This approach reduced multitasking and allowed me to concentrate fully on each task, enhancing productivity.

- **Managing Flow:**
I closely monitored the flow of work to prevent delays. For example, while developing the "User Recipe Management" feature, I noticed the task was stuck in "In Progress" due to challenges with aggregating ingredient quantities when different units were used for the same ingredient. By identifying this obstacle, I was able to recognise the complexity of the issue and adjust my priorities accordingly. Although I wasn't able to fully resolve the issue during this phase, I made necessary adjustments to keep the rest of the project moving forward, ensuring that overall progress remained on schedule.

- **Continous Improvement:**
Throughout the project, I regularly reviewed the Trello board to assess progress and identify areas for improvement. For example, after implementing the "Recipe Management feature", I realised that the validation logic for recipe descriptions was insufficient for allowing users to store and search recipes based on specific dietary needs or preferences (Keto, Vegan etc). This resulted in the suboptimal implementation of an essential feature. Based on my review process, I enhanced the validation method using Marshmallow's @validates decorator to ensure that recipe descriptions strictly adhered to predefined dietary categories, thereby improving the overall user experience when adding and searching for recipes. This approach allowed my API project to continuously evolve and improve.

Therefore, by using Trello for task management and applying the Agiles methodology of Kanban and it's core practices, the development of my Healthy Meal Planner API was organised, efficient, and clearly tracked from start to finish. This method ensured that all tasks were completed in a timely manner, and that I was able to deliver my API project successfully with all necessary features and functionality.

### Screenshots: [My Trello Board](https://trello.com/b/zpkuS1jz/api-webserver)

#### 1. My Trello Board

![My Trello Board](docs/trello_board.png)

#### 2. Initial Meal Planner API Setup Trello Card

![My Trello Board](docs/trello_initial.png)

#### 3. User Account Feature Trello Card

![My Trello Board](docs/trello_user.png)

#### 4. Recipe Management Feature Trello Card

![My Trello Board](docs/trello_recipe.png)

#### 5. User Recipe Management Feature Trello Card

![My Trello Board](docs/trello_userrecipe.png)

#### 6. Recipe-Ingredient Model and Schema Trello Card

![My Trello Board](docs/trello_recipeingredient.png)

#### 7. Ingredient Model and Schema Trello Card

![My Trello Board](docs/trello_ingredient.png)

#### 8. CLI Controller Trello Card

![My Trello Board](docs/trello_cli.png)

#### 9. Design ERD Diagram For API Trello Card

![My Trello Board](docs/trello_erd.png)

#### 10. Marshmallow Validation and Global Error Handling Trello Card

![My Trello Board](docs/trello_marshmallow.png)

**References:** 

1. [My Trello Board](https://trello.com/b/zpkuS1jz/api-webserver)
2. [4 Kanban Principles for Agile Project Management](https://www.atlassian.com/agile/project-management/kanban-principles)
3. [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)


## R3. List and explain the third-party services, packages and dependencies used in this app.

In developing my Healthy Meal Planner API, I used many third-party services, packages, and dependencies that were essential to the functionality my application. Below, I will describe in detail all the services, packages, and dependencies used, along with examples of how they are implemented in my API: 

### 1. Flask

Flask is what's known as a lightweight web framework for Python, designed to be simple and flexible for developers. It adheres to the Web Server Gateway Interface (WSGI) standard, which establishes a universal interface between web servers and web applications. Flask offers essential features like routing, request handling, and templating with Jinja2. Its modular design allows developers to easily extend it with additional Python libraries to enhance an application's functionality. This combination of modularity and simplicity makes Flask a popular choice among developers for building a wide range of web applications. 

Below is an example of how I created and configured my Flask app instance, setting configurations like SQLALCHEMY_DATABASE_URI and JWT_SECRET_KEY. This was done within the create_app function, which serves as an 'application factory' in Flask.

```python
fromflask import Flask 

def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
    return app
```

Flask handles the routing for my API, allowing it to support various HTTP methods like GET, POST, PUT/PATCH, and DELETE. Below is an example from my recipe_controller.py file, demonstrating a route that fetches (GET) all recipes:

```python
@recipe_bp.route("/", methods=["GET"])
def get_all_recipes():
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt)
    return recipes_schema.dump(recipes)
```

#### References

1. [What Is Flask and How Do Developers Use It? A Quick Guide](https://careerfoundry.com/en/blog/web-development/what-is-flask/)
2. [What is Flask? Overview of the Flask Python Framework in 2024](https://flatirons.com/blog/what-is-flask-overview-of-the-flask-python-framework-2024/)

### 2. SQLAlchemy and Flask-SQLAlchemy

SQLAlchemy is an Object-Relational Mapping (ORM) library for Python that bridges the gap between a Python application, like the API I’ve built, and a relational database, such as SQLite, MySQL, or PostgreSQL; which I used to store my Meal Planner (meal_planner_db) data. With SQLAlchemy, developers can interact with databases using Python objects and methods instead of writing raw SQL queries, and therefore gives one the ability to use the database's SQL functionalities. SQLAlchemy provides a comprehensive set of tools for creating and managing database schemas, querying data, and handling relationships between different models. Below is an example of how I used SQLAlchemy in my API user.py file to define the User model that maps to a table ("users") in my Meal Planner database (meal_planner_db):

```python
# The User class inherits from db.Model, which makes it a SQLAlchemy model. SQLAlchemy will use this class definition to create a corresponding table in the database.
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=lambda: datetime.now(timezone.utc).date())
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships
    recipes = db.relationship("Recipe", back_populates="user", cascade="all, delete")
    user_recipes = db.relationship("UserRecipe", back_populates="user", cascade="all, delete")
```

While SQLAlchemy provides the core ORM functionality and can be used independently in any Python application, Flask-SQLAlchemy is an extension specifically designed to integrate SQLAlchemy seamlessly with Flask applications. It simplifies the use of SQLAlchemy within Flask by managing the application's settings, establishing the database connection using the configuration details provided by Flask, and integrating with Flask's session management to track user interactions effectively. 

Below is an example of how Flask-SQLAlchemy is used to initialise the SQLAlchemy instance in init.py, connect it to the Flask app instance in main.py, and interact with the database session in recipe_controller.py:

```python
from flask_sqlalchemy import SQLAlchemy

# Creates an instance of SQLAlchemy that is specifically designed to work with Flask, due to the Flask-SQLAlchemy extension. (init.py)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # Connecting the Flask app instance to the SQLAlchemy instance (db) making it possible to use SQLAlchemy within the Flask app. (main.py)
    db.init_app(app)
    return app

# Example of querying the database using Flask-SQLAlchemy (recipe_controller.py)
stmt = db.select(Recipe)
recipes = db.session.scalars(stmt)
```

Therefore, in my API, Flask-SQLAlchemy manages the connection to the database, enabling me to perform database queries using the ORM in a Pythonic way. It also ensures that database sessions are properly handled within each request, including committing transactions when necessary.

#### References

1. [How to Use Flask-SQLAlchemy to Interact with Databases in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)
2. [What is SQLAlchemy?](https://www.educative.io/answers/what-is-sqlalchemy)

### 3. Marshmallow and Flask-Marshmallow

Marshmallow is a Python library that helps convert complex data types into simple Python data types, which can then be easily turned into formats like JSON and vice versa. It's commonly used in API's to handle data that comes from or goes to the client-side. Marshmallow also has built in validation functionality to ensure that any input data meets a specified criteria before it gets processed or saved to a database, making it easier to ensure that all data exchanged with the database is correct and consistent.

Below is an example of how I used Marshmallow in my API to define my Userschema for user input, including validation rules to ensure that the data meets specific criteria before it is processed or saved to the database.

```Python
# Importing necessary modules from Marshmallow for field definitions in UserSchema and validation for username, email, and password.
from marshmallow import fields, validate  
# Importing the specific validators I chose to use for the field's; username, email, and password
from marshmallow.validate import Length, And, Regexp 

# Defining a schema for the User model using Marshmallow to serialise and deserialise the fields: username, email, and password.
class UserSchema(ma.Schema):
    # Define the 'username' field as a string that is required and must be at least 4 characters long, using Length validator.
    username = fields.String(
        required=True,  
        validate=Length(min=4, error="Your username must be at least 4 characters long.") 
    )

    # Define the 'email' field as a string that is required and must be in a valid email format, using the Email validator.
    email = fields.String(
        required=True,
        validate=validate.Email(error="Your email address must be in a valid format.")
    )

    # Define the 'password' field as a string that is required and must meet multiple validation criteria, using the Length, and Regexp validators.
    password = fields.String(
        required=True, 
        validate=And(
            Length(min=6, error="Your password must be at least 6 characters long."),  
            Regexp("^[A-Z].*$", error="Your password must start with an uppercase letter."),
            Regexp(".*\\d.*$", error="Your password must contain at least one number.")
        )
    )
```

While Marshmallow provides the core functionality for serialisation, deserialisation, and validation, as demonstrated above for my API, it can be used independently in any Python application. However, Flask-Marshmallow adds an extra layer of integration specifically designed for Flask applications. It simplifies the use of Marshmallow by making it easier to handle request data and format responses within the Flask environment.

Below is an example of how Flask-Marshmallow is used to integrate Marshmallow schemas within my Flask API, initialising it in init.py, and integrating it in main.py:

```Python
from flask_marshmallow import Marshmallow

# Initialise Marshmallow instance (init.py)
ma = Marshmallow()

# main.py
def create_app():
    app = Flask(__name__)
    
    # Flask-Marshmallow is specifically integrated with the Flask API here, connecting the Marshmallow instance to the Flask application.
    ma.init_app(app)
    
    return app
```

This integration ensures that Marshmallow's serialisation, deserialisation, and validation features work seamlessly within the Flask environment, allowing easy and consistent handling of data across different routes and models.

#### References

1. [Marshmallow: Serialization and Deserialization Like a Pro](https://medium.com/@pijpijani/marshmallow-in-python-a-powerful-tools-for-serialization-and-deserialization-84ea564a3a2a)
2. [Object validation and conversion with Marshmallow in Python](https://circleci.com/blog/object-validation-and-conversion-with-marshmallow/)

### 4. Flask-Bcrypt

Bcrypt is a Flask extension that enables secure hashing and verification of passwords within a Flask application. Hashing is the process of converting often sensitive data, such as a password or passcode, into a string of random characters of fixed length, resulting in what's known as a hash. These hashes are unique and are used to store sensitive information in a database instead of the actual passwords. Bcrypt uses the Blowfish cipher algorithm for hashing, which is designed to be slow, making it difficult and time consuming for hackers to crack. Hashing only goes in one direction, meaning that once data is transformed into a hash, it can not be easily reversed back to its original form. Therefore, using an extension like Bcrypt ensures that user passwords are stored securely, and so reducing the risk of security breaches.

In my API project, I used Bcrypt to securely hash user passwords before storing them in the Meal Planner database, ensuring that the actual passwords remain protected, as they are stored as secure hashes instead of plain text. Below is an example of how Bcrypt was implemented in my API file auth_controller.py, and how a password hash looks in the database:

```Python
# Bcrypt instance import
from init import bcrypt 

# Here, a user's password is hashed before saving it to the database:
user.password = bcrypt.generate_password_hash(password).decode("utf-8")

# Below is the "users" table from my Meal Planner database, as you can see in the password column, each users password is a hash.
meal_planner_db=# SELECT * FROM users;

 user_id |  username   |         email         |                           password                           | created_at | is_admin 
---------+-------------+-----------------------+--------------------------------------------------------------+------------+----------
       1 | layla_admin | admin@mealplanner.com | $2b$12$QlJs/kjsBYofXW6PlaDMOOc.Ki2gmn23dKanqThMTufJX6mgTuX/. | 2024-09-25 | t
       2 | elise04     | elisebc04@email.com   | $2b$12$RCOpRcJU70pKEYHmtsOJAeNszrMlYgjXwGxsRJCD7t2S/Su2j1WFW | 2024-09-25 | f
```

#### References

1. [Hashing in Action: Understanding bcrypt](https://auth0.com/blog/hashing-in-action-understanding-bcrypt/)
2. [Password Hashing with Bcrypt in Flask](https://www.geeksforgeeks.org/password-hashing-with-bcrypt-in-flask/)

### 5. Flask-JWT-Extended

Flask-JWT-Extended is an extension that adds JSON Web Token (JWT) authentication to Flask applications, providing a secure way to manage user sessions, such as when a user logs in. JWTs are used to securely transmit information between systems, like a client and a server. A JWT consists of three parts: the header, which specifies the token type and algorithm; the payload, which contains user data; and the signature, which ensures the token’s integrity. These components are combined into a single string separated by dots. JWTs can have expiration times, making them valid for only a limited period, which is useful for authenticating users in web applications. This extension simplifies the process of creating, sending, and validating JWTs in a Flask application.

For instance, in my API, after a user successfully logs in, a JWT is generated using the create_access_token function, which includes the user's unique ID (user_id) and an expiration time. This token is then returned to the client and must be included in the Authorisation header for any subsequent requests to protected routes. The @jwt_required decorator is used on these protected routes, ensuring that the JWT is present and valid, thereby maintaining secure access across the API.

Below is an example from my API project in the auth_controller.py file, where Flask-JWT-Extended is used to create and return a JWT token during user login, and a protected route that updates a user's account details. The protected route uses the @jwt_required decorator to ensure that only requests with a valid JWT token can access it:

```Python
from flask_jwt_extended import create_access_token, jwt_required

# User login route 
@auth_bp.route("/login", methods=["POST"])
def login_user():
    body_data = request.get_json()

    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)

    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # GENERATE JWT token with user_id as identity and set expiration time:
        token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
        return {"email": user.email, "is_admin": user.is_admin, "token": token}, 200
    else:
        return {"error": "Invalid email or password"}, 400

# PROTECTED route to update a users account details, that requires a valid JWT, with the use of @jwt_required().
@auth_bp.route("/users", methods=["PUT", "PATCH"])
@jwt_required()
def update_user():
```

#### References

1. [What are the benefits of using Flask-JWT-Extended for JWT authentication in Flask applications?](https://medium.com/@sujathamudadla1213/what-are-the-benefits-of-using-flask-jwt-extended-for-jwt-authentication-in-flask-applications-ec503c25e885#:~:text=Flask%2DJWT%2DExtended%20is%20a,secure%2C%20stateless%2C%20and%20flexible.)
2. [Understanding JWT and how to implement a simple JWT with Flask](https://4geeks.com/lesson/what-is-jwt-and-how-to-implement-with-flask)

### 6. Psycopg2-Binary

Psycopg2-Binary is a PostgreSQL adapter for Python that acts as the bridge between your Python application and a PostgreSQL database. Essentially, it’s the tool that connects your Flask app to a PostgreSQL database, functioning as the engine that ensures your Python code interacts with the database correctly.

Moreover, Psycopg2-Binary lets your Python code connect to a PostgreSQL database, run SQL queries, and handle tasks like adding, updating, or deleting records. The "binary" version is a pre-compiled, self-contained package, simplifying setup by eliminating the need for additional dependencies, making it an excellent choice for beginners. In Flask applications, Psycopg2-Binary works with Flask-SQLAlchemy to manage communication between your Python code and the PostgreSQL database, ensuring smooth and efficient database interactions.

For example, in my .env file, I define the DATABASE_URL for connecting to the PostgreSQL database through Psycopg2-Binary. This URL is then used in main.py to set up the database connection configuration:

```Python
# This is the database URL connecting to the PostgreSQL database using Psycopg2 as the adapter.
DATABASE_URL = "postgresql+psycopg2://layla_dev:..."

# Retrieves the database URL from the environment variable
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
```

#### References

1. [When and How to Use Psycopg2](https://www.timescale.com/blog/when-and-how-to-use-psycopg2/)
2. [Comparing psycopg2-binary vs psycopg2 in Python](https://www.geeksforgeeks.org/comparing-psycopg2-binary-vs-psycopg2-in-python/)

### 7. Python-Dotenv

Python-Dotenv is a package that loads environment variables from a .env file into your Python environment. This is useful for managing settings like database connections, API keys, and secret keys without hardcoding them into your application. By using Python-Dotenv, you keep sensitive information, such as database passwords and JWT secret keys, out of your code, making your application more secure. It also simplifies the process of moving your application from development to production, as you can simply update the .env file with new settings, and the application will automatically use them.

For example, in the main.py file, environment variables that configure the Flask application, such as the database connection and JWT secret key, are loaded and used. These variables are stored in the .env file:

```Python
# main.py file
import os
# Configures the Flask app to use the environment variables that loads from the .env file
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

# .env file
# Defines the database connection details and store them securely in the .env file
DATABASE_URL = "postgresql+psycopg2://layla_dev:..."
# Stores the JWT secret key, used for signing tokens, in the .env file to keep it secure
JWT_SECRET_KEY = ""
```

#### References

1. [Using Py Dotenv (python-dotenv) Package to Manage Env Variables](https://configu.com/blog/using-py-dotenv-python-dotenv-package-to-manage-env-variables/#:~:text=Python%20Dotenv%20is%20an%20open,different%20settings%20for%20different%20environments.)

## R4. Explain the benefits and drawbacks of this app’s underlying database system.

## R5. Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

## R6. Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. <br><br>This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

## R7. Explain the implemented models and their relationships, including how the relationships aid the database implementation. <br><br>This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

## R8. Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:
- ## HTTP verb
- ## Path or route
- ## Any required body or header
- ## Response