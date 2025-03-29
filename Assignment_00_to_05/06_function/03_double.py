def double(num):
    return num * 2

def main():
    num = float(input("Enter a number: "))  # Taking user input
    result = double(num)  # Calling the function
    print(f"Double that is {result}")  # Printing the result

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
