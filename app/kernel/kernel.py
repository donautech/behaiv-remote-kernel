from app.storage import storage


class Kernel:

    def __init__(self, kernel_id):
        self.kernel_id = kernel_id
        self.threshold = 100
        self.partial_fit_allowed = False
        self.always_keep_data = True

    @property
    def data(self):
        return storage.get_data(self.kernel_id)

    @property
    def empty(self):
        return storage.data_amount(self.kernel_id) == 0

    def fit(self):
        pass

    def ready_to_predict(self):
        return storage.data_amount(self.kernel_id) >= self.threshold

    def update_single(self, entry):
        storage.save_data(self.kernel_id, entry)

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
