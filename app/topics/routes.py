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