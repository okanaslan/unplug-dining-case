from flask import request, jsonify
from database import db
from models.menu_item import MenuItem


def update_menu_item_handler(menu_item_id):
    data = request.get_json()

    menu_item = MenuItem.query.filter_by(id=menu_item_id).first()
    if not menu_item:
        return jsonify({"error": "Menu item not found"}), 404

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

    return jsonify(menu_item.serialize()), 200
