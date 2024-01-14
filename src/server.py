from flask import Flask, jsonify, request
import os

from src.endpoints.menu.update_menu import update_menu
from src.endpoints.menu.get_menu import get_menu
from src.endpoints.menu_item.update_menu_item import update_menu_item

server = Flask(__name__)

server.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://prisma:prisma@localhost:5432/unplugdining"
server.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


# register endpoints
@server.route("/menu/<int:id>")
def get_menu_handler(id):
    menu = get_menu(id)
    if not menu:
        return jsonify({"error": "Menu not found"}), 404

    return jsonify(menu), 200


@server.route("/menu/<int:id>", methods=["POST"])
def update_menu_handler(id):
    data = request.get_json()
    menu, status_code = update_menu(id, data)
    if not menu:
        return jsonify({"error": "Menu not found"}), status_code

    return jsonify(menu), 200


@server.route("/menu-item/<int:id>", methods=["POST"])
def update_menu_item_handler(id):
    data = request.get_json()

    menu_item = update_menu_item(id, data)
    if not menu_item:
        return jsonify({"error": "Menu item not found"}), 404

    return jsonify(menu_item), 200
