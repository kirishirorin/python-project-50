import json
import yaml
from yaml.loader import SafeLoader


def load_file(file):
    if '.json' in file:
        with open(file, "r") as read_file:
            data = json.load(read_file)
            return data
    elif ('.yaml' in file) or ('.yml' in file):
        with open(file, "r") as read_file:
            data = yaml.load(read_file, Loader=SafeLoader)
            return data
