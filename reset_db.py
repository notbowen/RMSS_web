from app.extensions import db
from app.models.category import Category

from app import create_app

with create_app().app_context():
    db.drop_all()
    db.create_all()

    pom = Category(level="Secondary 4", subject="Physics", topic="Principle of Moments")
    emi = Category(level="Secondary 4", subject="Physics", topic="Electromagnetic Induction")
    vec = Category(level="Secondary 4", subject="E Maths", topic="Vectors")

    db.session.add(pom)
    db.session.add(emi)
    db.session.add(vec)

    db.session.commit()
