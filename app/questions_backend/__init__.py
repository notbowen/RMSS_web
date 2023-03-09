from flask import Blueprint

bp = Blueprint("questions_backend", __name__)

from app.questions_backend import routes