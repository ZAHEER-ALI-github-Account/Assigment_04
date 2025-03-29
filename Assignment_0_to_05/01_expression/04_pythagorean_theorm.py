import math  # Import math module for square root function

def main():
    # Prompt user for the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    # Print the result
    print(f"\nThe length of BC (the hypotenuse) is: {bc}")

# Call the main function
if __name__ == '__main__':
    main()
