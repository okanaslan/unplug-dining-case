import datetime
from database import db

class Menu(db.Model):
    __tablename__ = "menus"
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, restaurant_id):
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return "<Menu %r>" % self.id

    def serialize(self):
        return {"id": self.id, "restaurant_id": self.restaurant_id}
