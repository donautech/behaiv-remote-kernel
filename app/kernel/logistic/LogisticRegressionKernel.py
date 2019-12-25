import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

from app.kernel.kernel import Kernel
from app.storage.storage import MongoStorage


class LogisticKernel(Kernel):

    def __init__(self, kernel_id, storage=MongoStorage()):
        super().__init__(kernel_id, storage)
        self.reg: LogisticRegression or None = None
        self.le = LabelEncoder()

    def fit(self):
        reg = LogisticRegression()

        data = self.data
        labels, features = zip(*[(it['label'], it['features']) for it in data['data']])
        labels = np.array(labels)
        encoded_labels = self.le.fit_transform(np.array(labels).reshape(len(labels), 1))

        reg.fit(pd.DataFrame(features).values, encoded_labels)
        self.reg = reg

    def predict_one(self, features):
        encoded_result = self.reg.predict([list(features.values())])[0]
        return self.le.inverse_transform([encoded_result])[0]
