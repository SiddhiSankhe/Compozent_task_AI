import requests

def get_weather(city_name, api_key):
    # API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters to send with the request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  
    }
    
    # Make the request
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse JSON data
        city = data.get("name")
        temperature = data["main"].get("temp")
        weather_description = data["weather"][0].get("description")
        humidity = data["main"].get("humidity")
        
        # Display the details
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Failed to get weather data. Error code: {response.status_code}")

api_key = "9096607fe6320626da9d9428614c645b"
city_name = input("Enter the city name: ")

get_weather(city_name, api_key)
