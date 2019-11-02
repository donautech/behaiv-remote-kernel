from flask import Response
from flask import json
from flask import request

from app import db
from app.config import bp
from app.models import AlchemyEncoder
from app.models import Config


@bp.route('/', methods=['POST'])
def add_config():
    """
    Add new config object to global config
    ---
    tags:
        - config
    parameters:
        - in: body
          name: body
          schema:
            id: Config
            required:
                - key
                - value
            properties:
                key:
                    type: string
                    description: key of config
                value:
                    type: string
                    description: value for key of config
                description:
                    type: string
                    description: description of what this config is doing
    responses:
        200:
            description: object saved successfully
        404:
            description: no object was found
        500:
            description: some problems occurred from backend sid
    """
    config_json = request.json
    config = Config(key=config_json['key'], value=config_json['value'])
    if 'description' in config_json:
        config.description = config_json['description']
    db.session.add(config)
    db.session.commit()
    return 'OK'


@bp.route('/<id>', methods=['PUT'])
def update_config(id):
    """
    Update existing config
    ---
    tags:
        - config
    parameters:
        - in: path
          name: id
          "type": "string"
          description: id of existing config
        - in: body
          name: body
          schema:
            id: Config
            required:
                - key
                - value
            properties:
                key:
                    type: string
                    description: key of config
                value:
                    type: string
                    description: value for key of config
                description:
                    type: string
                    description: description of what this config is doing
    responses:
        200:
            description: object updated successfully
        404:
            description: no object was found
        500:
            description: some problems occurred from backend sid
    """
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
    """
    Get all existing objects
    ---
    tags:
        - config
    responses:
        200:
            description: returns all the config objects
            content:
                application/json:
                    schema:
                        $ref: '#/definitions/Config'
        404:
            description: no object was found
        500:
            description: some problems occurred from backend sid
    """
    return Response(json.dumps(Config.query.all(), cls=AlchemyEncoder), mimetype='application/json')


@bp.route('/<id>', methods=['DELETE'])
def delete_config(id):
    """
    Delete existing config
    ---
    tags:
        - config
    parameters:
        - in: path
          name: id
          type: string
          description: id of existing config
    responses:
        200:
            description: object deleted successfully
        404:
            description: no object was found
        500:
            description: some problems occurred from backend sid
    """
    config = Config.query.get(id)
    if config is None:
        return 'Not Found', 404
    db.session.delete(config)
    db.session.commit()
    return 'OK'
