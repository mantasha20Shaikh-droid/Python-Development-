import random
import string


def generate_password(length):
    characters = ""

    lower = input("Include lowercase letters? (y/n): ")
    upper = input("Include uppercase letters? (y/n): ")
    digits = input("Include numbers? (y/n): ")
    symbols = input("Include symbols? (y/n): ")

    if lower == "y":
        characters += string.ascii_lowercase

    if upper == "y":
        characters += string.ascii_uppercase

    if digits == "y":
        characters += string.digits

    if symbols == "y":
        characters += string.punctuation

    if characters == "":
        print("Please select at least one character type.")
        return

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


def main():
    length = int(input("Enter password length: "))
    generate_password(length)


if __name__ == "__main__":
    main()
