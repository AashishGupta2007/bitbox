# tool: count_palindromes
# description: Counts the number of palindromic substrings in a string.
# author: @navaneethsankar07
# example: count_palindromes("abba") returns "6"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = args[0]
    count = 0

    def expand(left: int, right: int) -> int:
        total = 0

        while left >= 0 and right < len(text) and text[left] == text[right]:
            total += 1
            left -= 1
            right += 1

        return total

    for i in range(len(text)):
        count += expand(i, i)
        count += expand(i, i + 1)

    return str(count)
