#!/bin/bash
docker build -t ping-pong-api .
docker tag ping-pong-api gcr.io/verdant-future-257013/ping-pong-api:latest
docker push gcr.io/verdant-future-257013/ping-pong-api:latest

kubectl apply -f deployment.yml

kubectl scale deployment ping-pong-api --replicas=0
sleep 1
kubectl scale deployment ping-pong-api --replicas=1