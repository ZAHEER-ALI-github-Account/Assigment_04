def main():
    for num in range(10, 20):  # Loop from 10 to 19
        if num % 2 == 0:
            print(f"{num} even", end=" ")
        else:
            print(f"{num} odd", end=" ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
