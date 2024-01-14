from src.database import db
from src.server import server
from src.endpoints.menu.get_menu import get_menu
from src.models.menu import Menu

def test_menu_found():
    db.init_app(server)
    with server.app_context():
        menu = Menu(1, "test menu")
        db.session.add(menu)

        result = get_menu(1)
        assert result["id"] == menu.id
        assert result["name"] == menu.name
        assert result["menu_items"] == []

        db.session.delete(menu)


def test_menu_not_found():
    with server.app_context():
        assert get_menu(0) == None
