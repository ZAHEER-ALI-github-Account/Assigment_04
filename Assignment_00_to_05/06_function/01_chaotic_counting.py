import random

DONE_LIKELIHOOD = 0.3  # 30% chance to stop counting

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # Stops the function if done() returns True
        print(i, end=" ")  # Print numbers on the same line

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")  # Newline for formatting

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
