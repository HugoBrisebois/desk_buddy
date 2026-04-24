from flask import Flask
import requests
import json


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
    print(city1["lat"])
    print(city1["lon"])

    # store the latitudes and longetitudes
    lon = city1["lon"]
    lat = city1["lat"]
    

print(f"lat: {lat}")
print(f"log: {lon}")

# calling the openweather API to get the temperature
r1 = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_API}")
response1 = r1
data = response1.json()
city1 = data[0]

if response1:
    print(city1["lat"])
    print(city1["lon"])

    # store the latitudes and longetitudes
    lon = city1["lon"]
    lat = city1["lat"]
    

print(f"lat: {lat}")
print(f"log: {lon}")

# store returned temperature
if response1:
    print(temp1["main"])



# setting up the web app 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"""
    <p>Hello, World!</p>
    <H4>Temperature</H4>
    
    """
