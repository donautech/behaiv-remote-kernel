import flask_injector
import injector
from flask import request

from app.kernel.kernel import Kernel


class KernelProvider(injector.Module):

    def __init__(self):
        self.kernels = {}

    def configure(self, binder):
        binder.bind(Kernel,
                    to=self.create,
                    scope=flask_injector.request)

    @injector.inject
    def create(self) -> Kernel:
        # TODO implement real logistic kernel instead of a stub
        token = request.headers['Authorization']
        if token in self.kernels:
            return self.kernels[token]
        else:
            kernel = Kernel(token)
            self.kernels[token] = kernel
            return kernel
