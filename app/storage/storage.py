from abc import ABC, abstractmethod

from app.storage import data_tb


class Storage(ABC):

    @abstractmethod
    def save_data(self, kernel_id, data):
        pass

    @abstractmethod
    def data_amount(self, kernel_id):
        pass

    @abstractmethod
    def get_data(self, kernel_id):
        pass


class MongoStorage(Storage):

    def save_data(self, kernel_id, data):
        kernel_entry = data_tb.find_one({"id": kernel_id})
        if kernel_entry is None:
            data_tb.insert_one({"id": kernel_id, "data": [data]})
        else:
            kernel_entry["data"].append(data)
            data_tb.save(kernel_entry)

    def data_amount(self, kernel_id):
        data_ = data_tb.find_one({"id": kernel_id})
        if data_ is None:
            return 0
        return len(data_["data"])

    def get_data(self, kernel_id):
        return data_tb.find_one({"id": kernel_id})
