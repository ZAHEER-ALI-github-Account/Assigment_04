def main():
    print("Welcome to the Simple Addition Calculator!")
    
    # Taking input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Calculating sum
    total = num1 + num2
    
    # Displaying result
    print(f"The sum of {num1} and {num2} is {total}.")

if __name__ == '__main__':
    main()
