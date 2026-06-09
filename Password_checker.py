import re

def check_password_strength(password):
    # Rules
    min_length     = len(password) >= 8
    has_number     = bool(re.search(r'\d', password))
    has_special    = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    has_uppercase  = bool(re.search(r'[A-Z]', password))

    # All rules must pass for "Strong"
    if min_length and has_number and has_special and has_uppercase:
        print("Strong 💪")
    else:
        print("Weak ❌")
        # Show what's missing
        if not min_length:
            print("  - Need at least 8 characters")
        if not has_uppercase:
            print("  - Need at least 1 uppercase letter")
        if not has_number:
            print("  - Need at least 1 number")
        if not has_special:
            print("  - Need at least 1 special character")

password = input("Enter a password: ")
check_password_strength(password)