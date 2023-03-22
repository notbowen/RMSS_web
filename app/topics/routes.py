from flask import render_template, request

from app.topics import bp
from app.models.category import Category
from app.extensions import db

@bp.route("/edit", methods=["GET", "POST"])
def edit_topics():
    # Handle POST request
    if request.method == "POST":
        # Get ID from URL query parameters
        id = request.args.get("id", type=int)

        # Ensure ID is present
        if id == None:
            return "Missing ID", 400

        # Get data
        content = request.get_json()

        # Ensure data is valid
        if not content:
            return "No data provided", 400
        
        # Ensure ID is valid
        category = Category.query.get(id)
        if not category:
            return "Invalid ID", 400

        # Update category
        try:
            category.level = content["level"]
            category.subject = content["subject"]
            category.topic = content["topic"]
        except KeyError:
            return "Missing data", 400

        # Save changes
        db.session.commit()

        return "OK", 200

    # Handle GET request
    categories = Category.query.all()
    return render_template("edit_topics.html", categories=categories)

@bp.route("/add", methods=["POST"])
def add_topic():
    """ Adds a new topic to the database """
    # Get data
    content = request.get_json()

    # Ensure data is valid
    if content == None:
        return "No data provided", 400

    # Ensure data is valid
    try:
        level = content["level"]
        subject = content["subject"]
        topic = content["topic"]
    except KeyError:
        return "Missing data", 400
    
    # Ensure none of the fields are empty
    if level.strip() == "" or subject.strip() == "" or topic.strip() == "":
        return "Fields cannot be empty", 400

    # Ensure none of the fields are above 100 characters
    if len(level) > 100 or len(subject) > 100 or len(topic) > 100:
        return "Fields cannot be longer than 100 characters", 400

    # Add topic to database
    category = Category(level=level, subject=subject, topic=topic)
    db.session.add(category)
    db.session.commit()

    return "OK", 200