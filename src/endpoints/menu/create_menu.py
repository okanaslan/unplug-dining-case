from flask import request, jsonify
from server import app
# from db import db
from models.menu import Menu


# POST Endpoint: /menu/{restaurant_id}
@app.route("/menu/<int:restaurant_id>", methods=["POST"])
def create_menu(restaurant_id):
    # Get the request body data
    data = request.get_json()

    # Create a new menu
    menu = Menu(restaurant_id)

    # Add the menu to the database
    # db.session.add(menu)
    # db.session.commit()

    # Return a 201 response with the menu
    return jsonify(menu.serialize()), 201