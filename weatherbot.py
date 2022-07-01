import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):


    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Cloudy \U00002601",
        "Rain": "Rain \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Fog \U0001F32B"
    }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_discription = data["weather"][0]["main"]
        if weather_discription in code_to_smile:
            wd = code_to_smile[weather_discription]
        else:
            wd = "Loot at window, I cant figure out what is going on there"

        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}***\n"
              f"The weather in city: {city}\nTemperature: {cur_weather} C {wd}\n"
              f"Humidity: {humidity} %\nWind: {wind} m/c\nSunrise: {sunrise_timestamp} a.m.\n"
              f"Sunset: {sunset_timestamp} p.m.\nDay lenght: {lenght_of_the_day}\n"
              f"Have a good day!"
              )
    except Exception as ex:
        print(ex)
        print("Check you city name")

def main():
    city = input("What is your city? ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()