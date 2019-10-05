from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__, static_url_path='/')

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from app.client import bp as client_bp
from app.config import bp as config_bp
from app.kernel import bp as kernel_bp
from app.provider import bp as provider_bp
from app.storage import bp as storage_bp
from app.user import bp as user_bp

app.register_blueprint(client_bp, url_prefix='/')
app.register_blueprint(config_bp, url_prefix='/config')
app.register_blueprint(kernel_bp, url_prefix='/kernel')
app.register_blueprint(provider_bp, url_prefix='/provider')
app.register_blueprint(storage_bp, url_prefix='/storage')
app.register_blueprint(user_bp, url_prefix='/user')

from app import models

CORS(app)
