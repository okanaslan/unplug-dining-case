from flask_sqlalchemy import SQLAlchemy
from server import app

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://prisma:prisma@localhost:5432/postgres"

db = SQLAlchemy(app)

# Models
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(50), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False)
    password = db.Column(db.VARCHAR(50), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.name

    def serialize(self):
        return {"id": self.id, "name": self.name, "email": self.email}
