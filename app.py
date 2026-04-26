from datetime import datetime

from flask import Flask
import requests



def get_location():
    # start up
    # init the api keys needed and the application and global VARs
    # location VARs
    city = ""
    state = ""
    country = ""

    # weather API (OpenWeather API key)
    # get city, state and country info
    city = input("Please enter the name of your city: ")
    state = input("Please enter the name of your state: ")
    country = input("Please enter the name if your country: ")

    weather_API = ""
    weather_API = input("Please enter your OpenWeather: ")

    r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={weather_API}")
    response = r.text

    lat = ""
    lon = ""
        
    # Store the API data 
    response = r
    data = response.json()
    city1 = data[0]

    if response:
        # store the latitudes and longetitudes
        lon = city1["lon"]
        lat = city1["lat"]
    
    print(f"lat: {lat}")
    print(f"log: {lon}")

    return lat, lon, weather_API


def get_temp(lat, lon, weather_API):
    # calling the OpenWeather API to get the temperature
    r1 = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_API}")
    data1 = r1.json()
    print(data1)
    
    # store the temperature in VARs
    temp1 = data1["main"]["temp"]

    print(temp1)
    return temp1


def get_weather(lat, lon, weather_API):
    # calling the OpenWeather API to get the temperature
    r1 = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_API}")
    data1 = r1.json()
    print(data1)
    
    # store weather in a VAR
    weather = data1["weather"][0]["description"]

    print(weather)
    return weather

# get time in a function
def get_time():
    time = datetime.now().strftime("%H:%M")

    print(time)
    return time


# getting all the VARs stored with the Parsed returned data to display on the widgets
lat, lon, weather_API = get_location()
temp1 = get_temp(lat, lon, weather_API)
weather = get_weather(lat,lon, weather_API)
time = get_time()



# setting up the web app 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"""
    <p>Hello, World!</p>
    <H4>Temperature</H4>
    {round(temp1 - 273.15, 1)}
    
    <H4>weather</H4>
    {weather}

    <H4>Time</H4>
    {time}    
    """
