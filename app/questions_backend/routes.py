import ast
import docx

from sqlalchemy import exc
from flask import request, jsonify, render_template, redirect, url_for

from app.questions_backend import bp
from app.extensions import db
from app.models.question import Question
from app.models.category import Category

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
            "message": "Malformed content object!"
        }
        return jsonify(response), 400

    # Ensure answer is not empty
    if not isinstance(question["answer"], dict):
        response = {
            "success": 0,
            "message": "Answer must be a JSON object"
        }
        return jsonify(response), 400
    
    # Ensure answer has at least 1 block
    try:
        if len(question["answer"]["blocks"]) == 0:
            response = {
                "success": 0,
                "message": "Answer cannot be empty"
            }
            return jsonify(response), 400
    except KeyError:
        response = {
            "success": 0,
            "message": "Malformed answer object!"
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

@bp.route("/edit", methods=["POST"])
def edit_question():
    """Edit question route

    Accepts a POST request with a question content
    and answer in the body.
    Edits question in database via ID provided

    Returns a 200 OK if successful"""

    # Get question from request
    question_data = request.get_json()

    # Ensure question has all required fields
    required_fields = ["id", "content", "answer"]
    for field in required_fields:
        if field not in question_data:
            response = {
                "success": 0,
                "message": f"Missing required field: {field}"
            }
            return jsonify(response), 400

    # Ensure question id is not empty
    if question_data["id"].strip() == "":
        response = {
            "success": 0,
            "message": "Question id cannot be empty"
        }
        return jsonify(response), 400

    # Ensure content is a JSON object
    if not isinstance(question_data["content"], dict):
        response = {
            "success": 0,
            "message": "Content must be a JSON object"
        }
        return jsonify(response), 400

    # Ensure EditorJS has at least 1 block
    try:
        if len(question_data["content"]["blocks"]) == 0:
            response = {
                "success": 0,
                "message": "Content cannot be empty"
            }
            return jsonify(response), 400
    except KeyError:
        response = {
            "success": 0,
            "message": "Malformed content object!"
        }
        return jsonify(response), 400

    # Ensure answer is not empty
    if not isinstance(question_data["answer"], dict):
        response = {
            "success": 0,
            "message": "Answer must be a JSON object"
        }
        return jsonify(response), 400
    
    # Ensure answer has at least 1 block
    try:
        if len(question_data["answer"]["blocks"]) == 0:
            response = {
                "success": 0,
                "message": "Answer cannot be empty"
            }
            return jsonify(response), 400
    except KeyError:
        response = {
            "success": 0,
            "message": "Malformed answer object!"
        }
        return jsonify(response), 400

    # Get question from database
    question = Question.query.filter_by(id=question_data["id"]).first()

    # Ensure question exists
    if question is None:
        response = {
            "success": 0,
            "message": "Question does not exist"
        }
        return jsonify(response), 400

    # Update question
    question.content = question_data["content"]
    question.answer = question_data["answer"]

    # Commit changes to database
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        response = {
            "success": 0,
            "message": str(e)
        }
        return jsonify(response), 400
    
    # Craft JSON response
    response = {
        "success": 1,
        "message": "Question edited successfully"
    }

    return jsonify(response), 200

@bp.route("/delete", methods=["GET"])
def delete_question():
    """Delete question route

    Accepts a POST request with a question id as query parameter
    Deletes question from database

    Returns a 200 OK if successful"""

    # Get question id from request
    question_id = request.args.get("id", None, type=str)

    # Get optional params from request
    section = request.args.get("section", None, type=str)
    category = request.args.get("category", None, type=int)

    # Ensure question id is not empty
    if question_id is None:
        render_template("error.html", message="Question ID cannot be empty"), 400
    
    # Get question from database
    question = Question.query.filter_by(id=question_id).first()

    # Ensure question exists
    if question is None:
        return render_template("404.html"), 404
    
    # Delete question from database
    try:
        db.session.delete(question)
        db.session.commit()
    except Exception as e:
        return render_template("error.html", message=str(e)), 400

    # Redirect to list questions with specified params
    if section is not None and category is not None:
        return redirect(url_for("questions_frontend.search_question", section=section, category=category))
    elif section is not None:
        return redirect(url_for("questions_frontend.search_question", section=section))
    elif category is not None:
        return redirect(url_for("questions_frontend.search_question", category=category))
    
    # Redirect to search
    categories = Category.query.all()
    return render_template("search_question.html", categories=categories), 200

@bp.route("/export", methods=["POST"])
def export_questions():
    """Export questions route

    Accepts a POST request with a list of question ids
    Exports questions to a Word document

    Returns a 200 OK if successful"""

    # Get question ids from request
    try:
        question_ids = request.form["questions"]
    except KeyError:
        return "No questions provided!", 400
    
    # Turn question ids into a list
    try:
        question_ids = ast.literal_eval(question_ids)
    except:
        return "Unable to parse question IDs!", 400
    
    # Ensure question ids is not empty
    if len(question_ids) == 0:
        return "No questions provided!", 400

    # Get questions from database
    questions = []
    for question_id in question_ids:
        question = Question.query.filter_by(id=question_id).first()
        if question is not None:
            questions.append(question)
        else:
            return f"Question with ID: {question_id} does not exist!", 400

    # Get Word document
    try:
        doc = docx.Document(request.files["document"])
    except KeyError:
        return "No file provided!", 400

    # Loop through questions and parse to Word document
    for question in questions:
        # TODO: Create function to parse question content & answer to Word document
        pass

    return "OK", 200
    