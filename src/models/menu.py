import datetime
from typing import List
from sqlalchemy.orm import Mapped
from src.database import db
from src.models.menu_item import MenuItem


class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    menu_items: Mapped[List["MenuItem"]] = db.relationship(
        back_populates="menu", lazy=True
    )

    def __init__(self, id, name, menu_items=[]):
        self.id = id
        self.name = name
        self.menu_items = menu_items

    def __repr__(self):
        return "<Menu %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "menu_items": [menu_item.serialize() for menu_item in self.menu_items],
        }

    def add_menu_item(self, menu_item_id):
        menu_item = MenuItem.query.filter_by(id=menu_item_id).first()
        if not menu_item:
            return None
        self.menu_items.append(menu_item)
        db.session.commit()

    def remove_menu_item(self, menu_item_id):
        menu_item = MenuItem.query.filter_by(id=menu_item_id).first()
        if not menu_item:
            return None
        if menu_item not in self.menu_items:
            return None
        self.menu_items.remove(menu_item)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
