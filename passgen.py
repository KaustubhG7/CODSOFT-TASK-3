############ TASK-3 : Password Generator #######################  
########### Kaustubh Gaikwad ##############

import random
import string

def generate_password(length, include_special_chars=True, include_spaces=False):
    # Error handling for password length
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    whitespace = string.whitespace

    # Combine character sets based on user preferences
    all_characters = lowercase + uppercase + digits
    if include_special_chars:
        all_characters += special_characters
    if include_spaces:
        all_characters += whitespace

    # Ensure the password contains at least one character from each category if special characters are included
    password = []
    if include_special_chars:
        password.append(random.choice(lowercase))
        password.append(random.choice(uppercase))
        password.append(random.choice(digits))
        password.append(random.choice(special_characters))
    else:
        password.append(random.choice(lowercase))
        password.append(random.choice(uppercase))
        password.append(random.choice(digits))

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        print("Choose the type of password:")
        print("1. Alphanumeric (with special characters)")
        print("2. Alphanumeric (without special characters)")
        print("3. Alphanumeric (with spaces)")
        print("4. Alphanumeric (without special characters and spaces)")
        
        choice = input("Enter the number corresponding to your choice: ")

        if choice == '1':
            password = generate_password(length, include_special_chars=True, include_spaces=False)
        elif choice == '2':
            password = generate_password(length, include_special_chars=False, include_spaces=False)
        elif choice == '3':
            password = generate_password(length, include_special_chars=True, include_spaces=True)
        elif choice == '4':
            password = generate_password(length, include_special_chars=False, include_spaces=False)
        else:
            print("Invalid choice. Please select a valid option.")
            return

        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()