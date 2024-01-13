from src.database import db
from src.server import server
from src.endpoints.menu_item.update_menu_item import update_menu_item


def test_answer():
    with server.app_context():
        data = {
            "price": 0,
        }
        assert update_menu_item(0, data) == None
