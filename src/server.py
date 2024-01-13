from flask import Flask
import os

from endpoints.menu.create_menu import create_menu_handler
from endpoints.menu.get_menu import get_menu_handler
from endpoints.menu_item.update_menu_item import update_menu_item_handler

server = Flask(__name__)

server.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://prisma:prisma@localhost:5432/unplugdining"
server.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


# register endpoints
@server.route("/menu/<int:id>", methods=["POST"])
def create_menu(id):
    return create_menu_handler(id)


@server.route("/menu/<int:id>")
def get_menu(id):
    return get_menu_handler(id)


@server.route("/menu-item/<int:id>", methods=["POST"])
def update_menu_item(id):
    return update_menu_item_handler(id)
