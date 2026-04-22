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

r =requests.get(F"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={weather_API}")
response = r.text

lat = ""
lon = ""

print(response)
    
    
# Store the API data 

print(r.json())



# setting up the web app 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
