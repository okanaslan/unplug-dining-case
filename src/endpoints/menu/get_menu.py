from sqlalchemy.orm import joinedload
from src.models.menu import Menu


def get_menu(id):
    menu = Menu.query.filter_by(id=id).options(joinedload(Menu.menu_items)).first()
    if not menu:
        return None
    return menu.serialize()
