from flask import render_template

from app.main import bp
from app.models.category import Category
from app.models.question import Question


@bp.route('/')
def index():
    categories = Category.query.all()
    return render_template('index.html', categories=categories)
