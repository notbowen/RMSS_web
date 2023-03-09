from flask import Blueprint

bp = Blueprint("questions_frontend", __name__)

from app.questions_frontend import routes