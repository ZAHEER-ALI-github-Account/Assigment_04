def main():
    curr_value = int(input("Enter a number: "))
    curr_value *= 2  # First doubling
    
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value *= 2  # Keep doubling
    
    print(curr_value)  # Print the last value which is >= 100

# Python file to call the main() function.
if __name__ == '__main__':
    main()
