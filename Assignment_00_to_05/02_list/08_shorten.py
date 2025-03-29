MAX_LENGTH = 3  # Define the maximum allowed length

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Keep removing items until the length is MAX_LENGTH
        removed_item = lst.pop()  # Remove last element
        print("Removed:", removed_item)  # Print removed element

def main():
    # Example: Getting a list from the user
    user_list = input("Enter a list of elements separated by spaces: ").split()
    
    print("Original list:", user_list)
    shorten(user_list)  # Call the function to modify the list
    print("Final list:", user_list)  # Print the final shortened list

# Required to call the main function
if __name__ == '__main__':
    main()
