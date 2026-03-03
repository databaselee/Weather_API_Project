import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data.")
        try:
            error_data = response.json()
            print(f"Details: {error_data.get('message', error_data)}")
        except Exception:
            print(f"HTTP Status: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
