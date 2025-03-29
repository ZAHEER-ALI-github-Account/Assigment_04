def main():
    values = []  # Initialize an empty list

    while True:
        value = input("Enter a value: ")  # Prompt user for input

        if value == "":  # Stop when user presses enter without input
            break
        
        values.append(value)  # Add value to list

    print("Here's the list:", values)  # Print final list

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
