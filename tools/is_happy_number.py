# tool: is_happy_number
# description: check if a number is a happy number
# author: @HeaTTap
# example: is_happy_number "19" -> "True"

def run(*args) -> str:
    if not args:
        return "Error: expected an integer"
    try:
        n = int(args[0])
    except ValueError:
        return "Error: argument must be an integer"
    
    if n <= 0:
        return "False"
        
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
        
    return "True" if n == 1 else "False"
