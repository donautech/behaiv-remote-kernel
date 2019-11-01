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
    """
    Method that ensures you're on the right track
    ---
    responses:
      200:
        description: Dependency injection and API routing is working
    """
    print(kernel)
    return 'OK'


@injector.inject
@bp.route("/predictionReady")
def ready_to_predict(kernel: Kernel):
    return Response('{"predictionReady":true}' if kernel.ready_to_predict() else '{"predictionReady":false}',mimetype='application/json')


@injector.inject
@bp.route("/feed", methods=['POST'])
def feed_data(kernel: Kernel):
    """
    Feed network with more data
    ---
    tags:
        - kernel
    parameters:
        - in: body
          name: body
          schema:
            id: KernelData
            required:
                - features
                - label
            properties:
                features:
                    type: object
                    additionalProperties:
                        type: integer
                label:
                    type: string
                    description: label for features
    responses:
        200:
            description: data saved successfuly
        500:
            description: some problems occurred from backend side
    """
    new_data = request.json
    kernel.update_single(new_data)
    return 'OK'


@injector.inject
@bp.route("/predict")
def predict(kernel: Kernel):
    """
    Feed network with more data
    ---
    tags:
        - kernel
    parameters:
        - in: body
          name: body
          schema:
            id: KernelData
            required:
                - features
            properties:
                features:
                    type: object
                    additionalProperties:
                        type: integer
    responses:
        200:
            description: data saved successfuly
        500:
            description: some problems occurred from backend side
    """
    features = request.json['features']
    return str(kernel.predict_one(features)), 200


@injector.inject
@bp.route("/stats")
def stats(kernel: Kernel):
    return kernel.stats()
