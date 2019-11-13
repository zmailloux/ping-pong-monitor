# Python Motion Detection Application
The application currently uses a PIR motion sensor to detect changes in infrared motion from 2-8ft away. This data is then sent to an API that injects the data into a timeseries database that will be used to display the results.

## Dependencies:
* Python3.6+

## Setup:
* Run `python3 -m pip install -r requirements.txt`
* Run `python3 motion_detector_pir_active.py`

## PIR Sensor Resources:
https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/
https://thepihut.com/blogs/raspberry-pi-tutorials/raspberry-pi-gpio-sensing-motion-detection
https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor
https://www.raspberrypi.org/forums/viewtopic.php?t=157105

## Auto Start Python Script:
https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/