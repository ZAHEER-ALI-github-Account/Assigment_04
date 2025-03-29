def double_numbers(numbers):
    return [num * 2 for num in numbers]  # List comprehension to double each number

def main():
    # Example list of numbers
    numbers = [3, 6, 9, 12]
    
    # Call the function and store the result
    doubled_numbers = double_numbers(numbers)
    
    # Print the updated list
    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled_numbers}")

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
