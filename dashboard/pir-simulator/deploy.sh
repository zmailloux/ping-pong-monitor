#!/bin/bash
docker build -t pir-app .
docker tag pir-app gcr.io/verdant-future-257013/pir-app:latest
docker push gcr.io/verdant-future-257013/pir-app:latest

#kubectl apply -f pir-deployment.yml

kubectl scale deployment pir-app --replicas=0
sleep 3
kubectl scale deployment pir-app --replicas=1