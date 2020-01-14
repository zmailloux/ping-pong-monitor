import time
import os
import requests
from gpiozero import MotionSensor

# Ping pong server address and port (if needed)
server_address = os.getenv("server_address", "http://myaddresshere:5000")

# Counters and values
motion_event = 0
previously_in_motion = True
initial_notify_inactivity_freq = 10
notify_inactivity_counter = 0
notify_inactivity_freq = 5

# PIR Sensor Settings
pin = 4
sensitivity_threshold = 0.20

pir = MotionSensor(pin, threshold=sensitivity_threshold)

print("Started")
print(pir.pin)

while True:
    # Every second of activity, send a API call to our server
    if pir.motion_detected:
        previously_in_motion = True
        motion_event += 1
        notify_inactivity_counter = 0
        try:
            r = requests.post(f"{server_address}/api/pir_reading", json={"value": 100})
            print(f"Motion event #{motion_event} sent, status: {r.status_code}")
        except:
            print("error")
        time.sleep(1)
    else:
        notify_inactivity_counter += 1
        # Every time we've gone without activity for more than `notify_inactivity_freq` seconds, send an API call.
        # We do this because we don't have a lot of faith in the sensor and frequency at which we gather data.
        # It allows us to ignore a period of breif inactivity being sent to the server.
        if notify_inactivity_counter >= notify_inactivity_freq and not previously_in_motion:
            try:
                r = requests.post(f"{server_address}/api/pir_reading", json={"value": 0})
                print(f"No motion sent, status: {r.status_code}")
                notify_inactivity_counter = 0
            except requests.RequestExeception as e:
                print(e)

        if notify_inactivity_counter >= initial_notify_inactivity_freq and previously_in_motion:
            try:
                r = requests.post(f"{server_address}/api/pir_reading", json={"value": 0})
                print(f"First submission of no motion sent, status: {r.status_code}")
                previously_in_motion = False
            except requests.RequestExeception as e:
                print(e)
        time.sleep(1)