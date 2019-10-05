class Kernel:

    def __init__(self, kernel_id):
        self.kernel_id = kernel_id
        self.data = []
        self.threshold = 100
        self.partial_fit_allowed = False
        self.always_keep_data = True

    @property
    def empty(self):
        return len(self.data) == 0

    def fit(self):
        pass

    def ready_to_predict(self):
        return len(self.data) >= self.threshold

    def update_single(self, entry):
        self.data.append(entry)

    def predict_one(self, features):
        pass

    def save(self, storage):
        pass

    def restore(self, storage):
        pass
