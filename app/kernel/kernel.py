

class Kernel:
    DEFAULT_THRESHOLD = 10

    def __init__(self, kernel_id, storage):
        self.kernel_id = kernel_id
        self.threshold = Kernel.DEFAULT_THRESHOLD
        self.partial_fit_allowed = False
        self.always_keep_data = True
        self.storage = storage

    @property
    def data(self):
        return self.storage.get_data(self.kernel_id)

    @property
    def empty(self):
        return self.storage.data_amount(self.kernel_id) == 0

    def fit(self):
        pass

    def ready_to_predict(self):
        return self.storage.data_amount(self.kernel_id) >= self.threshold

    def update_single(self, entry):
        self.storage.save_data(self.kernel_id, entry)
        if self.ready_to_predict():
            self.fit()

    def predict_one(self, features):
        pass

    def save(self):
        pass

    def restore(self):
        pass

    def stats(self):
        return {
            'id': self.kernel_id,
            'data_size': len(self.data),
            'threshold': self.threshold,
            'partial_fit_allowed': self.partial_fit_allowed,
            'always_keep_data': self.always_keep_data
        }
