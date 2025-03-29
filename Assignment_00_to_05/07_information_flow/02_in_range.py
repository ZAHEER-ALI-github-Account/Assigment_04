def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high  # Check if n is within the range

def main():
    n = int(input("Enter a number: "))  # Get user input for n
    low = int(input("Enter the lower bound: "))  # Get user input for low
    high = int(input("Enter the upper bound: "))  # Get user input for high
    print(in_range(n, low, high))  # Call the function and print the result

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
