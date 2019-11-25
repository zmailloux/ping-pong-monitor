import json
import os
import random
from datetime import datetime
import flask_login
from flask import (Blueprint, flash, jsonify, redirect, render_template, request, session, url_for)
from influxdb import InfluxDBClient
from utils.activity import (add_login_activity, add_user_activity, get_user_activity, load_json_file)

api_view = Blueprint('api_view', __name__)
api_view.app_template_filter()
dbname = 'player_status_test'

# If not Windows (If we're running in kubernetes)
if "nt" not in os.name:
    # dbname = 'player_status_test'
    client = InfluxDBClient("influxdb.monitoring", "8086", "root", "root", dbname)


@api_view.route("/api/pir_reading", methods=['POST'])
def pir_reading():
    content = request.json
    write_influx(content["value"])
    return "temp"


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


@api_view.route('/api/metadata', methods=['GET'])
def get_metadata():
    user_data = get_user_activity()
    output = {"user_data": user_data}
    return jsonify(output)

@api_view.route('/api/player_present', methods=['GET'])
def get_player_present():
    # False by default
    player_present = False
    result = client.query('SELECT moving_average("signature", 20) FROM "pir_sensor_reading" WHERE ("host" = \'server01\') AND time >= now() - 5m')
    point = list(result.get_points(measurement='pir_sensor_reading')).pop()
    if point['moving_average'] >= 50:
        player_present = True
    point['player_present'] = player_present
    return str(point)


# @api_view.route('/api/status', methods=['GET'])
# def get_status():
#     result = client.query('SELECT last("signature") FROM "pir_sensor_reading" WHERE ("host" = \'server01\')')
#     print("Result: {0}".format(result))
#     return "Result: {0}".format(result)


# @api_view.route('/api/rolling_average', methods=['GET'])
# def get_rolling_average():
#     result = client.query('SELECT moving_average("signature", 20) FROM "pir_sensor_reading" WHERE ("host" = \'server01\') AND time >= now() - 5m')
#     points = list(result.get_points(measurement='pir_sensor_reading'))
#     return "Latest Rolling Average: {0}".format(points.pop())

# @api_view.route('/api/feedback', methods=['GET', 'POST'])
# def set_feedback():
#     content = request.data
#     str_content = str(content.decode("utf-8"))
#     feedback = {"user": session['user'], "time": time.asctime(time.localtime(time.time())), "feedback": str_content}
#     f = open("static_resources/activity/feedback.json", "a+")
#     f.write(str(feedback))
#     f.close()
#     return content


# @api_view.route('/api/get_feedback', methods=['GET'])
# def get_feedback():
#     feedback_file = open("static_resources/activity/feedback.json", "r")
#     content = feedback_file.read()
#     feedback_file.close()
#     return content
