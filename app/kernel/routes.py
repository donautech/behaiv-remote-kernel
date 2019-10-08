import injector
from flask import Response
from flask import json
from flask import request

from app import db
from app.kernel import bp
from app.kernel.kernel import Kernel
from app.models import AlchemyEncoder
from app.models import Config

# TODO these endpoints haven't been tested yet, should be adjusted with LogisticRegressionKernel


@injector.inject
@bp.route("/")
def test_kernel(kernel: Kernel):
    print(kernel)
    return 'OK'


@injector.inject
@bp.route("/predictionReady")
def ready_to_predict(kernel: Kernel):
    return kernel.ready_to_predict()


@injector.inject
@bp.route("/feed")
def feed_data(kernel: Kernel):
    new_data = request.json
    kernel.data.extend(new_data)
    return 'OK'


@injector.inject
@bp.route("/predict")
def predict(kernel: Kernel):
    features = request.json
    return kernel.predict_one(features)


@injector.inject
@bp.route("/stats")
def stats(kernel: Kernel):
    return kernel.stats()
