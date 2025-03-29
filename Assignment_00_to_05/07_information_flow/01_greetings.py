def greet(name):
    print(f"Greetings {name}!")

def main():
    name = input("What's your name? ")  # Get the user's name
    greet(name)  # Call the greet function with the user's input

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
