import random
import string

def generate_simple_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_medium_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits)
    for _ in range(length - 3):
        password += random.choice(string.ascii_letters + string.digits)
    return ''.join(random.sample(password, len(password)))

def generate_complex_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        
        print("Password Complexity Options:")
        print("1. Simple (Letters and Digits)")
        print("2. Medium (Uppercase, Lowercase, and Digits)")
        print("3. Complex (Uppercase, Lowercase, Digits, and Special Characters)")
        
        choice = input("Enter the complexity option (1/2/3): ")
        
        if choice == '1':
            password = generate_simple_password(length)
        elif choice == '2':
            password = generate_medium_password(length)
        elif choice == '3':
            password = generate_complex_password(length)
        else:
            print("Invalid option. Please select 1, 2, or 3.")
            exit(1)

        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
