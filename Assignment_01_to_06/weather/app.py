import requests

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city, api_key):
    # OpenWeatherMap API endpoint for current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Make the request to the API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract necessary details from the response
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        # Print the weather details
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
    else:
        print(f"Error: Could not retrieve weather data for {city}. Please check the city name or try again later.")

# Main function to drive the program
def main():
    api_key = "e1ccda538bcda62fd802c525d30efe50"  
    
    # Ask the user for the city name
    city = input("Enter the city name: ")
    
    # Call the function to get weather data for the given city
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
