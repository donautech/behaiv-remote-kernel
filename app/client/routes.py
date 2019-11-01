from flask import redirect

from app.client import bp


@bp.route('/')
def redirect_webapp():
    """
    Redirects to static folder with react ui
    ---
    tags:
        - ui
    responses:
        302:
            description: redirection to /web/index.html
    """
    return redirect("/web/index.html", code=302)
