# tool: generate_random_string
# description: Generates a random alphanumeric string of a specified length.
# author: @navaneethsankar07
# example: generate_random_string("10") returns "aB3kL9xZ2m"

import random
import string


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        length = int(args[0])
    except ValueError:
        return "Error: Length must be an integer."

    if length < 0:
        return "Error: Length must be non-negative."

    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))
