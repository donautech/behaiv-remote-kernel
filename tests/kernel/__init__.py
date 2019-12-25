from flask import Blueprint

bp = Blueprint('kernel', __name__)

from app.kernel import routes
