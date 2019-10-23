from flask import Blueprint
from pymongo import MongoClient

bp = Blueprint('storage', __name__)
client = MongoClient()

behaiv_db = client.behaiv

network_tb = behaiv_db['network']
data_tb = behaiv_db['data']

data_tb.insert_one({"user": "123", "data": {"a": 123, "b": 456}})

from app.storage import routes
