import injector
from flask import Response
from flask import json
from flask import request

from app import db
from app.kernel import bp
from app.kernel.kernel import Kernel
from app.models import AlchemyEncoder
from app.models import Config


@injector.inject
@bp.route("/")
def test_kernel(kernel: Kernel):
    print(kernel)
    return 'OK'

