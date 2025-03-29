def main():
    # Prompt user for input in feet
    feet = float(input("Enter the length in feet: "))

    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12

    # Print the result with correct singular/plural form
    unit = "foot" if feet == 1 else "feet"
    print(f"{feet} {unit} is equal to {inches} inches.")

# Call the main function
if __name__ == '__main__':
    main()
