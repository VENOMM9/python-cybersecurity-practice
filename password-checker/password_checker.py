import re

def check_password_strength(password):
    length = len(password)

    if length < 6:
        return "Too short"

    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"\W", password)

    len_has_digit = len(has_digit)
    len_has_special = len(has_special)

    if has_upper and has_lower and (has_digit or has_special):
        return "Strong"
    elif has_upper or has_lower:
        return "Medium"
    else:
        return "Weak"
    
    if (len_has_digit or len_has_special) > 4:
        return "too many digite or special"
    elif (len_has_special or len_has_digit) <= 4:
        return "correctly done"
    else:
        return "weak"

password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
