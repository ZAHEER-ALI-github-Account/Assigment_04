import random

def choose_word():
    words = ["python", "developer", "hangman", "coding", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            print("Good guess!")
            if set(word_to_guess).issubset(guessed_letters):
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
    else:
        print(f"Game over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
