import datetime
from database import db
from sqlalchemy.orm import Mapped
from typing import List


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
    menu_items: Mapped[List["MenuItem"]] = db.relationship(back_populates="menu", lazy=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.menu_items = []

    def __repr__(self):
        return "<Menu %r>" % self.id

    def serialize(self):
        return {"id": self.id, "name": self.name, "menu_items": [menu_item.serialize() for menu_item in self.menu_items]}

    def save(self):
        db.session.add(self)
        db.session.commit()
