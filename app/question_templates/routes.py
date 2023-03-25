from flask import render_template, request

from app.question_templates import bp
from app.extensions import db

from app.models.template import Template
from app.models.question import Question

@bp.route("/", methods=["GET"])
def index():
    return render_template("question_templates.html")

@bp.route("/add", methods=["POST"])
def add_to_template():
    """ Adds selected questions to a template.
        If template does not exist, creates a new template.
    """

    # Get POST JSON data
    data = request.get_json()

    # Reject if no JSON data is found, or data is malformed
    if data is None or "template" not in data or "questions" not in data:
        return "Bad Request", 400
    
    # Get template name and questions
    template_id = data["template"]
    questions = data["questions"]

    # Ensure that template ID is a string
    if not isinstance(template_id, str):
        return "Template ID should be a string!", 400

    # Ensure that questions is a list
    if not isinstance(questions, list):
        return "Questions should be an array!", 400

    # Ensure that questions is not empty
    if len(questions) == 0:
        return "No questions selected!", 400

    # Get template from database and create new template if it does not exist
    template = Template.query.filter_by(id=template_id).first()
    if template is None:
        template = Template(name=template_id)
        db.session.add(template)
    
    # Add questions to template
    template_questions = set(template.questions)  # Convert to set to remove duplicates

    for question in questions:
        # Ensure question is a valid question
        queried_question = Question.query.filter_by(id=question).first()
        if not queried_question:
            return f"Question {question} does not exist", 400

        # Add question to template
        template_questions.add(queried_question)

    template.questions = list(template_questions)
    db.session.commit()

    return "Questions added to template", 200
