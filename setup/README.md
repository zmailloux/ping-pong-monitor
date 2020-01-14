## Install InfluxDB:
Using the InfluxDB Helm chart: https://github.com/helm/charts/tree/master/stable/influxdb
`helm install --namespace monitoring --name influxdb stable/influxdb`
```
NOTES:
InfluxDB can be accessed via port 8086 on the following DNS name from within your cluster:

- http://influxdb.monitoring:8086

You can easily connect to the remote instance with your local influx cli. To forward the API port to localhost:8086 run the following:

- kubectl port-forward --namespace monitoring $(kubectl get pods --namespace monitoring -l app=influxdb -o jsonpath='{ .items[0].metadata.name }') 8086:8086

You can also connect to the influx cli from inside the container. To open a shell session in the InfluxDB pod run the following:

- kubectl exec -i -t --namespace monitoring $(kubectl get pods --namespace monitoring -l app=influxdb -o jsonpath='{.items[0].metadata.name}') /bin/sh

To tail the logs for the InfluxDB pod run the following:

- kubectl logs -f --namespace monitoring $(kubectl get pods --namespace monitoring -l app=influxdb -o jsonpath='{ .items[0].metadata.name }')
```

To create the proper table, run `kubectl exec -i -t --namespace monitoring $(kubectl get pods --namespace monitoring -l app=influxdb -o jsonpath='{.items[0].metadata.name}') /bin/sh` to enter the pod.
The type `influx` to start the interactive shell. Type `CREATE DATABASE player_status_test`. From here you're good to go. You should see that Grafana is able to connect to the data source now.

## Install Grafana:
To install the Grafana helm chart, navigate to the grafana directory and run the following command.
`helm install --namespace monitoring --name grafana stable/grafana`
```
   Get the Grafana URL to visit by running these commands in the same shell:
NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        You can watch the status of by running 'kubectl get svc --namespace monitoring -w grafana'
     export SERVICE_IP=$(kubectl get svc --namespace monitoring grafana -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
     http://$SERVICE_IP:80
```
