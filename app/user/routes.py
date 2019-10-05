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
    user_data = request.json
    new_user = User(login=user_data['login'], token=str(uuid.uuid1()), verification_token=str(uuid.uuid1()))
    # we allow users to set their own token, e.g if mobile developers decide to attach devices' uuid
    # it will give them ability to restore device later on
    if 'token' in user_data:
        new_user.token = user_data['token']
    db.session.add(new_user)
    db.session.commit()
    return Response(json.dumps(new_user, cls=AlchemyEncoder), mimetype='application/json')
