def add_three_copies(lst, data):
    """Adds three copies of data to the given list."""
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    # Get user input
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Print before modification
    print("List before:", my_list)

    # Call the function (modifies the list in place)
    add_three_copies(my_list, message)

    # Print after modification
    print("List after:", my_list)

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
