#!/bin/bash
docker build -t ping-pong-dashboard .
# docker tag ping-pong-dashboard gcr.io/verdant-future-257013/ping-pong-dashboard:latest
# docker push gcr.io/verdant-future-257013/ping-pong-dashboard:latest
docker tag ping-pong-dashboard gcr.io/precise-space-265115/ping-pong-dashboard:latest
docker push gcr.io/precise-space-265115/ping-pong-dashboard:latest

kubectl apply -f deployment.yml

kubectl scale deployment ping-pong-dashboard --replicas=0
sleep 1
kubectl scale deployment ping-pong-dashboard --replicas=1

export SERVICE_IP=$(kubectl get svc --namespace default ping-pong-dashboard-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo "http://$SERVICE_IP:80"
