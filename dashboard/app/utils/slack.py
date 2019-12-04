import json
import time
import requests
import os

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = os.getenv('slack_webhook')


def notify_slack(msg):
    current_time = time.asctime(time.localtime(time.time()))
    slack_data = {
        'channel': '#test-alerts',
        'icon_emoji': 'ping-pong',
        'username': 'Ping Pong Dashboard v0.1.2',
        'text': msg
    }
    send_slack_message(slack_data)


def send_slack_message(slack_data):
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )