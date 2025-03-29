def get_first_element(lst):
    """Prints the first element of the given list."""
    print("First element:", lst[0])

def main():
    # Initialize an empty list
    my_list = []

    # Get list size from user
    n = int(input("Enter the number of elements in the list: "))

    # Get list elements from user
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        my_list.append(element)

    # Call the function to print the first element
    get_first_element(my_list)

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()