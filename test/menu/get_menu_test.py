from src.database import db
from src.server import server
from src.endpoints.menu.get_menu import get_menu


def test_answer():
    db.init_app(server)
    with server.app_context():
        assert get_menu(0) == None
