from flask import request, jsonify
from database import db
from models.menu import Menu


def update_menu_handler(id):
    data = request.get_json()
    operation = data["operation"]
    menuItemId = data["menuItemId"]

    menu = Menu.query.filter_by(id=id).first()
    if not menu:
        return jsonify({"error": "Menu not found"}), 404

    if operation == "add":
        menu.add_menu_item(menuItemId)
    elif operation == "remove":
        menu.remove_menu_item(menuItemId)
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify(menu.serialize()), 201
