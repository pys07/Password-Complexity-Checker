#Python script to check password strength
#It checks for minimum length, presence of lowercase, uppercase, digit and special characters.
def check_strength(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()-_=+[]{}|;:',.<>?/":
            has_special = True

    feedback = []

    if len(password) < 8:
        feedback.append("\033[91m- Password is too short (min 8 characters).\033[0m")
    if not has_lower:
        feedback.append("\033[91m- Add at least one lowercase letter.\033[0m")
    if not has_upper:
        feedback.append("\033[91m- Add at least one uppercase letter.\033[0m")
    if not has_digit:
        feedback.append("\033[91m- Add at least one number.\033[0m")
    if not has_special:
        feedback.append("\033[91m- Add at least one special character (!@#$, etc.).\033[0m")

    return feedback

# Loop until password is strong
while True:
    password = input("Enter a password to test: ")

    feedback = check_strength(password)

    if not feedback:
        print("\033[92mPassword is strong! \033[0m")
        break
    else:
        print(" Your password needs improvement:")
        for item in feedback:
            print(item)
        print("\nPlease try again!\n")
