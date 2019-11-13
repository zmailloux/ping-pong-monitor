from flask import Flask,render_template, request, session, redirect, url_for
import flask_login
import os
from prometheus_flask_exporter import PrometheusMetrics
import hashlib
import socket
from random import choice
from string import ascii_lowercase
from influxdb import InfluxDBClient
import time
from datetime import datetime
import random

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
metrics = PrometheusMetrics(app)

dbname = 'player_status_test'
#client = InfluxDBClient("influxdb.monitoring", "8086", "root", "root", dbname)

# static information as metric
# This can set as an environment variable in the deployment that can pull either the container image hash or version
# https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/
metrics.info('app_info', 'Application info', version='0.0.1')

app.config['IMAGES_FOLDER'] = os.path.join('static', 'images')
app.config['STATIC_FOLDER'] = os.path.join('..', 'static_resources')
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
users = {'admin': {'password': '69bc0cc4b50ac0342dfcecdde7091587'}, 'user': {'password': '9e8acc5d49877acdb8837b032b7b9010'}}


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return

    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in users:
        return

    user = User()
    user.id = username

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    encoded_pw = str(hashlib.md5(request.form['password'].encode()).hexdigest())
    user.is_authenticated = encoded_pw == users[username]['password']
    return user


@app.route("/index")
@flask_login.login_required
def index():
    try:
        # host_name = socket.gethostname()
        # host_ip = socket.gethostbyname(host_name)
        #return render_template('index.html', hostname=host_name, ip=host_ip)
        return render_template('index.html')
    except:
        return render_template('error.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():

    #https://github.com/maxcountryman/flask-login
    if request.method == 'GET':
        if not session.get('logged_in'):
            return render_template('login.html')
        else:
            return redirect(url_for('index'))

    username = request.form['username']
    encoded_pw = str(hashlib.md5(request.form['password'].encode()).hexdigest())

    if encoded_pw == users[username]['password']:
        user = User()
        user.id = username
        flask_login.login_user(user)
        session['logged_in'] = True
        return redirect(url_for('index'))

    return 'Bad login'

@app.route('/')
def main():
    return "Welcome to the Echo Ping Pong Dashboard"


@app.route("/api/pir_reading", methods=['POST'])
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
                "signature": signature, # PIR Sensor reading
                "string_value": "temp",
                "bool_value": bool(random.getrandbits(1))
            }
        }
    ]
    print(json_body)
    print("Write points: {0}".format(json_body))
    client.write_points(json_body)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
