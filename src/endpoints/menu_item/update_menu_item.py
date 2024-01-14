from src.database import db
from src.models.menu_item import MenuItem


def update_menu_item(menu_item_id, data):
    menu_item = MenuItem.query.filter_by(id=menu_item_id).first()
    if not menu_item:
        return None

    if "name" in data:
        menu_item.name = data["name"]
    if "stock_status" in data:
        menu_item.stock_status = data["stock_status"]
    if "image" in data:
        menu_item.image = data["image"]
    if "price" in data:
        menu_item.price = data["price"]
    if "description" in data:
        menu_item.description = data["description"]
    if "ranking" in data:
        menu_item.ranking = data["ranking"]
    if "calorie" in data:
        menu_item.calorie = data["calorie"]

    db.session.commit()

    return menu_item.serialize()
