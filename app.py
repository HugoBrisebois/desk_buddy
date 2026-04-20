from flask import Flask
import requests


# start up
# init the api keys needed and the application and global VARs

# location VARs
city = ""
state = ""
country = ""

# Requests VARs

limit = 1

r =requests.get(F"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={API key}")



# weather API (OpenWeather API key)
# get city, state and country info
city = input("Please enter the name of your city: ")
state = input("Please enter the name of your state: ")
country = input("Please enter the name if your country: ")

weather_API = ""
weather_API = input("Please enter your OpenWeather: ")




# setting up the web app 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
