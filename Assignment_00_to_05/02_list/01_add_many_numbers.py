def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num  # Add each number to total
    return total

def main():
    # Example list of numbers
    numbers_list = [1, 3, 2, 4, 6]
    
    # Call the function and print the result
    result = sum_of_numbers(numbers_list)
    print(f"The sum of the numbers is: {result}")

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
