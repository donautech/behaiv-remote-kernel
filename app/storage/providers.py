import flask_injector
import injector
from flask import request

from app.kernel.kernel import Kernel
from app.kernel.logistic.LogisticRegressionKernel import LogisticKernel
from app.storage.storage import Storage, MongoStorage


class StorageProvider(injector.Module):

    def __init__(self):
        self.storages = {}

    def configure(self, binder):
        binder.bind(Kernel,
                    to=self.create,
                    scope=flask_injector.request)

    @injector.inject
    def create(self) -> Storage:
        token = request.headers['Authorization'][7:]
        if token in self.storages:
            return self.storages[token]
        else:
            storage = MongoStorage()
            self.storages[token] = storage
            return storage
