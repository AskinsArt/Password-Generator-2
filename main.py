import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    return "".join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    results = []
    if len(password) >= 12:
        results.append("✔️ Length is good (12+ characters)")
    else:
        results.append("❌ Too short (min 12 characters recommended)")

    if any(c.isupper() for c in password):
        results.append("✔️ Contains uppercase")
    else:
        results.append("❌ Missing uppercase")

    if any(c.islower() for c in password):
        results.append("✔️ Contains lowercase")
    else:
        results.append("❌ Missing lowercase")

    if any(c.isdigit() for c in password):
        results.append("✔️ Contains number")
    else:
        results.append("❌ Missing number")

    if any(c in string.punctuation for c in password):
        results.append("✔️ Contains symbol")
    else:
        results.append("❌ Missing symbol")

    return results

# Padlock ASCII Logo
padlock_logo = Fore.YELLOW + Style.BRIGHT + """
     .--------.
    / .------. \\
   / /        \\ \\
   | |        | |
   | |        | |
   | |        | |
   | '--------' |
    \\__________/
"""

# Welcome Banner
print(padlock_logo)
print(Fore.CYAN + Style.BRIGHT + """
=========================================
       🔒 SECUREPASS - PASSWORD MAKER
=========================================
""")

# Main menu
print("Would you like to:")
print("1️⃣ Generate a random secure password")
print("2️⃣ Check the strength of your own password")

choice = input(Fore.YELLOW + "Enter 1 or 2: ")

if choice == "1":
    # Ask user for password length
    while True:
        try:
            length = int(input(Fore.YELLOW + "Enter password length (min 6, max 20): "))
            if 6 <= length <= 20:
                break
            else:
                print(Fore.RED + "❌ Please enter a number between 6 and 20.")
        except ValueError:
            print(Fore.RED + "❌ Please enter a valid number.")

    # Generate password
    password = generate_password(length)
    print(Fore.GREEN + Style.BRIGHT + f"\n✅ Generated Password: {password}")

    # Password strength warning
    if length < 20:
        print(Fore.RED + Style.BRIGHT + "⚠️ Warning: This password is shorter than recommended guidelines (min 20 characters).")

    # Confirmation step
    print(Fore.CYAN + "\nNow let’s confirm your password...")
    password1 = input(Fore.YELLOW + "Enter your password: ")
    password2 = input(Fore.YELLOW + "Re-enter your password: ")

    print("\n-----------------------------------------")

    if password1 == password2 and password1 == password:
        print(Fore.GREEN + Style.BRIGHT + "✅ Password confirmed successfully!")
    elif password1 != password2:
        print(Fore.RED + Style.BRIGHT + "❌ Passwords do NOT match.")
    else:
        print(Fore.RED + Style.BRIGHT + "❌ Entered password doesn’t match the generated one.")

    print(Fore.CYAN + Style.BRIGHT + "\n🔒 Thank you for using SecurePass!")

elif choice == "2":
    while True:  # loop until they succeed or quit
        user_password = input(Fore.YELLOW + "Enter your password (or type 'exit' to quit): ")
        if user_password.lower() == "exit":
            print(Fore.CYAN + "👋 Exiting password check.")
            break

        results = check_password_strength(user_password)

        print(Fore.CYAN + "\nPassword Strength Check:")
        passed_all = True
        for r in results:
            if "✔️" in r:
                print(Fore.GREEN + r)
            else:
                print(Fore.RED + r)
                passed_all = False

        if passed_all:
            print(Fore.GREEN + Style.BRIGHT + "\n✅ This is a strong password!")
            break
        else:
            print(Fore.RED + Style.BRIGHT + "\n❌ Your password is weak. Please try again.\n")

else:
    print(Fore.RED + "❌ Invalid choice. Please restart and enter 1 or 2.")