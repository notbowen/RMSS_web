from flask import request, render_template, redirect, url_for

from app.questions_frontend import bp
from app.models.question import Question
from app.models.category import Category

@bp.route("/search")
def search_question():
    categories = Category.query.all()

    # Return search page if no query string is provided
    if len(request.args) == 0:
        return render_template("search_question.html", categories=categories)

    # Get query string parameters
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

@bp.route("/edit", methods=["GET"])
def edit_question():
    id = request.args.get("id", None, type=str)

    # If no id is provided, redirect to index
    if id == None:
        return redirect(url_for("main.index"))
    
    # Get question
    question = Question.query.get(id)

    # If question is not found, return 404 page
    if question == None:
        return render_template("404.html"), 404

    return render_template("edit_question.html", question=question)
