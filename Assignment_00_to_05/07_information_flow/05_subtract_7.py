def subtract_seven(num):
    """Subtracts 7 from the given number and returns the result."""
    return num - 7

def main():
    number = int(input("Enter a number: "))  # Get user input and convert to integer
    result = subtract_seven(number)  # Call the helper function
    print("Result after subtracting 7:", result)  # Print the result

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
