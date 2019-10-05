import json

from sqlalchemy.ext.declarative import DeclarativeMeta

from app import db


class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, index=True, unique=True)
    value = db.Column(db.String, index=True, unique=False)
    description = db.Column(db.String, index=True, unique=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, index=True)
    login = db.Column(db.String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
