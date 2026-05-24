from datetime import datetime
from flask_apscheduler import APScheduler
from flask import Flask, render_template, request, redirect, url_for
import requests
from typing import Any
# Global time variable updated by the scheduler
current_time = datetime.now().strftime("%H:%M")

# In-memory config store
config: dict[str, Any] = {
    "lat": None,
    "lon": None,
    "weather_API": None,
    "temp": None,
    "weather": None,
}


def fetch_location(city, state, country, weather_API):
    r = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct"
        f"?q={city},{state},{country}&limit=1&appid={weather_API}"
    )
    data = r.json()
    if not data:
        return None, None
    city1 = data[0]
    return city1["lat"], city1["lon"]


def get_weather_data(lat, lon, weather_API):
    """Fetch temp and description in a single API call."""
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={weather_API}"
    )
    data = r.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return temp, description


# App and scheduler setup
app = Flask(__name__)
scheduler = APScheduler()


@scheduler.task('interval', id='update_time', seconds=30, misfire_grace_time=30)
def update_time():
    global current_time
    current_time = datetime.now().strftime("%H:%M")
    print(f"Scheduler tick: {current_time}")


@scheduler.task('interval', id='update_weather', seconds=3600, misfire_grace_time=60)
def update_weather():
    if config["lat"] is not None:
        config["temp"], config["weather"] = get_weather_data(
            config["lat"], config["lon"], config["weather_API"]
        )
        print(f"Weather updated: {config['temp']}K, {config['weather']}")


@app.route('/')
def index():
    if config["lat"] is None:
        return redirect(url_for('setup'))
    return render_template(
        'index.html',
        time_of_day=current_time,
        temp=config["temp"],
        weather=config["weather"],
    )


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    error = None
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        state = request.form.get('state', '').strip()
        country = request.form.get('country', '').strip()
        weather_API = request.form.get('weather_api', '').strip()

        if not all([city, state, country, weather_API]):
            error = "All fields are required."
        else:
            lat, lon = fetch_location(city, state, country, weather_API)
            if lat is None:
                error = "Location not found. Check your city/state/country and try again."
            else:
                config["lat"] = lat
                config["lon"] = lon
                config["weather_API"] = weather_API
                config["temp"], config["weather"] = get_weather_data(lat, lon, weather_API)
                return redirect(url_for('index'))

    return render_template('setup.html', error=error)


if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)