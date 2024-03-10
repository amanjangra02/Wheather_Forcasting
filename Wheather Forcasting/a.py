import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',  # You can change to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    if weather_data is None or 'main' not in weather_data:
        print("Weather data not available.")
        return

    main_info = weather_data['main']
    wind_info = weather_data['wind']
    weather_info = weather_data['weather'][0]

    print("\nWeather Information:")
    print(f"City: {weather_data['name']}")
    print(f"Temperature: {main_info['temp']}°C")
    print(f"Humidity: {main_info['humidity']}%")
    print(f"Wind Speed: {wind_info['speed']} m/s")
    print(f"Description: {weather_info['description']}")

def main():
    print("Weather Forecast Application")
    print("---------------------------")

    api_key = input("Enter your OpenWeatherMap API key: ")
    location = input("Enter the name of a city or a zip code: ")

    weather_data = get_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
