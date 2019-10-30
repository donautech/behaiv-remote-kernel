import flask_injector
import injector
from flask import request

from app.kernel.kernel import Kernel
from app.kernel.logistic import LogisticKernel


class KernelProvider(injector.Module):

    def __init__(self):
        self.kernels = {}

    def configure(self, binder):
        binder.bind(Kernel,
                    to=self.create,
                    scope=flask_injector.request)

    @injector.inject
    def create(self) -> Kernel:
        token = request.headers['Authorization']
        if token in self.kernels:
            return self.kernels[token]
        else:
            kernel = LogisticKernel(token)
            if kernel.ready_to_predict():
                kernel.fit()
            self.kernels[token] = kernel
            return kernel
