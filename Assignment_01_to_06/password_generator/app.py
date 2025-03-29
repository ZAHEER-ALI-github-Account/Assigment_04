import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the length of each password: "))
        
        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            print(generate_password(length))
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()
