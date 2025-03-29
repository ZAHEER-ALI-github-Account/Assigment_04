# Define the legal adult age in the U.S.
ADULT_AGE = 18  

def is_adult(age):
    return age >= ADULT_AGE  # Returns True if age is 18 or more, otherwise False

def main():
    age = int(input("How old is this person?: "))  # Get user input as an integer
    print(is_adult(age))  # Call the function and print the result

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
