import uuid

from flask import Response
from flask import json
from flask import request

from app import db
from app.models import AlchemyEncoder
from app.models import User
from app.user import bp


@bp.route('/', methods=['POST'])
def register_user():
    new_user = User(login=request.json['login'], token=str(uuid.uuid1()))
    db.session.add(new_user)
    db.session.commit()
    return Response(json.dumps(new_user, cls=AlchemyEncoder), mimetype='application/json')
