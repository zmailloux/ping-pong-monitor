# ping-pong-monitor
A collection of applications responsible for letting us know if the ping pong table is currently being used.

## The Problem:
People currently have to walk all the way to the ping pong table (or take the elevator up here) just to find out someone is already playing, leaving them to wait for the previous players to finish playing.

## The Solution:
We will set up a PIR motion sensor (or webcam) attached to a raspberry pi that will detect motion and then send a signal off to a web server which stores the latest status. This web server would be available at an address like `ping-pong.echo.com` which will then take the value we stored and display something along the lines of "The table is free" or the "The table is currently being used". Now, all of this is just a rough and dirty initial implementation, but with that data we'd then be able to visualize the most common playing times throughout the day, how long the average play session is, etc

## Version 1: PIR Motion Sensor
![Version 1](https://github.com/zmailloux/ping-pong-monitor/blob/master/Ping%20Pong%20Monitor%20-%20V1.png)



## Version 2: Webcam Motion Sensor
This version provides the benefit of **eventually** having a video feed into a grafana dashboard. This version however may face some kick back from HR.
<!-- ![Version 2](https://github.com/zmailloux/ping-pong-monitor/blob/master/Ping%20Pong%20Monitor%20-%20V2.png) -->
![Version 3](https://github.com/zmailloux/ping-pong-monitor/blob/master/Ping%20Pong%20Monitor%20-%20V3.png)
