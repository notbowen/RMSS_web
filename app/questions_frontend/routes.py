from flask import request, render_template

from app.questions_frontend import bp
from app.models.question import Question
from app.models.category import Category

@bp.route("/search")
def search_question():
    categories = Category.query.all()

    # Return search page if no query string is provided
    if len(request.args) == 0:
        return render_template("search_question.html", categories=categories)

    section = request.args.get("section", None, type=str)
    category = request.args.get("category", None, type=int)

    # Get all questions
    questions = Question.query.all()

    # Filter by section if section is not None
    if section != None:
        questions = [q for q in questions if q.section == section]
    
    # Filter by level if level is not None
    if category != None:
        questions = [q for q in questions if q.category_id == category]

    return render_template("list_questions.html", categories=categories, questions=questions)

@bp.route("/all")
def get_all_questions():
    questions = Question.query.all()
    return render_template("list_questions.html", questions=questions)
