# Define the speed of light constant
C = 299792458  # meters per second

def main():
    while True:
        try:
            # Prompt user for mass input
            mass = float(input("Enter kilos of mass: "))
            
            # Calculate energy using E = m * C^2
            energy = mass * C**2
            
            # Print the results
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"{energy} joules of energy!\n")
        
        except ValueError:
            print("Invalid input. Please enter a numerical value for mass.")
        
        # Ask user if they want to continue
        again = input("Would you like to enter another mass? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

# Call the main function
if __name__ == '__main__':
    main()
