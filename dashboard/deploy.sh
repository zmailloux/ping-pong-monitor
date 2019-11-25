#!/bin/bash
docker build -t dashboard-app .
docker tag dashboard-app gcr.io/verdant-future-257013/dashboard-app:latest
docker push gcr.io/verdant-future-257013/dashboard-app:latest

kubectl scale deployment dashboard-app --replicas=2
sleep 1
kubectl scale deployment dashboard-app --replicas=1