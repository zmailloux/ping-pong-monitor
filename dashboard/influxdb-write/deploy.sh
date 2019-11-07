#!/bin/bash
docker build -t influx-app .
docker tag influx-app gcr.io/verdant-future-257013/influx-app:latest
docker push gcr.io/verdant-future-257013/influx-app:latest

kubectl scale deployment influx-app --replicas=0
sleep 3
kubectl scale deployment influx-app --replicas=1