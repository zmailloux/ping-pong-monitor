import requests
import time
from datetime import datetime
import random

def spoof_pir_sensor(previous_signature):
    stop_start_chance = random.randint(0, 10)
    # 10% odds someone started or left.
    if stop_start_chance > 9:
        previous_signature = abs(previous_signature - 100)


    if (previous_signature < 50):
        return random.randint(0, 50)
    else:
        return random.randint(50, 100)

def main():
    previous_signature = 0
    while True:
        new_signature = spoof_pir_sensor(previous_signature)
        data = {"value": new_signature}
        r = requests.post(url = "http://34.69.249.145:5000/api/pir_reading", json = data) 
        previous_signature = new_signature
        time.sleep(5)

if __name__ == '__main__':
    main()