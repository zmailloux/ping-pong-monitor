# Python Motion Detection Application
Right now the application only detects motion in real time on the graphics pane. We want to take that movement information we gather in real time and ship that off to our web server. Ideally we could have the motion detection script aggregate motion information over a period of 10-60 seconds, determine that there was enough motion activity to qualify as active ping pong play, and have it forward a boolean value off to the dashboard page.

## Dependencies:
* Python3.6+

## Setup:
* Run `python -m pip install -r requirements.txt`
* Run `python motion_detector.py`


## Resources:
https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/