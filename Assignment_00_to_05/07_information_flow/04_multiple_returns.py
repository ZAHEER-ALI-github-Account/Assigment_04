def get_user_data():
    """Prompts the user for their first name, last name, and email, then returns them as a tuple."""
    first_name = input("What is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()
    email = input("What is your email address?: ").strip()

    return first_name, last_name, email  # Returns a tuple with the three values

def main():
    user_data = get_user_data()  # Call the function to get user input
    print("Received the following user data:", user_data)  # Print the returned tuple

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
