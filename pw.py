import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            return
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if _name_ == "_main_":
    main()