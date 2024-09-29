# DOCUMENTATION

- **Githib Repository**: [LaylahDePaull_T2A2](https://github.com/LaylaD4/LaylahDePaull_T2A2)

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

In my Flask API project, I use PostgreSQL as the underlying database system. PostgreSQL is an open-source, object-relational database management system (ORDBMS) with a history dating back to the "POSTGRES Project" at the University of California, Berkeley, in 1986. Originally designed to handle complex data types, PostgreSQL has evolved to support standard SQL queries and non-relational data types like JSON, making it highly versatile for modern applications.

PostgreSQL's reliability, scalability, and support for advanced functions and custom data types make it a popular choice for projects ranging from small APIs to large-scale applications used by companies like Apple and Meta. Its open-source nature and strong community support have contributed to its widespread adoption in the developer community.

Below is a discussion of the benefits and drawbacks of this app's underlying database system PostgreSQL, in the discussion, I will also include some examples from my Flask API project.

### BENEFITS OF POSTGRESQL

#### 1. Rich Features & Extensions

PostgreSQL provides a large variety of features and extensions that enhance its utility as a database management system. For example, it supports tablespaces for flexible data storage, asynchronous replication for minimal delay in data replication, and nested transactions, allowing complex operations within independent blocks. In my API, I leverage PostgreSQL's support for complex relationships between tables using SQLAlchemy. Below, is an example from my User model showing how PostgreSQL handles these relationships efficiently:

```Python
# models/user.py
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=lambda: datetime.now(timezone.utc).date())
    is_admin = db.Column(db.Boolean, default=False)

    recipes = db.relationship("Recipe", back_populates="user", cascade="all, delete")
    user_recipes = db.relationship("UserRecipe", back_populates="user", cascade="all, delete") 
```

The cascade="all, delete" option ensures that when a user is deleted, all associated recipes and user_recipes are also removed, demonstrating PostgreSQL's ability to maintain data integrity across complex relationships.

#### 2. Reliability

PostgreSQL is highly regarded for its data integrity and fault tolerance, adhering to the ACID principles (Atomicity, Consistency, Isolation, Durability). These principles ensure that database transactions are reliable and secure, which is crucial for any API handling sensitive user data. PostgreSQL's Write Ahead Logging (WAL) ensures that all changes are recorded before they are applied, protecting against data loss. For example, when a user registers or updates their details, the transactions, such as inserting new records into the users table or updating existing ones, are handled atomically:

```Python
# controllers/auth_controller.py
user = User(username=body_data.get("username"), email=body_data.get("email"))
db.session.add(user)
db.session.commit()
```

The db.session.commit() function ensures that all changes are committed to the database only if the transaction is fully successful, which aligns with PostgreSQL's durability and consistency guarantees. This is particularly beneficial in high traffic environments where multiple transactions might occur simultaneously, as PostgreSQL’s Multi-Version Concurrency Control (MVCC) ensures smooth operation without conflicts.

#### 3. Open Source

PostgreSQL's open-source nature makes it a cost-effective solution for developers and small businesses. There are no licensing fees, which allows an API like mine to scale without any additional costs. Moreover, the open-source community around PostgreSQL is large and active, contributing to its continuous improvement through security patches, feature enhancements, and bug fixes.

The flexibility offered by open source also means that the database can be modified to meet specific needs, making it adaptable to a wide range of applications. This is particularly useful when specific project requirements need unique features or performance optimisations. As a result, PostgreSQL not only provides a cost-effective solution but also a reliable and ever-evolving database system that meets modern development needs.

### DRAWBACKS OF POSTGRESQL

#### 1. Complexity

PostgreSQL’s advanced features can be difficult to manage, particularly for those who are new to relational databases or working on smaller projects, such as a Flask application. While PostgreSQL offers a wide array of powerful features and extensions that significantly enhance its capabilities as a database management system, this complexity can pose challenges. Developers may find it hard to understand and navigate PostgreSQL’s advanced functionalities, such as indexing, complex queries, and extensive configuration options.

For example, setting up and managing table relationships in my API with SQLAlchemy, such as using db.relationship, requires a good understanding of how PostgreSQL handles data relationships. To use it effectively, you need to keep the data accurate and make sure queries run efficiently, even if you aren't explicitly dealing with indexing. Moreover, configuring these relationships correctly is critical. Errors can lead to data integrity issues or performance problems, making PostgreSQL's complexity a potential drawback for less experienced developers.

```Python
# models/recipe.py
recipe_ingredients = db.relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete")
```

#### 2. Performance Considerations

PostgreSQL’s performance can be impacted by several factors, including large tables, inefficient query structures, and complex data relationships. As an applications data grows, these factors become more significant. PostgreSQL, by default, uses sequential scans, where it reads each row in a table to find the required data. This method can become inefficient as tables grow larger, leading to slower query execution times. To improve performance, it’s crucial to understand PostgreSQL’s indexing mechanisms, which allow the database to quickly locate the required data without scanning the entire table. Complex queries that involve multiple joins between tables or aggregations can also place a heavy load on the database, further affecting performance. Therefore, maintaining good performance requires a solid understanding of query optimisation, indexing, and efficient database design.

For example, as the recipes table in my API increases in size, a simple query like the one below could lead to slower query execution times, especially if the database isn't properly optimised. Proper indexing and query optimisation are essential to maintaining performance as an applications data grows in volume and complexity.

 ```Python
 # controllers/recipe_controller.py
stmt = db.select(Recipe)
recipes = db.session.scalars(stmt)
 ```

#### 3. Open Source

While the open-source nature of PostgreSQL is a significant advantage, it also has drawbacks. Unlike commercial databases, PostgreSQL does not come with warranties, liability protection, or guaranteed support. This means that if an issue arises in my API, I must rely on community support or my troubleshooting skills, which might not be as reliable or timely as commercial support options.

Additionally, PostgreSQL’s open-source development model can lead to potential compatibility issues with other software and operating systems. While the community is strong and active, there is always a risk that a feature might be modified or deprecated, potentially affecting the API’s performance or functionality.

#### References

1. [PostgreSQL Advantages and Disadvantages](https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/)
2. [What is PostgreSQL? Introduction, Advantages & Disadvantages](https://www.guru99.com/introduction-postgresql.html)
3. [What is PostgreSQL and how does it compare to other database management systems?](https://www.quest.com/learn/what-is-postgresql.aspx#:~:text=For%20most%20use%20cases%2C%20Postgres,of%20ownership%20compared%20to%20Oracle.)
4. [PostgreSQL: a closer look at the object-relational database management system](https://www.ionos.com/digitalguide/server/know-how/postgresql/)


## R5. Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

In my Meal Planner API, SQLAlchemy, an Object-Relational Mapping (ORM) tool, plays a vital role in managing the database. ORMs simplify working with databases by letting developers use Python instead of writing SQL queries. Below are several key features of SQLAlchemy and how they support my API's functionality.

One of the main benefits of SQLAlchemy is simplifying database interactions. Instead of manually writing SQL queries, developers can define models in Python that represent database tables. For example, a User model corresponds to a users table in the database. This allows developers to easily perform database operations without worrying about SQL syntax.

```Python
# User Model Defined
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=lambda: datetime.now(timezone.utc).date())
    is_admin = db.Column(db.Boolean, default=False)

# Create a new user instance
new_user = User(username ="layla4",
                email = "layla@email.com",
                password = "Abc&123") # Hashed

# Add the user to the session and commit to the database
db.session.add(new_user)
db.session.commit()

# Query the database to retrieve the user by username:
stmt = db.select(User).filter_by(username="layla4")
user = db.session.scalar(user)
```

Another important feature is automated schema generation. When you define a model in Python, SQLAlchemy automatically creates the necessary tables and columns in the database. This keeps the database structure consistent with the code, saving developers from manually updating the database schema as the project evolves. For example, defining my API Recipe model automatically generates a recipes table with the necessary attributes:

```Python
# Recipe model (SQLAlchemy generates the corresponding table)
class Recipe(db.Model):
    __tablename__ = "recipes"
    
    recipe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    is_predefined = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Date, default=lambda: datetime.now(timezone.utc).date())
    # Create Foreign Key that references 'users' table
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

# Table Generated:
                                         Table "public.recipes"
    Column     |          Type          | Collation | Nullable |                  Default                   
---------------+------------------------+-----------+----------+--------------------------------------------
 recipe_id     | integer                |           | not null | nextval('recipes_recipe_id_seq'::regclass)
 name          | character varying(100) |           | not null | 
 description   | character varying(100) |           |          | 
 is_predefined | boolean                |           |          | 
 created_at    | date                   |           |          | 
 user_id       | integer                |           | not null | 
```

SQLAlchemy is also great at relationship management. Relational databases contain related tables, and managing these relationships can be complex. SQLAlchemy allows developers to define relationships directly in their models, simplifying the process of joining related tables. For example, in my API; a User can have multiple Recipes, and each Recipe can include many Ingredients. SQLAlchemy takes care of the foreign keys and connections, making it simple to manage this related data.

In addition to handling relationships, SQLAlchemy manages sessions and transactions. It allows developers to make multiple changes to the database and commit them all at once. This ensures that all changes are saved together, maintaining data consistency. In my API, when a new recipe is added, SQLAlchemy keeps track of changes in a session. Once you call session.commit(), all the changes are saved to the database at the same time, ensuring data integrity and consistency.

Finally, SQLAlchemy integrates with Marshmallow for data validation and serialisation. Marshmallow ensures that only valid data (eg; correct email formats, required recipe names) is stored in the database. It also serialises complex objects into JSON for API responses. For example, RecipeSchema serialises recipe data, including nested fields like the associated user and ingredients, into a structured JSON format, ensuring reliables API responses.

In conclusion, SQLAlchemy ORM greatly simplifies database management by offering features like simplifying interactions, automating schema creation, managing relationships, handling transactions, and ensuring data validation. These features make it an essential tool for efficiently managing databases in APIs like my Meal Planner.

#### References

1. [What is SQLAlchemy Used For? An Overview with Practical Examples](https://www.cdata.com/blog/what-is-sqlalchemy)
2. [Must know package to build your system — Real world examples with SQLAlchemy in Python](https://medium.com/@danielwume/must-know-package-to-build-your-system-real-world-examples-with-sqlalchemy-in-python-db8c72a0f6c1)


## R6. Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. <br><br>This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.<br>

![Meal Planner ERD](/docs/meal_planner_erd.png)

### 1. Explanation of How the Relations Between the Diagrammed Models will aid the Database Design

- #### User & Recipe: one-to-many (1:N)

    The one-to-many relationship between the users and recipes tables is fundamental to the database design. This relationship allows each user to create multiple recipes, while ensuring that each recipe is linked only to a single user. By storing a foreign key (user_id) in the Recipes table, the database efficiently tracks which user created which recipes. This setup organises recipes under specific users, making it easy to create new recipes, retrieve recipes created by a particular user, and ensure that users can update or delete only their own recipes. Meanwhile, it allows users to browse or save recipes created by others or by admins (predefined), without having the ability to modify or delete them.

- #### User & UserRecipe: one-to-many (1:N)

    The one-to-many relationship between users and user_recipes allows each user to have multiple entries in the user_recipes table, which represents the recipes they have saved to create meal plans and shopping lists of ingredients. This relationship is crucial for tracking which recipes are saved by each user without needing to duplicate the recipes themselves. The user_recipes table tracks which users have saved which recipes by storing both the user_id and recipe_id. This setup prevents redundancy, as the same recipe can be saved by multiple users without being duplicated in the database. It also simplifies the retrieval of a user’s saved recipes, making the API personalised, and more user-friendly.

- #### Recipe & UserRecipe: one-to-many (1:N)

    The one-to-many relationship between recipes and user_recipes tables ensures that a single recipe can be saved by multiple users. The user_recipes table stores the recipe_id, linking each saved recipe to the recipe table. This setup allows the same recipe to be saved by different users without needing to store the recipe multiple times. It efficiently manages user interactions with recipes, ensuring that the database remains organised and scalable.

- #### Recipe & RecipeIngredient: one-to-many (1:N)

    The one-to-many relationship between the recipes and recipe_ingredients tables allows each recipe to be fully detailed by listing all its individual ingredients, along with their specific amounts and units. This setup means that a single recipe can have multiple recipe_ingredient entries, each specifying a different ingredient with its exact quantity. This relationship helps the database store detailed information about a recipe’s components in an organised way. By separating ingredient details into the recipe_ingredients table, the design avoids redundancy and makes it easy to update or modify recipes. If the ingredients or quantities in a recipe need to change, the relevant recipe_ingredient entries can be updated without impacting other recipes, ensuring efficient and flexible management of recipe data.

- #### Ingredient & RecipeIngredient: one-to-many (1:N)

    The one-to-many relationship between the ingredients and recipe_ingredient tables allows each ingredient to be used in multiple recipes. This means that a single ingredient can have multiple recipe_ingredient entries, each linking it to a different recipe or specifying a different quantity and unit for the same ingredient in various recipes. This setup enables the database to manage ingredient data efficiently by storing each ingredient only once in the ingredients table. By linking ingredients to recipes through the recipe_ingredients table, the design prevents duplication and ensures that any changes to an ingredient’s details are reflected across all related recipes. This structure simplifies the process of updating ingredient information and ensures consistent, accurate data management throughout the database.


### 2. Explanation of How All Relations are Normalised

The Meal Planner database design, as depicted in the ERD image above, adheres to Third Normal Form (3NF). This design is optimal for reducing redundancy and improving data integrity, following best practices by strictly adhering to the principles of normalisation. Specifically, each table has a primary key, with all columns or attributes containing only atomic values, meaning no repeating groups (1NF). All non-key attributes are entirely dependant on the primary key, with no partial dependencies (2NF). Additionally, there are no transitive dependencies, meaning every attribute depends solely on the primary key (3NF). Below I will explain how each relation is normailsed.


- #### Users Relation

    The User table is in 3NF. It uses user_id as the primary key, with all other attributes like username, email, password, and is_admin depending directly on this key. This ensures that each user’s information is stored in one place without any unnecessary duplication. By keeping user data centralised, the design maintains atomicity (each piece of data is stored in its simplest form), which simplifies data management and ensures consistency across the application.

- #### Recipes Relation

    The recipes table is also in 3NF. The recipe_id serves as the primary key, and all attributes, such as name, description, is_predefined, and created_at, are fully dependent on it. The user_id foreign key links each recipe to the user who created it, ensuring that all data in the Recipe table depends entirely on the primary key, without any partial dependencies (where an attribute depends on only part of a composite primary key). This structure avoids data redundancy and ensures that each recipe is accurately linked to its creator.

- #### Ingredients Relation

    The ingredients table is in 3NF. Each ingredient is uniquely identified by ingredient_id, with the name attribute directly depending on this key. This setup ensures atomicity, meaning each ingredient is stored in its simplest form, avoiding duplicate entries. This structure ensures consistency in ingredient data across all recipes and makes it easier to update or modify ingredients when necessary.

- #### RecipeIngredient Relation

    The recipe_ingredients table is in 3NF, managing the many-to-many relationship between recipes and ingredients. Although it has a primary key (recipe_ingredient_id), my queries focus on the composite key (recipe_id, ingredient_id). The additional attributes of, amount and unit, depend directly on this composite key, ensuring there are no partial dependencies (unnecessary data duplication) or transitive dependencies (indirect data links that depend on other non-key attributes). This setup ensures that each ingredient’s relationship to a recipe is unique, and without redundancy.

- #### UserRecipe Relation

    The user_recipes table, which manages the many-to-many relationship between users and recipes, is also in 3NF. Although it has a primary key (user_recipe_id), my queries rely on the composite key (user_id, recipe_id). This setup ensures that each user's saved recipes are uniquely stored, avoiding unnecessary data duplication.

### 3. Comparison of Normalisation

Normalisation helps organise database tables to reduce redundancy and improve data integrity. My Meal Planner ERD is designed in Third Normal Form (3NF). Below, I’ll explain how the recipes table would look at different levels of normalisation, and why the creation of the recipe_ingredients junction table was essential for achieving the optimal 3NF design.

#### 1. First Normal Form (1NF):

In 1NF, you could store all recipe details, including ingredients, directly in the recipes table. For example, you might have multiple columns for ingredients, along with their corresponding amounts and units, such as ingredient1, amount1, unit1, and so on. While this setup conforms to 1NF because each field contains only one piece of data, it is highly inefficient. It forces you to store the same ingredient multiple times across different recipes, each with varying amounts and units.

#### 2. Second Normal Form (2NF):

In 2NF, all non-key attributes must be fully dependent on the primary key. So, if you stored a recipe's ingredients directly in the recipes table, it would still conform to 2NF, as each ingredient, amount, and unit would depend on the recipe's primary key. However, this design still leads to redundancy because the same ingredient would likely appear in many different recipes, with each recipe having a different amount or unit. To avoid this redundancy, you would separate the ingredients into a distinct table and connect them to the recipes using a junction table.

#### 3. Second Normal Form (3NF):

To achieve 3NF, you need to eliminate all redundancy and ensure that every non-key attribute depends only on the primary key. This is why the recipe_ingredients table becomes essential. This allows you to store each ingredient only once and associate it with different recipes, specifying the amount and unit for each recipe individually. This setup conforms to 3NF because it eliminates redundancy and ensures that every non-key attribute depends only on the primary key, without any indirect dependencies.

#### Refereences

1. [Database Normalization – Normal Forms 1nf 2nf 3nf Table Examples](https://www.freecodecamp.org/news/database-normalization-1nf-2nf-3nf-table-examples/)  
2. [Description of the database normalization basics](https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description)


## R7. Explain the implemented models and their relationships, including how the relationships aid the database implementation. <br><br>This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

### 1. Explain implemented models and their relationships

#### 1. **User Model**

The User model allows a user to create an account, and log in to the meal planner database. Users can create, update, and delete their own recipes, while having access to other users' recipes, and predefined ones created by admins. The relationships in the User model ensures that when a user is deleted, that all their associated recipes and user recipe records are also deleted too, maintaining data integrity.

   - **Attributes**:
     - **user_id:** Serves as the Primary Key for a user entry
     - **username:** Upon registration, a user must enter a username
     - **email:** Upon registration, a user must enter a valid email address, which must be unique.
     - **password:** Upon registration, a user must enter a valid password, which is hashed when stored.
     - **created_at:** This captures the date when the user created their account.
     - **is_admin:** Is a boolean, that defaults to false, and indicates whether the user has admin privileges.

   ### Relationships
   **User to Recipe (One-to-Many)**: Each user can create multiple recipes or none, but each recipe is linked to one and only one user.  
   **User to UserRecipe (One-to-Many)**: A user may not have any recipes saved or stored in their own personal list, but they can add multiple recipes to their personal list if they so choose.  

**Code Example Usage**: In the delete_user route in auth_controller.py, when a user is deleted, all their associated recipes are also deleted due to the cascade="all, delete" option in the relationship.

```Python
db.session.delete(user)
db.session.commit()
```

#### 2. **Recipe Model**

The Recipe model allows users to search for all recipes in the database along with their associated ingredients. Additionally, it enables users to filter recipes based on specific dietary needs or preferences, via the description attribute for keywords like 'Gluten Free', 'Keto', or 'Vegan'.

   - **Attributes**:
     - **recipe_id**: Serves as the Primary Key for a recipe entry
     - **name**: The name of the recipe, must be entered, and be of valid length.
     - **description**: A short description, that only allows a combination of 'VALID_DESCRIPTIONS' to categorise a recipe.
     - **is_predefined**: Is a boolean that defaults to false, indicating whether the recipe is a predefined recipe.
     - **created_at**: This captures the date when a recipe is created.
     - **user_id**: Serves as a Foreign Key referencing the user, who created the recipe.

   ### Relationships
   **Recipe to User (Many-to-One)**: A user can create many recipes, however each recipe must belong to one, and only one user.  
   **Recipe to RecipeIngredient (One-to-Many)**: A recipe can have multiple recipe_ingredients, however, a recipe_ingredient, can belong to one and only one recipe.  
   **Recipe to UserRecipe (One-to-Many)**: A recipe can be saved by multiple users in their personal lists, but a user_recipe entry must correspond to one and only one recipe.

**Code Example Usage**: In the create_recipe route in recipe_controller.py, when a new recipe is created, the user who created it is associated with the recipe:

```Python
recipe = Recipe(
    name = body_data.get("name"),
    description = body_data.get("description"),
    user_id = get_jwt_identity()  
)
db.session.add(recipe)
db.session.commit()
```

#### 3. **Ingredient Model**

This model stores all ingredients for recipes in the database. The relationship between Ingredient and Recipe via the RecipeIngredient model ensures that each ingredient is only stored once, reducing data redundancy, when new recipes and their associated ingredients are added to the database.

   - **Attributes**:
     - **ingredient_id**: Serves as the Primary Key for an ingredient entry.
     - **name**: The name of the ingredient, must be entered, and be of valid length.

   ### Relationships
   **Ingredient to RecipeIngredient (One-to-Many)**: An ingredient can be part of multiple recipe_ingredients, however each recipe_ingredient entry must be associated with one and only one ingredient 

**Code Example Usage**: In the update_recipe route in recipe_controller.py, you can add or update ingredients in a recipe:

```Python
stmt = db.select(Ingredient).filter_by(name=name)
ingredient = db.session.scalar(stmt)
        
if not ingredient:
    ingredient = Ingredient(name=name)
    db.session.add(ingredient)
    db.session.commit() 
```

#### 4. **RecipeIngredient Model**

This model serves as a junction table, managing the many-to-many relationship between the Recipe and Ingredient models. It allows each recipe to have its own specific ingredients, with distinct amounts and units for each ingredient.

   - **Attributes**:
     - **recipe_ingredient_id**: Serves as the Primary Key for a recipe_ingredient entry.
     - **amount**: The quantity of the ingredient must be entered as a float.
     - **unit**: The measurement or unit of the ingredient, must be entered as a string, eg; grams, cup.
     - **recipe_id**: Serves as a Foreign Key referencing the recipe, the reciped_ingredient is associated with.
     - **ingredient_id**: Serves as a Foreign Key referencing the ingredient, the reciped_ingredient is associated with.

   ### Relationships
   **RecipeIngredient to Recipe (Many-to-One)**: A recipe can contain multiple recipe_ingredients, however, each entry in the recipe_ingredients table must be associated with one and only one recipe.  
   **RecipeIngredient to Ingredient (Many-to-One)**: An ingredient can be used in multiple recipe_ingredients, however, each recipe_ingredient entry must be associated with one and only one ingredient.

**Code Example Usage**: When creating or updating a recipe, you use the RecipeIngredient model to associate ingredients with the recipe:

```Python
recipe_ingredient = RecipeIngredient(
    recipe_id=recipe.recipe_id,
    ingredient_id=ingredient.ingredient_id,
    amount=amount,
    unit=unit
)
db.session.add(recipe_ingredient)
db.session.commit()
```

#### 5. **UserRecipe Model**

This model serves as a junction table, managing the many-to-many relationship between between Users and Recipe models. It allows users to save the recipes they want to cook at home, enabling them to create a personalised shopping list with all the necessary ingredients, including their specific amounts and units, for those saved recipes.

   - **Attributes**:
     - **user_recipe_id**: Serves as the Primary Key for a user_recipe entry.
     - **user_id**: Serves as a Foreign Key referencing the user, that the user_recipe is associated with.
     - **recipe_id**: Serves as a Foreign Key referencing the recipe, that the user_recipe is associated with.

   ### Relationships
   **UserRecipe to User (Many-to-One)**: A user can have many user_recipes, however each entry in the user_recipes table must belong to one and only one user.  
   **UserRecipe to Recipe (Many-to-One)**: A recipe can be added to multiple users' recipe lists, however, a user_recipe entry must correspond to one and only one recipe.

**Code Example Usage**: In the add_user_recipe route in the user_recipe_controller.py, a user can add a recipe to their own personal list:

```Python
user_recipe = UserRecipe(user_id=user_id, recipe_id=recipe_id)
db.session.add(user_recipe)
db.session.commit()
```

#### TABLE RELATIONSHIP OVERVIEW

- #### User & Recipe: one-to-many (1:N)

    The relationship between the users table and the recipes table represents a one-to-many relationship. This means that a user can hold an account without creating any recipes (minimum of zero). However, a user has the option to create multiple recipes (maximum of many) while holding an account. Conversely, each recipe must belong to one, and only one user (minimum and maximum of one) or admin (for predefined recipes).

- #### User & UserRecipe: one-to-many (1:N)

    The relationship between the users table and the user_recipes table represents a one-to-many relationship. A user may not have any recipes (minimum of zero) saved or stored in their own personal list, but they can add multiple recipes (maximum of many) to their personal list. Conversely, each entry in the user_recipes table must belong to one and only one user (minimum and maximum of one).

- #### Recipe & UserRecipe: one-to-many (1:N)

    The relationship between the recipes table and the user_recipes table represents a one-to-many relationship. A recipe may not be added to a user's personal recipe list (minimum of zero), but it can be added to multiple users' recipe lists (maximum of many). Conversely, a user_recipe entry must correspond to one and only one recipe (minimum and maximum of one).

- #### Recipe & RecipeIngredient: one-to-many (1:N)

    The relationship between the recipes table and the recipe_ingredients table represents a one-to-many relationship. Each recipe must include at least one recipe_ingredient (minimum of one), but it can also contain multiple recipe_ingredients (maximum of many). Conversely, each entry in the recipe_ingredients table must be associated with one and only one recipe (minimum and maximum of one).

- #### Ingredient & RecipeIngredient: one-to-many (1:N)

    The relationship between the ingredients table and the recipe_ingredients table represents a one-to-many relationship. An ingredient does not need to be used in any recipe (minimum of zero), but it can be used in multiple recipes (maximum of many). Each recipe_ingredient entry must be associated with one and only one ingredient (minimum and maximum of one).

### 2. How the Relationships Aid in Database Implementation

In my Meal Planner API, the relationships between models like users, recipes, and ingredients are essential for keeping the database organised, efficient, and tailored to the API's needs.

First, these relationships ensure efficiency and data integrity. Ingredients are stored in a single ingredients table, and the recipe_ingredients table links them to specific recipes. This means the same ingredient, like “Almond Flour,” is stored only once but can be used in multiple recipes (eg; Keto and Vegan Pancakes). This relationship structure prevents duplication of ingredient data while allowing each recipe to have its own unique amounts and units for the ingredients it has. 

The relationships also enhance the scalability of the database. As more users, recipes, and ingredients are added, the structure handles the increased data without becoming disorganised in any way. New recipes can easily link to existing ingredients without needing to re-enter those ingredients. Therefore, adding new users or recipes doesn’t make the database more complex because the relationships between tables keep everything well organised.

Ease of querying is another benefit of these relationships. For example, the relationship between the users and recipes tables allows you to quickly retrieve all the recipes created by a particular user. Similarly, you can easily query all the ingredients for a specific recipe due to the links between the recipes, recipe_ingredients, and ingredients tables. These relationships make it easy to access data without needing complex queries.

Finally, the relationships directly support user-specific features. For example, users can save their favourite recipes using the user_recipes table, which links users to recipes. This setup allows each user to manage their own personal list of saved recipes without duplicating any recipe data. Users can also manage ingredients for their recipes through the recipe_ingredients table, which stores the amounts and units for each ingredient, making it easy to update or change recipes.

In summary, the relationships in my Meal Planner API not only make the database more efficient and scalable but also support essential features like easy data retrieval, personalised recipe lists, and ingredient management. These relationships ensure the API runs smoothly as it grows and remains very user-friendly.

## R8. Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:
- ## HTTP verb
- ## Path or route
- ## Any required body or header
- ## Response


My API consists of three main controllers, each with various endpoints that enable users to perform a wide range of tasks, from managing user accounts to handling recipe and shopping list data. The auth_controller handles user authentication and account management, the recipe_controller allows for creating, fetching, updating, and deleting recipes, and the user_recipe_controller facilitates the management of a user's personal recipe list and shopping list generation. Below, I will walk through each controller, outlining the HTTP verbs, routes, required body or header data, and expected responses for each endpoint.

## `controllers/auth_controller.py`

### REGISTERING A NEW USER ACCOUNT  
The `/auth/register` endpoint allows a client to create a new user account by sending a POST request with a JSON body containing username, email, and password. The password is securely hashed before storing in the database. The endpoint returns the created user data upon success, or an error message if there’s an issue like missing data or a duplicate email.

### 1. HTTP Verb

- **POST**: This endpoint uses the POST HTTP method, which is used to submit the users registration data of username, email, and password to the server to create a new user account.

### 2. Path or Route

- **Path**: `/auth/register`

### 3. Required Body Data or Header Data

There are no specific headers required for this endpoint. The request body must contain JSON data that includes the following fields when a new user registers an account:  
- **username**: This username must be unique, with a minimum of 4 characters.  
- **email**: This email address must be unique, with the correct email formatting.  
- **password**: This password must be atleast 6 characters in length, and comply with other character rules set. Because it is a password, this field is sensitive, and will be hashed before storing it in the database.  

**Example JSON body** Where a user is creating a new account correctly:

```json
{
  "username": "Lucy",
  "email": "lucy4@email.com",
  "password": "Abc&123"
}
```

### 4. Response

- **Success Response**: If the user successfully creates an account (HTTP Status Code: 201 Created), the API will return:

![Successful User Registration](docs/register_success.png)

- **Error Response**: If the user fails to enter a required field, such as username, email, or password (HTTP Status Code: 400 Bad Request), the API will return:

![Missing User Registration Data](docs/register_missing.png)

- **Error Response**: If the user trys to enter an email that is not unique, and already exists in the database (HTTP Status Code: 400 Bad Request), the API will return:

![User Registration Duplicate Email](docs/register_duplicate.png)

### LOGGING INTO A USER ACCOUNT  
The `/auth/login` endpoint allows a client to log in to a user account by sending a POST request with a JSON body containing an email and password. If those credentials are correct, the server responds with the user's email, their admin status, and a JWT token. If the credentials are incorrect, the server responds with an error message indicating invalid email or password. Upon successful authentication, the API generates a JSON Web Token (JWT) for the user. This token is crucial for accessing other protected endpoints within the application. The token is set to expire after 1 day (expires_delta=timedelta(days=1)).

### 1. HTTP Verb

- **POST**: This endpoint uses the POST HTTP method to submit the user's login data of email and password to the server, where it logs in and authenticates the user by creating a token (JWT).

### 2. Path or Route

- **Path**: `/auth/login`

### 3. Required Body Data or Header Data  

There are no specific headers required for this endpoint. The request body must contain JSON data that includes the following fields:  
- **email**: This email address that the user used to register their account. 
- **password**: The password used, when registering their (user) account together, with the above associated email address.

**Example JSON body** Where a user is correctly logging in to their account:

```json
{
  "email": "lucy4@email.com",
  "password": "Abc&123"
}
```

### 4. Response

- **Success Response**: If the user successfully logs in to their account successfully, that is they used the correct email address, and password combination (HTTP Status Code: 200 OK), the API will return:

![Successful User Login](docs/login_success.png)

- **Error Response**: If the user fails to enter the correct email or password, or if the email is not found, (HTTP Status Code: 400 Bad Request), the API will return:

![Incorrect Password Entered For Login](docs/login_fail.png)  

### UPDATING A USER ACCOUNT (By a user that is not admin) 
The `/auth/users` endpoint allows authenticated users to update specific account details, specifically their username and/or password, using the PATCH method. The request must include a valid JWT token, and users are restricted from changing their email address or admin status. Upon a successful update, the server responds with the updated user data. If the user does not exist or tries to make unauthorised changes, appropriate error messages are returned.

### 1. HTTP Verb

- **PATCH**: This endpoint uses the PATCH HTTP method to update a user's data, such as username and/or password, in the database without replacing the entire user account. The user must be logged in and authenticated via their JWT to perform this action.

### 2. Path or Route

- **Path**: `/auth/users`

### 3. Required Body Data or Header Data  

The request must include a valid JWT token in the Authorisation header. This token is required to authenticate the user making the request. The request body must contain JSON data that includes one or both of the following fields:  
- **username**: The username that the user would like to update or change, assuming it is valid
- **password**: The password that the user would like to update or change., assuming it is valid.

**Example JSON body** Where a user is changing just their username for their account:

```json
{
  "username": "Lucy44"
}
```

### 4. Response

- **Success Response**: If the user successfully changes their username, and they have their valid JWT token entered correctly in the header (HTTP Status Code: 200 OK), the API will return:

![Successful User Patch for Username](docs/userpatch_success.png)

- **Error Response**: If the user attempts to change their email, (HTTP Status Code: 403 Forbidden), the API will return:

![User Trys to Change Email](docs/userpatch_emailerror.png)  

- **Error Response**: If the user attempts to change their admin status, (HTTP Status Code: 403 Forbidden), the API will return:

![User Trys to Change Admin Status](docs/userpatch_adminerror.png)  

### DELETING A USER ACCOUNT 
The `/auth/users/<int:user_id>` endpoint allows authenticated users to delete a user account using the DELETE method. The request must include a valid JWT token, and the user must either be the account owner or an admin to perform the deletion. When a user is deleted, all related data asscociated with that user (user_id), like their recipes and user_recipes saved, are also deleted via cascading. Upon successful deletion, the server returns a confirmation message. If the user doesn’t exist or the deletion is unauthorised, appropriate error messages are also returned.

### 1. HTTP Verb

- **DELETE**: This endpoint uses the DELETE HTTP method to delete a user's account. The user must be recently logged in and authenticated via their JWT to perform this action.

### 2. Path or Route

- **Path**: `/auth/users/<int:user_id>` (Note; `<int:user_id>` is a placeholder for a user's user_id, eg; the int: 3)

### 3. Required Body Data or Header Data  

The user making the request must be either the owner of the account (ie; the user_id matches the user_id from the JWT token) or an admin. There is no body data required to make this request. However, the request must include a valid JWT token in the Authorisation header, to authenticate the user making the request is the owner of the account or is_admin:  

- **Example JWT Token**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNzU3NDE4NiwianRpIjoiMmUyYzZjYWYtMTM1Yi00ZmFkLWFmMGYtZTVmNDVmNjUzNDJhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE3Mjc1NzQxODYsImNzcmYiOiIzMTIxYmQzZS1lZDYzLTQ2NDQtOTYyMS05NmY4MjA5ZDQ1ZGYiLCJleHAiOjE3Mjc2NjA1ODZ9.e6uOPoV1OluxBJmEOjSePp4xLvD1Iq6eIbQo1kp7zVY`


### 4. Response

- **Success Response**: When a user successfully deletes their account, providing they have their valid JWT token entered correctly in the header (HTTP Status Code: 200 OK), the API will return:

![Successful User Deletion](docs/userdelete_success.png)

- **Error Response**: If the user making the request does not have permission to delete the account, that is; they are neither the owner nor an admin (HTTP Status Code: 403 Forbidden), the API will return:

![User Trys to Change Email](docs/userdelete_forbidden.png)  

- **Error Response**: If the user with the specified user_id does not exist in the database., (HTTP Status Code: 404 Not Found), the API will return:

![User Trys to Change Admin Status](docs/userdelete_notfound.png)  

### UPDATING A USER ACCOUNT (By admin only) 
The `/auth/users/<int:user_id>` endpoint allows an admin to update specific details of a user's account using the PATCH method.  The request must include a valid JWT token, and is enforced by the @auth_as_admin_decorator, which checks if the current user has admin privileges. Admins can update a user’s username, email, and is_admin status but are prohibited from changing the user’s password. If the update is successful, the server responds with the updated user data. If the  user doesn’t exist or the admin tries to change the password, appropriate error messages are also returned.

### 1. HTTP Verb

- **PATCH**: This method is used to update specific fields of the user’s account, such as a users; username, email, and admin status. To perform this action, an admin must be logged in and authenticated via their JWT, and the request must pass the @auth_as_admin_decorator check.

### 2. Path or Route

- **Path**: `/auth/users/<int:user_id>` (Note; `<int:user_id>` is a placeholder for the user_id, eg; the int: 3)

### 3. Required Body Data or Header Data    

The request must include a valid JWT token in the Authorisation header. This token is required to authenticate the user making the request. The request body must contain JSON data that includes one or either of the following fields:  
- **username**: The new username for the user being updated.
- **email**: The new email address for the user being updated.
- **is_admin**: The updated admin status (true/false) for the user being updated.

**Example JSON body**: Where a user is being updated (by an admin) to become an admin, recieveing a new username, and email:

```json
{
  "username": "lucy_admin",
  "email": "lucy@mealplanner.com",
  "is_admin": true
}
```

### 4. Response

- **Success Response**: If the update of the user's account details is successful, (HTTP Status Code: 200 OK), the API will return:

![Admin Update Successful](docs/admin_updatesuccess.png)

- **Error Response**: If the user making the request does not have permission to make the update, that is, they are not an admin, and are trying to change their email address (HTTP Status Code: 403 Forbidden), the API will return:

![Non-Admin Trys to Update Users](docs/adminupdate_forbidden.png)

- **Error Response**: If the user with the specified user_id does not exist in the database, when an admin is trying to update an email (HTTP Status Code: 404 Not Found), the API will return:

![Admin Update Can't find User](docs/adminupdate_nouser.png)  

### GETTING ALL USER ACCOUNTS IN THE DATABASE (By admin only) 
The /auth/users endpoint allows an admin to retrieve a list of all users currently registered in the meal planner database using the GET method. The request must include a valid JWT token, and the user must have admin privileges, which are verified by the @auth_as_admin_decorator. If the request is successful, the server returns a list of all users in the database. If the user is not an admin, they will receive a 403 Forbidden error.

### 1. HTTP Verb

- **GET**: This method is used to retrieve a list of all users who currently have accounts in the database. To perform this action, an admin must be logged in and authenticated via their JWT, and the request must pass the @auth_as_admin_decorator check.

### 2. Path or Route

- **Path**: ` /auth/users`

### 3. Required Body Data or Header Data

The user making the request must be an admin, there is no body data required to make this request. However, the request must include a valid JWT token in the Authorisation header, to authenticate the user making the request is_admin. This is enforced by the @auth_as_admin_decorator, which checks if the current user has admin privileges.  

- **Example JWT Token**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNzU3NDE4NiwianRpIjoiMmUyYzZjYWYtMTM1Yi00ZmFkLWFmMGYtZTVmNDVmNjUzNDJhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE3Mjc1NzQxODYsImNzcmYiOiIzMTIxYmQzZS1lZDYzLTQ2NDQtOTYyMS05NmY4MjA5ZDQ1ZGYiLCJleHAiOjE3Mjc2NjA1ODZ9.e6uOPoV1OluxBJmEOjSePp4xLvD1Iq6eIbQo1kp7zVY`  

### 4. Response

- **Success Response**: If the request is authorised and the user is an admin, (HTTP Status Code: 200 OK), the API will return:

![Admin Get All Users](docs/admin_getallusers.png)

- **Error Response**: If the user making the request does not have permission to make the update, that is, the user making the request does not have admin privileges, they will be denied access to this endpoint (HTTP Status Code: 403 Forbidden), the API will return:

![Non-Admin Trys to Get all Users](docs/notadmin_getallusers.png)


## `controllers/recipe_controller.py`

### GET ALL RECIPES IN THE DATABASE 
The `/recipes` endpoint allows users to fetch all recipes along with their associated ingredients using the GET method. It queries the database for all records in the Recipe table and returns them in a JSON format. The endpoint responds with a 200 OK status and a list of recipes.

## 1. HTTP Verb

- **GET**: This method is used to retrieve a list of all the recipes along with their associated ingredients, that currently exist in the database. User's do not need to be logged in or authenticated to browse the meal planner databases recipes.

### 2. Path or Route

- **Path**: `/recipes`

### 3. Required Body Data or Header Data

There is no body data or header data (authorisation) required to make this request.

### 4. Response

- **Success Response**: If recipes are successfully retrieved from the database,
 (HTTP Status Code: 200 OK), the API will return:

![Get All Recipes](docs/getallrecipes.png)

### GET ONE SPECIFIC RECIPE  
The `/recipes/<int:recipe_id>` endpoint allows clients to fetch the details of a specific recipe using the GET method. It queries the database for the recipe with the provided recipe_id integer and returns it in a JSON format. If the recipe is found, the server responds with a 200 OK status and the recipe details. If the recipe is not found, the server returns a 404 Not Found status with an appropriate error message.

## 1. HTTP Verb

- **GET**: This method is used to retrieve a specific recipe along with its associated ingredients using the recipe_id (if it exists). User's do not need to be logged in or authenticated to browse a specific recipe in the meal planner database.

### 2. Path or Route

- **Path**: `/recipes/<int:recipe_id>` (Note; `<int:recipe_id>` is a placeholder for the recipe_id, eg; the int: 3)

### 3. Required Body Data or Header Data

There is no body data or header data (authorisation) required to make this request.

### 4. Response

- **Success Response**: If the specific recipe exists, and is successfully retrieved from the database,
 (HTTP Status Code: 200 OK), the API will return:

![Get One Recipes](docs/getonerecipe.png)

- **Error Response**: If the recipe with the specified recipe_id does not exist or can not be found in the meal planner  database (HTTP Status Code: 404 Not Found), the API will return:

![Can't find Recipe](docs/recipe_notfound.png)  

### CREATE A RECIPE  
The `/recipes` endpoint allows authenticated users to create a new recipe using the POST method. The request must include a valid JWT token and JSON data with the recipe details. The recipe is then associated with the user who created it, and any new ingredients that are not already in the database are added. Upon successful creation of a new recipe, the API returns the recipe details with a 201 Created status. If there are any validation issues, the API responds with an appropriate error message.

## 1. HTTP Verb

- **POST**: This method is used to create a new recipe in the database. The request must include a valid JWT token in the Authorisation header. This token is used to authenticate the user, and associate the user with the recipe created.

### 2. Path or Route

- **Path**: `/recipes`

### 3. Required Body Data or Header Data

The request being made, must include a valid JWT token in the Authorisation header. This token is used to authenticate the user, and associate the user with the recipe created. The request body must contain JSON data that includes the following fields:  
- **name**: The name of the recipe is required, and it must be valid (eg; At least 4 characters in length)
- **description**: A description of the recipe, that meets what is stored in VALID_DESCRIPTIONS, eg; "keto", Gluten Free" etc.
- **recipe_ingredients**: A list of ingredients associated with the recipe. Each ingredient object should contain:
    - **ingredient**: The name of the ingredient, and it must be valid (eg; At least 4 characters in length).
    - **amount**: The amount of the ingredient for the recipe, must be a valid number (float), and greater that 0.1
    - **unit**: The unit of measurement of the ingredient in the recipe, and it must be valid (eg; At least 1 character in length)

**Example JSON body**: Where a user would like to create a new recipe, named "Steak Bearnaise", that is described as "Low Carb, Keto, Gluten Free" to be added to the database:

```json
{
  {
    "name": "Steak Bearnaise",
    "description": "Low Carb, Keto, Gluten Free",
    "recipe_ingredients": [
        {
            "ingredient": { "name": "Fillet Steak" },
            "amount": 250,
            "unit": "grams"
        },
        {
            "ingredient": { "name": "Bearnaise Sauce" },
            "amount": "100",
            "unit": "mls"
        },
        {
            "ingredient": { "name": "Butter" },
            "amount": 20,
            "unit": "grams"
        },
        {
            "ingredient": { "name": "Organic Salad Mix" },
            "amount": "200",
            "unit": "grams"
        }
    ]
}
}
```

### 4. Response

- **Success Response**: If the user is authenticated, and the recipe is successfully created (HTTP Status Code: 200 OK), the API will return:

![Recipe Created Successfully](docs/recipe_created.png)

- **Error Response**: If there are any issues with the input data, such as any missing and required fields, in this example, the description is missing (HTTP Status Code: 400 Bad Request), the API will return:

![Recipe Missing Field](docs/recipe_missingfield.png)  


### UPDATE A RECIPE  
The `/recipes/<int:recipe_id>` endpoint allows authenticated users to update a specific recipe using the PUT or PATCH methods. The request must include a valid JWT token, and the user must be either the creator of the recipe or an admin. The endpoint supports updates to the recipe's name, description, and ingredients, including adding, updating, or deleting ingredients. The server responds with the updated recipe details if successful, or appropriate error messages if the recipe is not found, the user is unauthorised, or the request data is invalid.

## 1. HTTP Verb

- **PUT**: This method is used to update an entire recipe, a user must be authenticated and own the recipe, or be an admin.

- **PATCH**: This method is used to update specific parts of a recipe, for example, just an ingredient amount needs to be changed in a recipe. Again, a user must be authenticated and own the recipe, or be an admin.

### 2. Path or Route

- **Path**: `/recipes/<int:recipe_id>`  (Note; `<int:recipe_id>` is a placeholder for the recipe_id, eg; the int: 3)

### 3. Required Body Data or Header Data

The request being made, must include a valid JWT token in the Authorisation header. This token is used to authenticate the user, and associate the user with the recipe being updated. The request body must contain JSON data that includes the following fields, with some optional:  
- **name**: The new name for the recipe if the user would like to update it (optional)
- **description**: The new description for the recipe if the user would like to update it (optional)
- **recipe_ingredients**: The list of ingredients associated with the recipe the user would like to update/add/delete:
    - **ingredient**: The name of the ingredient is always needed to add, update or delete. (required)
    - **amount**: The amount of the ingredient for the recipe, if the user would like to update it (optional)
    - **unit**: The unit of measurement of the ingredient needed in the recipe, if the user would like to update it (optional)
    - **delete**: A boolean (true/false) indicating whether to remove the ingredient or not (optional)

**Example JSON body**: Where a user would like to update an existing recipe, named "Steak Bearnaise". The user would like to change the amount of the ingredient named  "Bearnaise Sauce" to 150 (vs 100), and delete the ingredient named: "Butter" (Note; the name and description of the recipe is not required in this request, however I left them there to create a better understanding of the request being made):

```json
{
  "name": "Steak Bearnaise",
  "description": "Low Carb, Keto, Gluten Free",
  "recipe_ingredients": [
    {
      "ingredient": { "name": "Fillet Steak" },
      "amount": 250,
      "unit": "grams"
    },
    {
      "ingredient": { "name": "Bearnaise Sauce" },
      "amount": 150,
      "unit": "mls"
    },
    {
      "ingredient": { "name": "Butter" },
      "delete": true
    },
    {
      "ingredient": { "name": "Organic Salad Mix" },
      "amount": 200,
      "unit": "grams"
    }
  ]
}
```

### 4. Response

- **Success Response**: If the user is authenticated, and the recipe is successfully updated (HTTP Status Code: 200 OK), the API will return:

![Recipe Updated Successfully](docs/update_recipesuccess.png)

- **Error Response**: If there are any issues with the input data, such as any missing and required fields or improperly formatted data in the request, in this example, the name of the ingredient that is to be updated is missing (HTTP Status Code: 400 Bad Request), the API will return:

![Recipe Update Missing Field](docs/update_recipebad.png)  

- **Error Response**: If the recipe with the specified recipe_id that is to be updated does not exist, or can not be found in the meal planner database (HTTP Status Code: 404 Not Found), the API will return:

![Can't find Recipe to be Updated](docs/update_recipenotfound.png)  

- **Error Response**: If the user making the request does not have permission to update the recipe, that is, they are not an admin, or the owner of the recipe (via JWT) (HTTP Status Code: 403 Forbidden), the API will return:

![Non-Admin Trys to Update Recipe that doesn't belong to them](docs/update_recipeforbidden.png)

### DELETING A RECIPE (By a user that is not admin) 
The `/recipes/<int:recipe_id>` endpoint allows authenticated users to delete a specific recipe using the DELETE method. The request must include a valid JWT token, and the user must be either the creator of the recipe or an admin. Predefined recipes can only be deleted by admins. If the deletion is successful, the server responds with a 200 OK status and a confirmation message. If the recipe is not found or the user is unauthorised to delete the recipe, the appropriate error messages are returned.

### 1. HTTP Verb

- **DELETE**: This endpoint uses the DELETE HTTP method to remove a specific recipe from the database. The user must own the recipe (unless they are an admin), be recently logged in, and authenticated via their JWT to perform this action.

### 2. Path or Route

- **Path**: `/recipes/<int:recipe_id>` (Note; `<int:recipe_id>` is a placeholder for the recipes recipe_id, eg; the int: 3)

### 3. Required Body Data or Header Data  

There is no body data required to make this request. However, the request must include a valid JWT token in the Authorisation header, to authenticate the user making the request is the owner of the recipe or is_admin:  

- **Example JWT Token**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNzU3NDE4NiwianRpIjoiMmUyYzZjYWYtMTM1Yi00ZmFkLWFmMGYtZTVmNDVmNjUzNDJhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE3Mjc1NzQxODYsImNzcmYiOiIzMTIxYmQzZS1lZDYzLTQ2NDQtOTYyMS05NmY4MjA5ZDQ1ZGYiLCJleHAiOjE3Mjc2NjA1ODZ9.e6uOPoV1OluxBJmEOjSePp4xLvD1Iq6eIbQo1kp7zVY`


### 4. Response

- **Success Response**: If the user owns the recipe or is_admin, and so successfully deletes the recipe, providing they have their valid JWT token entered correctly in the header (HTTP Status Code: 200 OK), the API will return:

![Successful Recipe Deletion](docs/delete_recipesuccess.png)

- **Error Response**: If the user making the request does not have permission to delete the recipe, that is; they are neither the owner nor an admin (HTTP Status Code: 403 Forbidden), the API will return:

![User Trys to Change Email](docs/delete_recipeforbidden.png)  

- **Error Response**: If the user making the request is trying to delete a predefined recipe, that is; they not an admin (HTTP Status Code: 403 Forbidden), the API will return:

![User Trys to Change Email](docs/delete_predefined.png) 

- **Error Response**: If the recipe with the specified recipe_id does not exist in the database, (HTTP Status Code: 404 Not Found), the API will return:

![User Trys to Change Admin Status](docs/delete_recipenotfound.png) 

### GET ALL VEGAN RECIPES IN THE DATABASE 
The `/recipes/vegan` endpoint allows clients to fetch all recipes that contain the word "Vegan" in their description using the GET method. The endpoint performs a case-insensitive search and returns a list of matching recipes in JSON format. Whether Vegan recipes are found or not, the server responds with a 200 OK status.

## 1. HTTP Verb

- **GET**: This method is used to retrieve a list of all recipes that contain the word "Vegan" in their description. User's do not need to be logged in or authenticated to browse the meal planner database for Vegan recipes.

### 2. Path or Route

- **Path**: `/recipes/vegan`

### 3. Required Body Data or Header Data

There is no body data or header data (authorisation) required to make this request.

### 4. Response

- **Success Response**: If any Vegan recipes are successfully retrieved from the database,
 (HTTP Status Code: 200 OK), the API will return:

![Get All Vegan Recipes](docs/getvegan_recipes.png)

- **Empty Response**: If no Vegan recipes are currently in the database,
 (HTTP Status Code: 200 OK), the API will return:

 ![No Vegan Recipes](docs/novegan_recipes.png)


### GET ALL KETO RECIPES IN THE DATABASE 
The `/recipes/keto` endpoint allows clients to fetch all recipes that contain the word "Keto" in their description using the GET method. The endpoint performs a case-insensitive search and returns a list of matching recipes in JSON format. Whether Keto recipes are found or not, the server responds with a 200 OK status.

## 1. HTTP Verb

- **GET**: This method is used to retrieve a list of all recipes that contain the word "Keto" in their description. User's do not need to be logged in or authenticated to browse the meal planner database for Keto recipes.

### 2. Path or Route

- **Path**: `/recipes/keto`

### 3. Required Body Data or Header Data

There is no body data or header data (authorisation) required to make this request.

### 4. Response

- **Success Response**: If any Keto recipes are successfully retrieved from the database,
 (HTTP Status Code: 200 OK), the API will return:

![Get All Keto Recipes](docs/getketo_recipes.png)

- **Empty Response**: If no Keto recipes are currently in the database,
 (HTTP Status Code: 200 OK), the API will return:

 ![No Keto Recipes](docs/noketo_recipes.png)

 ### GET ALL GLUTEN FREE RECIPES IN THE DATABASE 
The `/recipes/gluten-free` endpoint allows clients to fetch all recipes that contain the word "Gluten Free" in their description using the GET method. The endpoint performs a case-insensitive search and returns a list of matching recipes in JSON format. Whether Gluten Free recipes are found or not, the server responds with a 200 OK status.

## 1. HTTP Verb

- **GET**: This method is used to retrieve a list of all recipes that contain the words "Gluten Free" in their description. User's do not need to be logged in or authenticated to browse the meal planner database for Gluten Free recipes.

### 2. Path or Route

- **Path**: `/recipes/gluten-free`

### 3. Required Body Data or Header Data

There is no body data or header data (authorisation) required to make this request.

### 4. Response

- **Success Response**: If any Gluten Free recipes are successfully retrieved from the database,
 (HTTP Status Code: 200 OK), the API will return:

![Get All Vegan Recipes](docs/getglutenfree_recipes.png)

- **Empty Response**: If no Gluten Free recipes are currently in the database,
 (HTTP Status Code: 200 OK), the API will return:

 ![No Vegan Recipes](docs/noglutenfree_recipes.png)

 ## `controllers/user_recipe_controller.py`

 ### ADD A RECIPE TO A USERS LIST
The `/user-recipes` endpoint allows authenticated users to add a recipe to their personal recipe list using the POST method. The request must include a valid JWT token and the recipe_id of the recipe they wish to add. The database checks if the recipe exists and whether it is already in the user's list to avoid any duplicate recipe entries. Upon successful addition, the server responds with a 201 Created status and a confirmation message. If the recipe is not found, or if it's already in the user's list, appropriate error messages are returned.

## 1. HTTP Verb

- **POST**: This method is used to add a recipe to a user's personal recipe list (user_recipes). The request must include a valid JWT token in the Authorisation header. This token is used to authenticate the user, and associate the user with the recipe added to their personal list.

### 2. Path or Route

- **Path**: `/user-recipes`

### 3. Required Body Data or Header Data

The request being made, must include a valid JWT token in the Authorisation header, which identifies the user to add a recipe to their associated list. The request body must contain JSON data that includes the following field:  
- **recipe_id**: The recipe_id (eg; 1) of the recipe that the user wants to add to their personal list.

**Example JSON body**: Where a user would like to add the recipe with the recipe_id of 1 to their personal list (user_recipes):

```json
{
  "recipe_id": 1
}
```

### 4. Response

- **Success Response**:  If the recipe is successfully added to the user's personal list (HTTP Status Code: 200 OK), the API will return:

![User Recipe Successfully Added to List](docs/userrecipe_added.png)

- **Error Response**: If there are any issues with the input data, such as a missing and required field, in this example, the recipe_id is not provided in the request body (HTTP Status Code: 400 Bad Request), the API will return:

![Recipe Missing Field](docs/userrecipe_bad.png) 

- **Error Response**: If the recipe with the specified recipe_id does not exist in the database, (HTTP Status Code: 404 Not Found), the API will return:

![User Trys to Change Admin Status](docs/userrecipe_notfound.png) 

- **Error Response**: If the recipe with the specified recipe_id already exists in the users personal list, (HTTP Status Code: 409 Conflict), the API will return:

![User Trys to Change Admin Status](docs/userrecipe_conflict.png) 

### GET ALL RECIPES IN A USERS PERSONAL LIST  
The `/user-recipes` endpoint allows authenticated users to retrieve the names of all recipes they have saved in their personal recipe/shopping list using the GET method. The request must include a valid JWT token. If the user has recipes in their list, the server responds with a list of recipe names in JSON format. If the user has no recipes, a message is returned indicating the list is empty. The server responds with a 200 OK status in both cases.

## 1. HTTP Verb

- **GET**: This method is used to retrieve all recipes (by name) that a user has saved in their personal recipe/shopping list (user_recipes). A user needs to be logged in and authenticated (JWT) to view heir personal recipe list. 

### 2. Path or Route

- **Path**: `/user-recipes`

### 3. Required Body Data or Header Data

There is no body data required to make this request. However, the request must include a valid JWT token in the Authorisation header. This token is used to authenticate and identify the user making the request.

### 4. Response

- **Success Response**: If the user has recipes saved in their personal list, (HTTP Status Code: 200 OK), the API will return:

![User Recipes List By Name](docs/userrecipes_list.png)

- **Empty Response**: If the user has no recipes in their personal list (HTTP Status Code: 200 OK), the API will return:

![No Users Recipes In List](docs/userrecipes_none.png)

### GET A USERS SHOPPING LIST (Ingredients for recipes saved)  
The `/user-recipes/shopping-list` endpoint allows authenticated users to generate a shopping list by retrieving all the ingredients from the recipes saved in their personal recipe list using the GET method. The request must include a valid JWT token. The system fetches the user's recipes, compiles the ingredients, and returns them in a list. If the user has no saved recipes, the server returns a message indicating the list is empty. The server responds with a 200 OK status in both cases.

## 1. HTTP Verb

- **GET**: This method is used to create a shopping list by retrieving all ingredients from the recipes saved in a user's personal recipe list. A user needs to be logged in or authenticated (JWT) to retrieve this list. 

### 2. Path or Route

- **Path**: `/user-recipes/shopping-list`

### 3. Required Body Data or Header Data

There is no body data required to make this request. However, the request must include a valid JWT token in the Authorisation header. This token is used to authenticate and identify the user making the request.

### 4. Response

- **Success Response**: If the user has recipes saved in their personal list, (HTTP Status Code: 200 OK), the API will return:

![User Recipes Shopping List](docs/userrecipes_shop.png)

- **Empty Response**: If the user has no recipes in their personal list (HTTP Status Code: 200 OK), the API will return:

![No Users Recipes In For Shopping List](docs/userrecipes_shopnone.png)

### DELETING A RECIPE IN A USERS LIST
The `/user-recipes/<int:recipe_id>` endpoint allows authenticated users to delete a specific recipe from their personal recipe list using the DELETE method. The request must include a valid JWT token. The system checks whether the recipe exists in the user's list, and if found, it is deleted. If the recipe is not found, an error message is returned. The server responds with a 200 OK status upon successful deletion or a 404 Not Found error if the recipe is not in the user's list.

### 1. HTTP Verb

- **DELETE**: This method is used to delete a specific recipe from a user's personal recipe/shopping list (user recipes).

### 2. Path or Route

- **Path**: `/user-recipes/<int:recipe_id>` (Note; `<int:recipe_id>` is a placeholder for the recipe's recipe_id, eg; the int: 3)

### 3. Required Body Data or Header Data  

There is no body data required to make this request. However, the request must include a valid JWT token in the Authorisation header, to authenticate, and identify the user making the request.

- **Example JWT Token**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNzU3NDE4NiwianRpIjoiMmUyYzZjYWYtMTM1Yi00ZmFkLWFmMGYtZTVmNDVmNjUzNDJhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE3Mjc1NzQxODYsImNzcmYiOiIzMTIxYmQzZS1lZDYzLTQ2NDQtOTYyMS05NmY4MjA5ZDQ1ZGYiLCJleHAiOjE3Mjc2NjA1ODZ9.e6uOPoV1OluxBJmEOjSePp4xLvD1Iq6eIbQo1kp7zVY`


### 4. Response

- **Success Response**: If the recipe is successfully deleted from the user's list (HTTP Status Code: 200 OK), the API will return:

![Successful User Recipe Deletion](docs/userrecipes_deletesuccess.png)

- **Error Response**: If the recipe with the specified recipe_id is not found in the user's list (HTTP Status Code: 404 Not Found), the API will return:

![User Trys to Delete a Recipe That is Not Found](docs/userrecipes_deletenotfound.png) 

