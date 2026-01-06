import re

password = input("Enter a password to check strength: ")

strength = 0

if len(password) >= 8:
    strength += 1

if re.search("[A-Z]", password):
    strength += 1

if re.search("[a-z]", password):
    strength += 1

if re.search("[0-9]", password):
    strength += 1

if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1

print("\nPassword Strength Result:")

if strength <= 2:
    print("❌ Weak Password")
    print("\nSecurity Tips:")
    print("- Use at least 8–12 characters")
    print("- Mix uppercase, lowercase, numbers, and symbols")
    print("- Avoid common words or personal information")
    print("- Consider using a passphrase for better security")
elif strength == 3 or strength == 4:
    print("⚠️ Medium Strength Password")
    print("- Mix uppercase, lowercase, numbers, and symbols")
    print("- Consider using a passphrase for better security")
else:
    print("✅ Strong Password")
    print("Great job! Your password is strong.")

