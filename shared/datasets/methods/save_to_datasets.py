import os
import json


def save_to_datasets_as_json(directory: str, name: str, data: dict):
    directory_path = f"shared/datasets/data/data_{directory}"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file = open(f"shared/datasets/data/data_{directory}/{name}.json", "w+")
    file.write(json.dumps(data))
    file.close()



