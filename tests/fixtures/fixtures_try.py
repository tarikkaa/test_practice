import json

import pytest

data_path = "..\\utilities\\test_data\\test_data.json"
def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@pytest.fixture(params=load_test_data(data_path))
def set_data(request):
    data = request.param
    return data


