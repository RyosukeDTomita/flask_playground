from app.database import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, comment="Unique identifier for the user")
    username = db.Column(db.String(10), nullable=False, comment="Username of the user")