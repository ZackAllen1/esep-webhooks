import os
import requests

def lambda_handler(event, context):
    message = "Issue Created: " + event['issue']['html_url']
    url = os.environ.get('SLACK_URL')
    response = requests.post(url, json = {"text":message})
    return response.text
