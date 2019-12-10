import hashlib
import json
import os
import random
import socket
import time
from datetime import datetime
from random import choice
import requests
from string import ascii_lowercase

import flask_login
from flask import (Flask, jsonify, redirect, render_template, request, session, url_for)
from flask_navigation import Navigation
# from influxdb import InfluxDBClient
from prometheus_flask_exporter import PrometheusMetrics

from utils.activity import (add_login_activity, add_user_activity, get_user_activity, load_json_file)
from views.api import api_view
from views.login import login_view, set_login_manager

app = Flask(__name__)
set_login_manager(app)
app.register_blueprint(login_view)
app.register_blueprint(api_view)
metrics = PrometheusMetrics(app)

# https://flask-navigation.readthedocs.io/en/latest/
# https://getbootstrap.com/docs/4.0/components/navbar/
nav = Navigation(app)
nav.Bar('top', [
    nav.Item('Home', 'index')
    # nav.Item('Feedback', 'feedback')
])

# Toggle to just send everything to maintenance
# https://gist.github.com/DazWorrall/3180841
is_maintenance_mode = json.loads(os.getenv("is_maintenance_mode", "False").lower())

build_info = load_json_file("build_info.json")

# static information as metric
# This can set as an environment variable in the deployment that can pull either the container image hash or version
# https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/
metrics.info('app_info', 'Application info', version='0.1.2')

app.config['IMAGES_FOLDER'] = os.path.join('static', 'images')
app.config['STATIC_FOLDER'] = os.path.join('..', 'static_resources')
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# https://stackoverflow.com/questions/35780562/flask-security-unauthorized-callback
@app.login_manager.unauthorized_handler
def unauth_handler():
    return redirect(url_for('login_view.login'))


@app.before_request
def check_for_maintenance():
    if is_maintenance_mode and request.path != url_for('maintenance'): 
        return redirect(url_for('maintenance'))
        # Or alternatively, dont redirect 
        # return 'Sorry, off for maintenance!', 503


@app.route("/health")
def health():
    return "I'm alive"

@app.route("/maintenance")
def maintenance():
    return render_template('maintenance.html')


@app.route("/index")
@flask_login.login_required
def index():
    try:
        # add_user_activity(request.remote_addr, "/index")
        return render_template('index.html', build_info=build_info)
    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
