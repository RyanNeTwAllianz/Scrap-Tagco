import json


def read_json(file_name: str):
    with open(f'{file_name}.json', 'r') as file:
        data = json.load(file)
        return data
        