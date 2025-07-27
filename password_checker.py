#Python script to check password strength
#It checks for minimum length, presence of lowercase, uppercase, digit and special characters.
def check_strength(password):
    haslower=False
    hasupper=False
    hasdigit=False
    haspecial=False


    for char in password:
        if char.islower():
            haslower = True
        elif char.isupper():
            hasupper = True
        elif char.isdigit():
            hasdigit = True
        elif char in "!@#$%^&*()-_=+[]{}|;:',.<>?/":
            haspecial = True
    
    feedback=[]


    if len(password) < 8:
         feedback.append("Password is too short.Minimum 8 characters long.")
    if not haslower:
        feedback.append("Add at least one lowercase letter.")
    if not hasupper:
        feedback.append("Add at least one uppercase letter.")
    if not hasdigit:
        feedback.append("Add at least one digit.")
    if not haspecial:
        feedback.append("Add at least one special character.")

    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    if not feedback:
        return f"{GREEN} Password is strong!{RESET}"
    elif len(feedback) <= 2:
        return f"{YELLOW} Medium strength password:\n" + "\n".join(f" - {point}" for point in feedback) + f"{RESET}"
    else:
        return f"{RED} Weak password:\n" + "\n".join(f" - {point}" for point in feedback) + f"{RESET}"


password=input("Enter password:")
print(check_strength(password))

