# tool: mask_email
# description: Masks an email address for privacy.
# author: @navaneethsankar07
# example: mask_email("user@example.com") returns "u***r@example.com"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one email address."

    email = args[0]

    if "@" not in email:
        return "Error: Invalid email address."

    username, domain = email.split("@", 1)

    if len(username) <= 2:
        masked = username
    else:
        masked = username[0] + "*" * (len(username) - 2) + username[-1]

    return f"{masked}@{domain}"
