from flask import jsonify
from models.menu import Menu
from sqlalchemy.orm import joinedload


def get_menu_handler(id):
    # get menu and join menu_items
    menu = Menu.query.filter_by(id=id).options(joinedload(Menu.menu_items)).first()


    if not menu:
        return jsonify({"error": "Menu not found"}), 404

    # Return a 200 response with the menu
    return jsonify(menu.serialize()), 200
