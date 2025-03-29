import hashlib

def hash_password(password):
    """Returns the SHA256 hash of the input password."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the given email's stored password hash matches the hash of password_to_check.
    
    Parameters:
    - email (str): The user's email.
    - password_to_check (str): The password entered by the user.
    - stored_logins (dict): A dictionary storing emails as keys and hashed passwords as values.

    Returns:
    - True if the password matches, False otherwise.
    """
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

def main():
    # Sample stored logins with hashed passwords
    stored_logins = {
        "user1@example.com": hash_password("securepassword123"),
        "user2@example.com": hash_password("myp@ssword"),
        "admin@example.com": hash_password("admin2025")
    }

    # Simulate user login
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Login failed! Incorrect email or password.")

if __name__ == '__main__':
    main()
