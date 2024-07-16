import json


def json_f(diff):
    sorted_list = sorted(diff.items())
    sorted_diff = {}
    for key, value in sorted_list:
        sorted_diff[key] = value
    return json.dumps(sorted_diff)
