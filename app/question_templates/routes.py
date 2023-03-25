from flask import render_template

from app.question_templates import bp

@bp.route("/", methods=["GET"])
def index():
    return render_template("question_templates.html")