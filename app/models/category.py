from app.extensions import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"
