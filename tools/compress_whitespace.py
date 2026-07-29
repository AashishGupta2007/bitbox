# tool: compress_whitespace
# description: Replace multiple whitespace characters with a single space
# author: @HeaTTap
# example: compress_whitespace "hello   world" -> "hello world"

import re


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    text = args[0]
    return re.sub(r"\s+", " ", text)
