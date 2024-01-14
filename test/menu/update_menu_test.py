from src.database import db
from src.server import server
from src.endpoints.menu.update_menu import update_menu
from src.models.menu import Menu
from src.models.menu_item import MenuItem


def test_menu_updated():
    with server.app_context():
        menu = Menu(1, "test menu")
        db.session.add(menu)

        menuItem = MenuItem(1, "test menu item", "IN_STOCK", "test image", 0, "test description", 0)
        db.session.add(menuItem)

        data = {
            "operation": "add",
            "menuItemId": menuItem.id
        }
        result, status_code = update_menu(1, data)
        assert status_code == 201
        assert result["id"] == menu.id
        assert result["menu_items"][0]["id"] == menuItem.id

        db.session.delete(menu)
        db.session.delete(menuItem)
        db.session.commit()


def test_invalid_operation():
    with server.app_context():
        menu = Menu(2, "test menu")
        db.session.add(menu)

        menuItem = MenuItem(2, "test menu item", "IN_STOCK", "test image", 0, "test description", 0)
        db.session.add(menuItem)

        data = {
            "operation": "delete",
            "menuItemId": menuItem.id
        }        
        assert update_menu(menu.id, data) == (None, 400)

        db.session.delete(menu)
        db.session.delete(menuItem)
        db.session.commit()


def test_menu_not_found():
    with server.app_context():
        data = {
            "operation": "add",
            "menuItemId": 0
        }
        assert update_menu(0, data) == (None, 404)
