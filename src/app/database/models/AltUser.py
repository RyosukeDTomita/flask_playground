from app.database import db

class AltUser(db.Model):
    """_summary_
    複数のデータベースを切り替えて使用できるかの検証用
    """
    __bind_key__ = "mydatabase_alt"
    __tablename__ = "alt_user"
    id = db.Column(db.Integer, primary_key=True, comment="Unique identifier for the user")
    username = db.Column(db.String(10), nullable=False, comment="Username of the user")
