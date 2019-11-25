## Install InfluxDB:
Using the InfluxDB Helm chart: https://github.com/helm/charts/tree/master/stable/influxdb
`helm install --namespace monitoring --name influxdb stable/influxdb`

## Install Grafana:
To install the Grafana helm chart, navigate to the grafana directory and run the following command.
`helm install --namespace monitoring --name grafana stable/grafana`