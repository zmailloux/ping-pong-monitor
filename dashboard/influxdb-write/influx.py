# -*- coding: utf-8 -*-
"""Tutorial on using the InfluxDB client."""
from influxdb import InfluxDBClient
import time
from datetime import datetime
import random

def main(host='influxdb.monitoring', port=8086):
    dbname = 'player_status_test'
    client = InfluxDBClient(host, port, "root", "root", dbname)

    while True:
        json_body = [
            {
                "measurement": "pir_sensor_reading",
                "tags": {
                    "host": "server01",
                    "day": datetime.today().weekday()
                },
                "time": str(datetime.now().isoformat(timespec='seconds')),
                "fields": {
                    "signature": random.randint(0,100), # PIR Sensor reading
                    "string_value": "temp",
                    "bool_value": bool(random.getrandbits(1))
                }
            }
        ]
        print(json_body)
        print("Write points: {0}".format(json_body))
        client.write_points(json_body)
        time.sleep(5)



if __name__ == '__main__':
    main()