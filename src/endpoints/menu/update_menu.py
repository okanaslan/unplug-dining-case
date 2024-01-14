from flask import request
from src.database import db
from src.models.menu import Menu


def update_menu(id, data):
    operation = data["operation"]
    menuItemId = data["menuItemId"]

    menu = Menu.query.filter_by(id=id).first()
    if not menu:
        return None, 404

    if operation == "add":
        menu.add_menu_item(menuItemId)
    elif operation == "remove":
        menu.remove_menu_item(menuItemId)
    else:
        return None, 400

    return menu.serialize(), 201
