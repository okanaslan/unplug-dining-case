import datetime
from database import db


class Menu(db.Model):
    __tablename__ = "menus"
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name

    def __repr__(self):
        return "<Menu %r>" % self.id

    def serialize(self):
        return {"id": self.id, "restaurant_id": self.restaurant_id}

    def save(self):
        db.session.add(self)
        db.session.commit()
