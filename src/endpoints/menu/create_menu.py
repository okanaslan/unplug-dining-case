from flask import request, jsonify
from database import db
from models.menu import Menu


def create_menu_handler(restaurant_id):
    # Get the request body data
    data = request.get_json()

    # Create a new menu
    menu = Menu(restaurant_id)

    # Add the menu to the database
    db.session.add(menu)
    db.session.commit()

    # Return a 201 response with the menu
    return jsonify(menu.serialize()), 201
