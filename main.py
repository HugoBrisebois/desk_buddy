import datetime
from flask import Flask
import requests

# init flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello, World!"

hello_world()