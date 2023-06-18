minimum_length = 8  # Minimum length for the password

while True:
    password = input("Enter a password: ")

    if len(password) < minimum_length:
        print(f"Password should be at least {minimum_length} characters long. Try again.")
    else:
        print("*" * len(password))
        break
