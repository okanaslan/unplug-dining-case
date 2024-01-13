import datetime
from database import db


class MenuItem(db.Model):
    __tablename__ = "menu_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    description = db.Column(db.VARCHAR(2550), nullable=True)
    stock_status = db.Column(db.VARCHAR(255), nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=True)
    image = db.Column(db.VARCHAR(255), nullable=False)
    ranking = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Float, nullable=False)
    calorie = db.Column(db.Integer, nullable=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    menu_id = db.Column(db.Integer, db.ForeignKey("menu.id"), nullable=True)

    def __init__(
        self,
        id,
        name,
        stock_status,
        image,
        price,
        description=None,
        ranking=None,
        calorie=None,
        restaurant_id=None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.stock_status = stock_status
        self.restaurant_id = restaurant_id
        self.image = image
        self.ranking = ranking
        self.price = price
        self.calorie = calorie

    def __repr__(self):
        return "<MenuItem %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
