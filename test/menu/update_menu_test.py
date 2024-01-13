from src.database import db
from src.server import server
from src.endpoints.menu.update_menu import update_menu


def test_answer():
    with server.app_context():
        data = {
            "operation": "add",
            "menuItemId": 0
        }
        assert update_menu(0, data) == (None, 404)
