def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):  # Loop from 1 to num
        if num % i == 0:  # Check if i is a divisor
            print(i, end=" ")  # Print divisors on the same line

def main():
    num = int(input("Enter a number: "))  # Get user input
    print_divisors(num)  # Call the function

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
