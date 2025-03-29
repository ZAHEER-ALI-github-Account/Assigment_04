def main():
    # Ask the user for the dividend
    dividend = int(input("Please enter an integer to be divided: "))

    # Ask the user for the divisor
    divisor = int(input("Please enter an integer to divide by: "))

    # Perform division and calculate remainder
    quotient = dividend // divisor
    remainder = dividend % divisor

    # Print the result
    print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

# Call the main function
if __name__ == '__main__':
    main()
