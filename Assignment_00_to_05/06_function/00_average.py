def main():
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculating the average
    average = (num1 + num2) / 2

    # Printing the result
    print(f"The average of {num1} and {num2} is {average}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
