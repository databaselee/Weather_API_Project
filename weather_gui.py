import tkinter as tk
from tkinter import messagebox
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
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"Temperature: {temp}°C\nDescription: {desc}"
    else:
        try:
            error_data = response.json()
            return f"Error: {error_data.get('message', error_data)}"
        except Exception:
            return f"HTTP Status: {response.status_code}"

def show_weather():
    city = city_entry.get()
    result = get_weather(city)
    messagebox.showinfo("Weather Result", result)

root = tk.Tk()
root.title("WeatherApp GUI")
root.geometry("300x150")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_btn = tk.Button(root, text="Get Weather", command=show_weather)
get_btn.pack(pady=10)

root.mainloop()
