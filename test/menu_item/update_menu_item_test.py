from src.database import db
from src.server import server
from src.endpoints.menu_item.update_menu_item import update_menu_item
from src.models.menu_item import MenuItem

def test_menu_item_updated():
    with server.app_context():
        menuItem = MenuItem(3, "test menu item", "IN_STOCK", "test image", 0, "test description", 0)
        db.session.add(menuItem)

        data = {
            "price": 10,
        }
        result = update_menu_item(menuItem.id, data)
        assert result["id"] == menuItem.id
        assert result["price"] == data["price"]


        db.session.delete(menuItem)
        db.session.commit()


def test_menu_item_not_found():
    with server.app_context():
        data = {
            "price": 0,
        }
        assert update_menu_item(0, data) == None
