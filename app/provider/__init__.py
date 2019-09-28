from flask import Blueprint

bp = Blueprint('provider', __name__)

from app.provider import routes
