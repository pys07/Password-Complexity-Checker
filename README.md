<h2 align="center">🔐 Password Complexity Checker</h2>
  
A beginner-friendly Python tool that checks password strength in real-time and keeps you looped in until you're **truly secure**.

---

## 💡 Features

* Evaluates password strength based on:
  * Minimum length of 8 characters
  * Presence of lowercase letters
  * Presence of uppercase letters
  * Presence of numbers
  * Presence of special characters (e.g., !, @, #, etc.)
  
* Feedback includes:
  * Color-coded messages using ANSI escape codes:
    * 🟥 **Red** → Weak
    * 🟩 **Green** → Strong
  * Immediate tips to improve the password
  * Loop continues until a strong password is entered

---

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/pys07/PRODIGY_CS_03.git
cd PRODIGY_CS_03
````

2. Run the script:

```bash
python password_checker.py
```

> Best viewed in terminals supporting ANSI colors: VS Code Terminal, Bash, CMD, or PowerShell.

---

## 🧪 Sample Output

```
Enter a password to test: mycat
🟥 Weak password:
 - Password is too short.
 - Include at least one uppercase letter.
 - Include at least one number.
 - Include at least one special character.

Enter a password to test: MidnightSky12!
🟩 Strong password!
```

---

## 📁 Project Structure

```
.
├── password_checker.py
└── README.md
```

---

## 📸 Demo


---

## 🔒 Disclaimer

This tool is for **educational use only**. It doesn’t save or transmit any data. Ideal for beginners learning about password validation, logic building, and user interaction design.

---

## ✍️ Author

Made with ❤️ by [Payal Samant](https://github.com/pys07)


