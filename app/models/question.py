from app.extensions import db


class Question(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    section = db.Column(db.String(1), nullable=False)
    content = db.Column(db.JSON, nullable=False)
    answer = db.Column(db.JSON, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref=db.backref("questions", lazy=True))

    def __repr__(self):
        return f"<Question {self.id}>"
