def main():
    MIN_HEIGHT = 50  # Minimum height requirement

    while True:
        height = input("How tall are you? (Press enter to exit) ")

        if height == "":  # Stop if user enters nothing
            print("Goodbye!")
            break

        height = float(height)  # Convert input to float

        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
