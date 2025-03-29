def main():
    phonebook = {}  # Dictionary to store names and phone numbers

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":  # Add Contact
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"{name} added successfully!")

        elif choice == "2":  # View Contact
            name = input("Enter contact name to search: ")
            if name in phonebook:
                print(f"{name}: {phonebook[name]}")
            else:
                print(f"{name} not found in phonebook.")

        elif choice == "3":  # Delete Contact
            name = input("Enter contact name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"{name} deleted successfully!")
            else:
                print(f"{name} not found.")

        elif choice == "4":  # Show All Contacts
            if phonebook:
                print("\nPhonebook Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty.")

        elif choice == "5":  # Exit
            print("Exiting Phonebook. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 5.")

if __name__ == '__main__':
    main()
