#!/bin/bash
docker build -t ping-pong-dashboard .
docker tag ping-pong-dashboard gcr.io/verdant-future-257013/ping-pong-dashboard:latest
docker push gcr.io/verdant-future-257013/ping-pong-dashboard:latest

kubectl apply -f deployment.yml

kubectl scale deployment ping-pong-dashboard --replicas=0
sleep 1
kubectl scale deployment ping-pong-dashboard --replicas=1