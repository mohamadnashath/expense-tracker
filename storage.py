import json


def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return []


def save_data(expenses):
    with open("data.json", "w") as f:
        json.dump(expenses, f)
