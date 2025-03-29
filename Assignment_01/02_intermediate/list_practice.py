def main():
    # Problem #1: List Practice
    
    # Create a list called fruit_list that contains the following fruits:
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    print("Length of fruit list:", len(fruit_list))
    
    # Add 'mango' at the end of the list.
    fruit_list.append('mango')
    
    # Print the updated list.
    print("Updated fruit list:", fruit_list)
    
    # Problem #2: Index Game
    
    def access_element(lst, index):
        if 0 <= index < len(lst):
            return lst[index]
        return "Index out of range."
    
    def modify_element(lst, index, new_value):
        if 0 <= index < len(lst):
            lst[index] = new_value
            return "Updated list:", lst
        return "Index out of range."
    
    def slice_list(lst, start, end):
        return lst[start:end] if 0 <= start < len(lst) and 0 <= end <= len(lst) else "Invalid indices."
    
    game_list = ['one', 'two', 'three', 'four', 'five']
    
    while True:
        print("\nChoose an operation: access, modify, slice, or exit")
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == "access":
            index = int(input("Enter index to access: "))
            print(access_element(game_list, index))
        elif choice == "modify":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(game_list, index, new_value))
        elif choice == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(game_list, start, end))
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
