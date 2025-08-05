import os
import requests
from dotenv import load_dotenv
import math

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_sydney_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Sydney&appid={API_KEY}"
    print(url)
    response = requests.get(url)



    if response.status_code == 200:
        kelvin = 273.15
        data = response.json()
        print(data)
        description = data["weather"][0]["description"]
        print(description)
        actual_temp = data["main"]["temp"] - kelvin
        rounded_actual_temp = math.floor( actual_temp * 10)/10
        print(rounded_actual_temp)
        feel_temp = data["main"]["feels_like"] - kelvin
        rounded_feel_temp = math.floor(feel_temp * 10)/10
        print(rounded_feel_temp)
        temp_max = data["main"]["temp_max"] - kelvin
        rounded_temp_max = math.floor(temp_max * 10)/10
        print(rounded_temp_max)
        return f"Sydney weather today: {description}, {rounded_feel_temp}, Max: {rounded_temp_max}"
    else:
        raise f"Failed to fetch weather: {response.status_code}"
