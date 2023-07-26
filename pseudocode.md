# MVP #
    The app should be able to perform READ ONLY operations on the Restaurant models as well as have routes to display information as JSON.

# MoSCoW #
    Must have:
        Store the following data in your PostgreSQL database and implement models for READ only operations for the following data: Menu Items, Title, Description, Price, Spicy Level, FK to Category, FK to Cuisine. Category (Appetizer, Dessert, Main Dish, etc.). Cuisine (American, Thai, etc.)

        Create views to send JSON data back to a GET request for a list of all menu items with the category and cuisine labels nested in the data.

        Create routes to use the views created in the previous step.

        Change the URL in the React Restaurant Code to the Gitpod url of your running backend code only. (NOTE: We shouldn’t be writing any React code for basic requirements)

    Should have:
        The owners of the restaurant opened up a new location and the menus are different. Create a way for the database to handle this situation (new model with a new relationship)

        Create a ManyToMany relationship on the menu items to an ingredients table and get those items to populate in the API elegantly with your existing endpoint

    Could have:
        Use class based views or decorators in Django to protect routes

        Handle exceptions with error messaging on front end and/or back end.

        Generate a csv export of the data in the database with a new route containing all the required information

    Won't have:
        Override the save, pre_save, or post_save methods in your models use a free API to grab an image that saves as a url in your database. Pixabay has a decent API you could interact with from the Django backend if you wanted to try to accomplish that. 
        Overriding model methods - Docs

        Create user groups to assign the restaurant owners a subset of abilities when they login to update data in the Django Administration. Enable the registration page for Django Admin.

        Add a custom field(s) to the API that improves the functionality of the restaurant front end

# Flow chart #

![backend bistro flowchar](/img/backend_bistro_flowchart.png)

# Notes / Questions #

    Slugs are the last part of the URL

    models.py is where the tables and relationships between the tables are created

    views.py these are "actions". This is where you use Python to pull information from the database

    The end point (slug) should direct the app where to route the request
    It does this at the top layer in the backend_bistro urls.py then after removing the matched pieces of the url goes to the appropriate app (menu_item, etc...)

# End points #

    /american-food - displays list of american foods - hamburger, hot dog, cheese fries
    /mexican-food - burrito, tacos, pupusas
    /asian-food - displays list of asian foods - habachi chicken, sake, sashimi, nigiri