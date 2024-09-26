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

### 2. Initial Meal Planner API Setup Trello Card

![My Trello Board](docs/trello_initial.png)

### 3. User Account Feature Trello Card

![My Trello Board](docs/trello_user.png)

### 4. Recipe Management Feature Trello Card

![My Trello Board](docs/trello_recipe.png)

### 5. User Recipe Management Feature Trello Card

![My Trello Board](docs/trello_userrecipe.png)

### 6. Recipe-Ingredient Model and Schema Trello Card

![My Trello Board](docs/trello_recipeingredient.png)

### 7. Ingredient Model and Schema Trello Card

![My Trello Board](docs/trello_ingredient.png)

### 8. CLI Controller Trello Card

![My Trello Board](docs/trello_cli.png)

### 9. Design ERD Diagram For API Trello Card

![My Trello Board](docs/trello_erd.png)

### 10. Marshmallow Validation and Global Error Handling Trello Card

![My Trello Board](docs/trello_marshmallow.png)

**References:** 

1. [My Trello Board](https://trello.com/b/zpkuS1jz/api-webserver)
2. [4 Kanban Principles for Agile Project Management](https://www.atlassian.com/agile/project-management/kanban-principles)
3. [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)


## R3. List and explain the third-party services, packages and dependencies used in this app.

## R4. Explain the benefits and drawbacks of this app’s underlying database system.

## R5. Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

## R6. Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. <br><br>This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

## R7. Explain the implemented models and their relationships, including how the relationships aid the database implementation. <br><br>Explain the implemented models and their relationships, including how the relationships aid the database implementation.

## R8. Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:
- ## HTTP verb
- ## Path or route
- ## Any required body or header
- ## Response