**Advanced Password Strength Checker**
About the Project:
The Advanced Password Strength Checker is a Python-based application that helps users understand how strong their passwords are.
1.The main idea behind this project is that checking only the password length or whether it contains numbers and special characters is not enough. A password can look complicated and still be easy to guess if it contains common words, repeated characters, or predictable patterns.
2.To make the checking process more useful, this project combines different methods such as password pattern checking, entropy calculation, "zxcvbn" analysis, and checking whether the password has appeared in known data breaches.
3.The application also includes a password generator that can create random passwords using Python's "secrets" module.

**What the Application Does**
The application checks a password and provides a strength result along with information about possible weaknesses.

Some of the checks include:
This Project Uses **Rule-Based Checks** and a **Password-Strength Estimation Library**.
1.Password length
2.Uppercase and lowercase characters
3.Numbers and special characters
4.Repeated characters
5.Sequential characters
6.Common password patterns
7.Password entropy
7.Password guessability
8.Presence in known password breaches
After the analysis, the user receives feedback about the password and suggestions for making it stronger.

## Main Features

**Password Strength Checking**
1.The application analyzes the password using several factors instead of depending on a single rule.
2.It can identify passwords that are short, repetitive, predictable, or based on commonly used patterns.

### Pattern Detection
1.The application checks for patterns that are frequently found in weak passwords.
For example:

```text
123456
password123
qwerty
aaaaaa
abcd1234
```
These types of passwords may satisfy some basic complexity requirements but can still be relatively easy to guess.

### Entropy Calculation
The application also considers password entropy to estimate how unpredictable a password is.
In general, a longer and less predictable password has a larger possible search space. However, entropy is not treated as the only measurement because a password containing predictable information can still be weak.

### zxcvbn Analysis
The project uses the `zxcvbn` library to get a more realistic estimate of password strength.
Instead of simply counting characters, `zxcvbn` considers common words, patterns, sequences, and other information that can make a password easier to guess.

### Breached Password Check
1.The project uses the **Have I Been Pwned (HIBP) Pwned Passwords API** to check whether a password has appeared in known data breaches.
2.The complete password is not sent to the API.
3.The application first creates a SHA-1 hash and uses the  k-anonymity method for the lookup. Only part of the hash is sent to the service, and the remaining comparison is performed locally.
4.This allows the application to check for known exposure without directly sending the user's complete password.

### Secure Password Generator
The application can also generate strong random passwords.
Python's `secrets` module is used instead of a normal pseudo-random approach because it is intended for security-related random values.

## Technologies Used

1. **Python** – Main programming language
2. **Tkinter** – Desktop graphical interface
3. **zxcvbn** – Password strength and guessability analysis
4. **HIBP Pwned Passwords API** – Breached password checking
5. **SHA-1** – Hash generation for the HIBP lookup
6. **k-anonymity** – Used during the HIBP password lookup
7.**REST API** – Communication with the HIBP service
8. **Regular Expressions** – Pattern and character checks
9. **Python `secrets`** – Secure password generation

## How It Works
The basic working flow of the application is:
```text
User enters password
        ↓
Basic password checks
        ↓
Pattern and repetition analysis
        ↓
Entropy calculation
        ↓
zxcvbn strength analysis
        ↓
HIBP breach check
        ↓
Combine the results
        ↓
Display strength and suggestions
```
The password is analyzed and the application gives the user a final assessment instead of relying only on one measurement.

## Project Structure

```text
Advanced-Password-Checker/
│
├── psc.py
├── README.md
│
└── screenshots/
    └── lock.png
```
The filenames can be changed depending on the actual structure of the project.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/advanced-password-checker.git
```

### 2. Open the project folder

```bash
cd advanced-password-checker
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

For example, the requirements file can contain:

```text
requests
zxcvbn
```

The other modules used in the project, such as `tkinter`, `hashlib`, `re`, `string`, and `secrets`, are part of Python's standard library where supported by the Python installation.

### 4. Run the application

```bash
python password_checker.py
```

## Example

Suppose the user enters:

```text
Password123
```

The password contains different character types, but that does not automatically make it strong.

The application can identify that it contains a common word and a predictable number sequence. The `zxcvbn` analysis can also take these patterns into account when estimating how easy the password may be to guess.

This is one of the reasons the project uses several checks instead of simply saying:

> "It has uppercase, lowercase, numbers and special characters, so it is strong."

## Security Approach

One of the main goals of this project was to avoid treating passwords as normal application data.

The application does not need to maintain a database of plaintext passwords for the strength-checking functionality.

For breach checking, the password is processed locally and the HIBP k-anonymity approach is used instead of sending the complete password to the API.

The password generator also uses the `secrets` module to produce random values suitable for security-related use.

## What I Learned From This Project

While working on this project, I gained practical understanding of:

1. Password security
2.Password entropy
3.Password guessing techniques
4.Common password patterns
5.Password breach checking
6.SHA-1 hashing
7.k-anonymity
8.REST API usage
9.Python GUI development
10.Regular expression based validation
11.Secure random password generation

The project also helped me understand why password security cannot be judged only by checking whether a password contains uppercase letters, numbers, and special characters.

## Future Improvements

Some improvements I would like to add in the future are:
1.Add more password pattern checks
2.Improve the user interface
3.Provide more detailed explanations for weak passwords
4.Add passphrase analysis
5.Add more password-generation options
6.Improve the scoring method by combining the different results more effectively

## Disclaimer

**This project is created for learning and cybersecurity awareness.

A password not being found by the breach-checking service does not guarantee that the password has never been exposed. Users should also avoid entering passwords from important personal accounts into applications they do not trust.
**
## Author

**D. Bhanu Charan**

Cybersecurity Student

**Interests:** Cybersecurity, Network Security, Digital Forensics, Threat Intelligence and Application Security

