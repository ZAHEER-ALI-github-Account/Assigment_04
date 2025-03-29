def print_ones_digit(num):
    ones_digit = num % 10  # Get the ones digit using modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Get user input as an integer
    print_ones_digit(num)  # Call the function with the input number

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
