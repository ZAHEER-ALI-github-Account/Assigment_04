def main():
    # Dictionary of fruits with prices per unit
    fruit_prices = {
        "apple": 3.5,
        "grapes": 15.0,
        "orange": 20.0,
        "kiwi": 2.5,
        "watermelon": 5.0,
        "mango": 7.0
    }

    total_cost = 0  # Variable to store the total cost

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity < 0:
                    print("Please enter a valid non-negative number.")
                else:
                    total_cost += quantity * price
                    break
            except ValueError:
                print("Invalid input! Please enter a number.")

    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
