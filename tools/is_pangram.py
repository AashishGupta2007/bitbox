# tool: is_pangram
# description: Checks if a string contains every letter of the alphabet.
# author: @navaneethsankar07
# example: is_pangram("The quick brown fox jumps over the lazy dog") returns "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = args[0].lower()
    letters = set()

    for char in text:
        if char.isalpha():
            letters.add(char)

    return str(len(letters) == 26)