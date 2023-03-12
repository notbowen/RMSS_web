from flask import request, jsonify, current_app
from werkzeug.utils import secure_filename

import os
import uuid
import datetime

from app.images import bp

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename: str) -> bool:
    """ Function to check if filetype is allowed """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/upload_file', methods=['POST'])
def upload_file():
    """Image upload route

    Accepts a POST request with a image in the body
    Name would be randomly generated
    TODO: Change name to be question ID with a incrementing number

    Returns a JSON response with the URL to the image"""

    # Check if image in request
    if "image" not in request.files:
        return "No image in request", 400

    # Extract image from request
    image = request.files["image"]

    # Check if filename is empty
    if image.filename == "":
        return "No filename", 400

    # Check if filetype is allowed and save image before returning URL
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        filename = "{}{:-%Y%m%d%H%M%S}.{}".format(str(uuid.uuid4()), datetime.datetime.now(), filename.rsplit('.', 1)[1].lower())

        image.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))

        # Craft JSON response
        response = {
            "success": 1,
            "file": {
                "url": current_app.config["UPLOAD_URL"] + "/" + filename
            }
        }

        return jsonify(response), 200

    return "Something went wrong", 500


@bp.route("/upload_url", methods=['POST'])
def upload_url():
    """ This endpoint should not be used """
    return "<h1>This endpoint should not be used</h1>", 301
