from sqlalchemy import exc
from flask import request, jsonify

from app.questions_backend import bp
from app.extensions import db
from app.models.question import Question

@bp.route("/save", methods=["POST"])
def save_question():
    """Save question route

    Accepts a POST request with a question in the body
    Saves question to database

    Returns a 200 OK if successful
    TODO: Return 400 if request is malformed"""

    # Get question from request
    question = request.get_json()

    # Ensure question has all required fields
    required_fields = ["id", "section", "content", "answer", "category_id"]
    for field in required_fields:
        if field not in question:
            response = {
                "success": 0,
                "message": f"Missing required field: {field}"
            }
            return jsonify(response), 400

    # Ensure question id is not empty
    if question["id"].strip() == "":
        response = {
            "success": 0,
            "message": "Question id cannot be empty"
        }
        return jsonify(response), 400

    # Ensure content is a JSON object
    if not isinstance(question["content"], dict):
        response = {
            "success": 0,
            "message": "Content must be a JSON object"
        }
        return jsonify(response), 400

    # Ensure EditorJS has at least 1 block
    try:
        if len(question["content"]["blocks"]) == 0:
            response = {
                "success": 0,
                "message": "Content cannot be empty"
            }
            return jsonify(response), 400
    except KeyError:
        response = {
            "success": 0,
            "message": "Content cannot be empty"
        }
        return jsonify(response), 400

    # Ensure answer is not empty
    if question["answer"].strip() == "":
        response = {
            "success": 0,
            "message": "Answer cannot be empty"
        }
        return jsonify(response), 400

    # Create question object
    question = Question(
        id=question["id"],
        section=question["section"],
        content=question["content"],
        answer=question["answer"],
        category_id=question["category_id"]
    )

    # Add question to database
    try:
        db.session.add(question)
        db.session.commit()
    except exc.IntegrityError:
        response = {
            "success": 0,
            "message": "Question ID already exists"
        }
        return jsonify(response), 400
    except Exception as e:
        response = {
            "success": 0,
            "message": str(e)
        }
        return jsonify(response), 400


    # Craft JSON response
    response = {
        "success": 1,
        "message": "Question saved successfully"
    }

    return jsonify(response), 200