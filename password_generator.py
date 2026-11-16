
import string
import secrets

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length (8-128): "))

    if length < 8 or length > 128:
        print("Please enter a length between 8 and 128.")
    else:
        characters = ""
        required = []

        if input("Include uppercase letters? (y/n): ").lower() == "y":
            characters += string.ascii_uppercase
            required.append(secrets.choice(string.ascii_uppercase))

        if input("Include lowercase letters? (y/n): ").lower() == "y":
            characters += string.ascii_lowercase
            required.append(secrets.choice(string.ascii_lowercase))

        if input("Include numbers? (y/n): ").lower() == "y":
            characters += string.digits
            required.append(secrets.choice(string.digits))

        if input("Include special characters? (y/n): ").lower() == "y":
            characters += string.punctuation
            required.append(secrets.choice(string.punctuation))

        if not characters:
            print("Please select at least one character type.")
        elif len(required) > length:
            print("Password length is too short for your selections.")
        else:
            password = required[:]

            for _ in range(length - len(password)):
                password.append(secrets.choice(characters))

            secrets.SystemRandom().shuffle(password)
            generated_password = "".join(password)

            print("\nYour generated password is:")
            print(generated_password)
            print("\nKeep your password private!")

except ValueError:
    print("Please enter a valid number.")
