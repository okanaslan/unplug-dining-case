import datetime
from database import db


class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    menu_items = db.relationship("MenuItem", backref="menu", lazy=True)



    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu_items = []

    def __repr__(self):
        return "<Menu %r>" % self.id

    def serialize(self):
        return {"id": self.id, "restaurant_id": self.restaurant_id}

    def save(self):
        db.session.add(self)
        db.session.commit()
