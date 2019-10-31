from flask import redirect

from app.client import bp


@bp.route('/')
def redirect_webapp():
    return redirect("/web/index.html", code=302)
