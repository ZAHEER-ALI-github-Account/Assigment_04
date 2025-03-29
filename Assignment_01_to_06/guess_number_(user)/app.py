import random

def computer_guesses():
    low, high = 1, 100
    attempts = 0
    
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    
    while True:
        guess = random.randint(low, high)
        attempts += 1
        
        print(f"Is it {guess}? (Enter 'h' if too high, 'l' if too low, 'c' if correct)")
        user_input = input().lower()
        
        if user_input == 'h':
            high = guess - 1
        elif user_input == 'l':
            low = guess + 1
        elif user_input == 'c':
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    computer_guesses()
