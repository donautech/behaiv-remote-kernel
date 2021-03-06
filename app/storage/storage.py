from app.storage import data_tb


def save_data(kernel_id, data):
    kernel_entry = data_tb.find_one({"id": kernel_id})
    if kernel_entry is None:
        data_tb.insert_one({"id": kernel_id, "data": [data]})
    else:
        kernel_entry["data"].append(data)
        data_tb.save(kernel_entry)


def data_amount(kernel_id):
    data_ = data_tb.find_one({"id": kernel_id})
    if data_ is None:
        return 0
    return len(data_["data"])


def get_data(kernel_id):
    return data_tb.find_one({"id": kernel_id})


class Storage:
    pass
