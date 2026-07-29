# tool: sort_list
# description: Sorts a list of comma-separated values.
# author: @navaneethsankar07
# example: sort_list 3,1,4,1,5,9 returns "[1, 1, 3, 4, 5, 9]"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        values = [int(value.strip()) for value in args[0].split(",")]
    except ValueError:
        return "Error: All values must be integers."

    values.sort()
    return str(values)
