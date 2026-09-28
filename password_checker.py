print("=======================")
print("PASSWORD ANALYZER")
print("=======================")

again = "y"

while again == "y":

    password = input("\nEnter password: ")

    weak_passwords = ["password", "qwerty", "123456", "admin"]

    length = len(password)

    print("Password Length:", length)

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    has_repeated = False

    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            has_repeated = True

    score = 0

    if length >= 8:
        score += 2
    if has_uppercase:
        score += 2
    if has_lowercase:
        score += 2
    if has_digit:
        score += 2
    if has_special:
        score += 2

    print("Password Strength Score:", score, "/ 10")

    if length < 8:
        print("Password is too short. It should be at least 8 characters long.")

    if not has_uppercase:
        print("Password should contain at least one uppercase letter.")
    if not has_lowercase:
        print("Password should contain at least one lowercase letter.")
    if not has_digit:
        print("Password should contain at least one digit.")
    if not has_special:
        print("Password should contain at least one special character.")

    if has_repeated:
        print("Password contains repeated characters.")
        
    if password.lower() in weak_passwords:
        print("WARNING: This is a common weak password!")

    if score <= 4:
        print("Strength: Weak")
    elif score <= 7:
        print("Strength: Medium")
    else:
        print("Strength: Strong")

    print("\nSuggestions:")

    suggestions = 0

    if length < 8:
        print("- Make your password at least 8 characters long.")
        suggestions += 1

    if not has_uppercase:
        print("- Add an uppercase letter.")
        suggestions += 1

    if not has_lowercase:
        print("- Add a lowercase letter.")
        suggestions += 1

    if not has_digit:
        print("- Add a number.")
        suggestions += 1

    if not has_special:
        print("- Add a special character.")
        suggestions += 1

    if has_repeated:
        print("- Avoid repeating characters.")
        suggestions += 1

    if password.lower() in weak_passwords:
        print("- Avoid using common passwords.")
        suggestions += 1

    if suggestions == 0:
        print("No improvements needed!")

    again = input("\nTest another password? (y/n): ").lower()

print("\nThank you for using Password Analyzer!")