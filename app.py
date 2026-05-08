from datetime import datetime
from flask_apscheduler import APScheduler
from flask import Flask, render_template, request, redirect, url_for
import requests

# Global time variable updated by the scheduler
current_time = datetime.now().strftime("%H:%M")

# In-memory config store
config = {
    "lat": None,
    "lon": None,
    "weather_API": None,
    "temp": None,
    "weather": None,
}


def get_location():

    # API request URL
    r = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct"
        f"?q={city},{state},{country}&limit=1&appid={weather_API}"
    )

    data = r.json()
    if not data:
        return None, None
    city1 = data[0]
    return city1["lat"], city1["lon"]


def get_temp(lat, lon, weather_API):
    r1 = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={weather_API}"
    )
    data1 = r1.json()
    temp1 = data1["main"]["temp"]
    return temp1


def get_weather(lat, lon, weather_API):
    r1 = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={weather_API}"
    )
    data1 = r1.json()
    weather = data1["weather"][0]["description"]
    return weather


# App and scheduler setup
app = Flask(__name__)
scheduler = APScheduler()


@scheduler.task('interval', id='update_time', seconds=30, misfire_grace_time=30)
def update_time():
    global current_time
    current_time = datetime.now().strftime("%H:%M")
    print(f"Scheduler tick: {current_time}")


@app.route('/')
def index():
    return render_template('index.html', time_of_day=current_time)


if __name__ == '__main__':
    lat, lon, weather_API = get_location()
    temp1 = get_temp(lat, lon, weather_API)
    weather = get_weather(lat, lon, weather_API)

    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)