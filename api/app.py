import hashlib
import json
import os
from datetime import datetime
import random
import socket
import time
import requests
from string import ascii_lowercase

from flask import (Flask, jsonify, redirect, render_template, request, session, url_for)
from influxdb import InfluxDBClient


app = Flask(__name__)

redirect_url = os.getenv("redirect_url", "http://146.148.75.164/")

dbname = 'player_status_test'

def write_influx(signature):
    json_body = [
        {
            "measurement": "pir_sensor_reading",
            "tags": {
                "host": "server01",
                "day": datetime.today().weekday()
            },
            "time": str(datetime.now().isoformat(timespec='seconds')),
            "fields": {
                "signature": signature # PIR Sensor reading
                # "string_value": "temp",
                # "bool_value": bool(random.getrandbits(1)) # remove this garbage
            }
        }
    ]
    print(json_body)
    print("Write points: {0}".format(json_body))
    client.write_points(json_body)

# If not Windows (If we're running in kubernetes)
if "nt" not in os.name:
    # dbname = 'player_status_test'
    client = InfluxDBClient("influxdb.monitoring", "8086", "root", "root", dbname)


@app.route("/api/pir_reading", methods=['POST'])
def pir_reading():
    print("pir")
    content = request.json
    write_influx(content["value"])
    return "temp"


@app.route("/")
@app.route("/index")
@app.route("/login")
def index():
    return redirect(redirect_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
