from app.extensions import db


class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    questions = db.relationship(
        "Question", secondary="template_question", backref=db.backref("templates", lazy="dynamic"))

    def __repr__(self):
        return f"<Template {self.name}>"


template_question = db.Table(
    "template_question",
    db.Column("template_id", db.Integer, db.ForeignKey(
        "template.id"), primary_key=True),
    db.Column("question_id", db.String, db.ForeignKey(
        "question.id"), primary_key=True),
)
