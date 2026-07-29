# tool: is_mixed_case
# description: Checks if a string has both uppercase and lowercase letters.
# author: @navaneethsankar07
# example: is_mixed_case("Hello") returns "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = args[0]

    has_upper = any(char.isupper() for char in text)
    has_lower = any(char.islower() for char in text)

    return str(has_upper and has_lower)
