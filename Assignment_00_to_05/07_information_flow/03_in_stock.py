# Fruit inventory dictionary
inventory = {
    "apple": 50,
    "banana": 30,
    "pear": 1000,
    "orange": 25,
    "grape": 200
}

def num_in_stock(fruit):
    """Returns the number of the given fruit in stock, or 0 if not available."""
    return inventory.get(fruit.lower(), 0)  # Convert to lowercase for case insensitivity

def main():
    fruit = input("Enter a fruit: ").strip()  # Get user input and remove extra spaces
    stock = num_in_stock(fruit)  # Get stock count

    if stock > 0:
        print("This fruit is in stock! Here is how many:\n", stock)
    else:
        print("This fruit is not in stock.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
