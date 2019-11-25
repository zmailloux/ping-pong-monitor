#!/bin/bash

for filename in dashboards/*.json; do
    DASHBOARD_NAME=$(basename "$filename" .json)
    kubectl create configmap dashboard-${DASHBOARD_NAME} --from-file=${filename} -o yaml --dry-run --namespace monitoring | kubectl apply -f -
    kubectl label --overwrite --namespace monitoring configmap dashboard-${DASHBOARD_NAME} grafana_dashboard=1
done
