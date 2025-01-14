import string
import random

def generate_password(passlen):
    if passlen < 4:
        print("Password length should be at least 4 to include all character types.")
        return

    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    # Ensuring at least one character from each category
    password = [
        random.choice(s1),
        random.choice(s2),
        random.choice(s3),
        random.choice(s4)
    ]

    # Filling the rest of the password length with random choices from all categories
    if passlen > 4:
        all_chars = s1 + s2 + s3 + s4
        password.extend(random.choices(all_chars, k=passlen-4))

    random.shuffle(password)
    return ''.join(password)

# Example usage
password_length = int(input("Enter Password length: "))
print(generate_password(password_length))
