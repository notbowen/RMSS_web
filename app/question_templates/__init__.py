from flask import Blueprint

bp = Blueprint("question_templates", __name__)

from app.question_templates import routes