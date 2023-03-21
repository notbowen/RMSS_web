from flask import render_template

from app.topics import bp
from app.models.category import Category

@bp.route("/edit")
def edit_topics():
    categories = Category.query.all()
    return render_template("edit_topics.html", categories=categories)