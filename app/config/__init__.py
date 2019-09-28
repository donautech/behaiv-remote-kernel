from flask import Blueprint

bp = Blueprint('config', __name__)

from app.config import routes
