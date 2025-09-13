import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Weak: Include at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Include at least one lowercase letter."
    if not re.search(r'\d', password):
        return "Weak: Include at least one number."
    if not re.search(r'[\W_]', password):
        return "Weak: Include at least one special character."
    return "Strong password!"

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
