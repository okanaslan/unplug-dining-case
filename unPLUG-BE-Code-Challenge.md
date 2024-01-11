# BE Code Challenge

## The Application

Build an API that allows a user to request and update a restaurant's menu data. This application should be documented and able to run on any Linux computer.

### API Endpoints

The application publishes an API with three endpoints that return a restaurant's menu, add new menu items, and remove menu items.

- The API must respond to requests on port `5000`.
- The API must respond using JSON.

#### 1. Menu

- GET Endpoint: `/menu/{restaurant_id}`.
  - Returns the latest menu object for a given restaurant ID.
  - The initial menu object should be loaded into a database on application start.

- POST Endpoint: `/menu/{restaurant_id}`.
  - Takes a payload to add or remove menu items.
  - Overwrites the initial menu object and persists across sessions.

#### 2. Menu Item

- POST Endpoint: `/menu-item/{menu_item_id}`.
  - Takes a menu item ID and a JSON payload to update the values of a menu item.

### Application Startup

If the database is empty when the application is run, the initial menu data provided should be automatically loaded into the database. Data should persist when the application is stopped and restarted.
The initial menu data can be found in the provided JSON file `sample_data.json`. The format of this file is a similar JSON structure that can be submitted to the menu endpoint.


### Other Requirements

- There must be documentation that one can follow to run the application.
- API endpoints must be clearly documented.
- Tests need to be in place.
- The application must be written in Python.

### Submitting

Zip up your submission and submit it via email to `alibolak@unplugdining.com`.

### Sample JSON for Testing

The full JSON will be submitted to the candidate as a separate file.
```
{
    "menu_group_map": {
        "21566": {
            "id": 21566,
            "name": "Starters",
            "sort_order": 1
        },
    },
    "menu_item_map": {
        "148185": {
            "id": 148185,
            "name": "Lunatic Sampler",
            "description": "Falafel, stuffed grape leaves, couscous medley, organic hummus (original or spicy harissa), pita bread.",
            "stock_status": "IN_STOCK",
            "restaurant_id": null,
            "image": "temp/1-2023071204PM32.JPEG",
            "ranking": 44,
            "price": 13.99,
            "calorie": null
        },
    },
    "menu_group_menu_item_lookup": {
        "21566": [
            148185,
            148144,
            148372,
            148145,
            148149,
            148160,
            148150,
            148383,
            148157,
            148411
        ]
    }
}
```
### Assessment

Members of our backend team will ensure your code meets the functional criteria and score the submission based on project design, language/framework best practices, code cleanliness and organization, ease of use, packaging, documentation, and testing practices.
