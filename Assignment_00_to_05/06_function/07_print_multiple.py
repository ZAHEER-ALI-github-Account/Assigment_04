def print_multiple(message, repeats):
    print(message * repeats)  # Print message repeated `repeats` times

def main():
    message = input("Please type a message: ")  # Get message from user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get number of repetitions
    print_multiple(message + " ", repeats)  # Add space for correct formatting

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
