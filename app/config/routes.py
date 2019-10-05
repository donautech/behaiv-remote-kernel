from flask import Response
from flask import json
from flask import request

from app import db
from app.config import bp
from app.models import AlchemyEncoder
from app.models import Config


@bp.route('/', methods=['POST'])
def add_config():
    config_json = request.json
    config = Config(key=config_json['key'], value=config_json['value'])
    if 'description' in config_json:
        config.description = config_json['description']
    db.session.add(config)
    db.session.commit()
    return 'OK'


@bp.route('/<id>', methods=['PUT'])
def update_config(id):
    config = Config.query.get(id)
    if config is None:
        return 'Not Found', 404
    config_json = request.json
    config.key = config_json['key']
    config.value = config_json['value']
    if 'description' in config_json:
        config.description = config_json['description']
    db.session.add(config)
    db.session.commit()
    return 'OK'


@bp.route('/', methods=['GET'])
def get_configs():
    return Response(json.dumps(Config.query.all(), cls=AlchemyEncoder), mimetype='application/json')


@bp.route('/<id>', methods=['DELETE'])
def delete_config(id):
    config = Config.query.get(id)
    if config is None:
        return 'Not Found', 404
    db.session.delete(config)
    db.session.commit()
    return 'OK'
