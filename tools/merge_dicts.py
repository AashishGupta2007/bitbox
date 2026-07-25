# tool: merge_dicts
# description: Merges two JSON dictionaries.
# author: @navaneethsankar07
# example: merge_dicts('{"a":1}', '{"b":2}') returns '{"a": 1, "b": 2}'

import json


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two JSON dictionaries."

    try:
        dict1 = json.loads(args[0])
        dict2 = json.loads(args[1])
    except json.JSONDecodeError:
        return "Error: Invalid JSON."

    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return "Error: Inputs must be JSON dictionaries."

    merged = {**dict1, **dict2}

    return json.dumps(merged)