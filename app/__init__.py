from flask import Flask, jsonify
from flask_cors import CORS
from flask_injector import FlaskInjector
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from config import Config

app = Flask(__name__, static_url_path='/web')

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

swaggerui_bp = get_swaggerui_blueprint(
    "/swagger",
    "http://localhost:5000/spec",
    config={
        'app_name': "Behaiv remote kernel"
    }
)

from app.kernel import providers

INJECTOR_DEFAULT_MODULES = dict(
    kernel=providers.KernelProvider
)

app.register_blueprint(client_bp, url_prefix='/')
app.register_blueprint(config_bp, url_prefix='/config')
app.register_blueprint(kernel_bp, url_prefix='/kernel')
app.register_blueprint(provider_bp, url_prefix='/provider')
app.register_blueprint(storage_bp, url_prefix='/storage')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(swaggerui_bp, url_prefix='/swagger')


FlaskInjector(
    app=app,
    modules=INJECTOR_DEFAULT_MODULES.values()
)


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "0.1"
    swag['info']['title'] = "Behaiv Remote Kernel API"
    return jsonify(swag)


from app import models

CORS(app)
