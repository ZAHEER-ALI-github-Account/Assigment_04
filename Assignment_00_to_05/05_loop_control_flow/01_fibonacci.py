def main():
    MAX_VALUE = 10000  # Maximum value for Fibonacci sequence
    fib1, fib2 = 0, 1  # First two Fibonacci numbers

    print(fib1, end=" ")
    while fib2 < MAX_VALUE:
        print(fib2, end=" ")
        fib1, fib2 = fib2, fib1 + fib2  # Update Fibonacci numbers

if __name__ == '__main__':
    main()
