from flask import request, jsonify

from app.questions import bp

@bp.route("/save", methods=["POST"])
def save_question():
    """Save question route

    Accepts a POST request with a question in the body
    Saves question to database

    Returns a 200 OK if successful
    TODO: Return 400 if request is malformed"""

    # Get question from request
    question = request.get_json()
    print(question)

    # Craft JSON response
    response = {
        "success": 1,
        "message": "Question saved successfully"
    }

    return jsonify(response), 200