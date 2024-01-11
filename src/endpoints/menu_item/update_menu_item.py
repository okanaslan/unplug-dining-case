from flask import request, jsonify
from server import app
from database import db
from models.menu_item import MenuItem


# POST Endpoint: /menu-item/{menu_item_id}
@app.route("/menu-item/<int:menu_item_id>", methods=["POST"])
def update_menu_item(menu_item_id):
    # Get the request body data
    data = request.get_json()

    # Get the menu item from the database
    menu_item = MenuItem.query.filter_by(id=menu_item_id).first()

    # If the menu item doesn't exist, return a 404 error
    if not menu_item:
        return jsonify({"error": "Menu item not found"}), 404

    # Update the menu item
    menu_item.name = data["name"]
    menu_item.description = data["description"]
    menu_item.price = data["price"]

    # Commit the changes to the database
    db.session.commit()

    # Return a 200 response with the updated menu item
    return jsonify(menu_item.serialize()), 200
    