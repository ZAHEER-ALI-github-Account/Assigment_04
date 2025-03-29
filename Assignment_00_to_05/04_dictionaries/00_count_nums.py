def main():
    number_counts = {}  # Dictionary to store occurrences

    while True:
        number = input("Enter a number (or press enter to finish): ")  # Take input
        if number == "":  # Stop when input is empty
            break

        number = int(number)  # Convert input to integer
        if number in number_counts:
            number_counts[number] += 1  # Increment count if exists
        else:
            number_counts[number] = 1  # Add new number with count 1

    # Print the results
    for num, count in number_counts.items():
        print(f"{num} appears {count} times.")

if __name__ == '__main__':
    main()
