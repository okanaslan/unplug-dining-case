import datetime
from database import db
from sqlalchemy.orm import Mapped


class MenuItem(db.Model):
    __tablename__ = "menu_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    description = db.Column(db.VARCHAR(2550), nullable=True)
    stock_status = db.Column(db.VARCHAR(255), nullable=False)
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
    menu: Mapped["Menu"] = db.relationship(back_populates="menu_items")


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
        menu_id=None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.stock_status = stock_status
        self.image = image
        self.ranking = ranking
        self.price = price
        self.calorie = calorie
        self.menu_id = menu_id

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
