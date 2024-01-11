from flask import jsonify
from server import app
from models.menu import Menu


# GET Endpoint: /menu/{restaurant_id}
@app.route("/menu/<int:restaurant_id>")
def get_menu(restaurant_id):
    # Get the menu from the database
    menu = Menu.query.filter_by(restaurant_id=restaurant_id).first()

    # If the menu doesn't exist, return a 404 error
    if not menu:
        return jsonify({"error": "Menu not found"}), 404

    # Return a 200 response with the menu
    return jsonify(menu.serialize()), 200