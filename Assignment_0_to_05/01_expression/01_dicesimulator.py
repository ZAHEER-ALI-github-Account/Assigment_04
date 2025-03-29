import random  # Importing the random module to generate random numbers

def roll_dice():
    """Function to roll a single die (returns a number between 1 and 6)."""
    return random.randint(1, 6)

def main():
    # Rolling two dice three times
    for i in range(3):
        die1 = roll_dice()  # First die roll
        die2 = roll_dice()  # Second die roll
        
        # Printing the results of the current roll
        print(f"Roll {i + 1}: Die 1 = {die1}, Die 2 = {die2}")

# Calling the main function
if __name__ == '__main__':
    main()
