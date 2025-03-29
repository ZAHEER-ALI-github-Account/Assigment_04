def main():
    # Prompt user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Display result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
