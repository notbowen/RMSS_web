from flask import Blueprint

bp = Blueprint("images", __name__)

from app.images import routes