# tool: octal_to_decimal
# description: Converts an octal string to its decimal integer value
# author: Selvakanthan Jagavan
# example: python bitbox.py octal_to_decimal 77

def run(octal: str) -> str:
    try:
        return str(int(octal, 8))
    except ValueError:
        return "Error: Invalid octal number"