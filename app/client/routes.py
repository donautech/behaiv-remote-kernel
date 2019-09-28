from app.client import bp
from flask import redirect

@bp.route('/')
def redirect_webapp():
    return redirect("/index.html", code=302)