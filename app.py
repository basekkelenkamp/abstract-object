import json
import os
import requests
from pprint import pprint
from flask import Flask, render_template, session, redirect, request, url_for

from data_extractor import DataExtractor

os.environ["FLASK_APP"] = "app.py"
app = Flask(__name__)


@app.route("/")
def index():
    return json.dumps(data_handler())


def data_handler():
    url = "https://dashboard.cphsense.com/api/v2/auth/new"
    value = {
          "username": "basekkelenkamp1@gmail.com",
          "password": os.getenv("PASSWORD"),
        }

    # POST request for json json data
    bearer_token = ''
    try:
        r = requests.post(url, json=value)
        response = r.json()
        bearer_token = f'Bearer {response["access_token"]}'

    except Exception as e:
        pprint(f"Could not fetch data. {e}")
        exit()

    return get_data('0123A8032A74EA58FF', bearer_token)


def get_data(device_id, token):
    url = f'https://dashboard.cphsense.com/api/v2/devices/{device_id}/data'
    r = requests.get(url, headers={"Authorization": token})
    response = r.json()
    pprint(response)
    extractor = DataExtractor(response, ['co2', 'pm2.5'])

    return response


def get_latest_data(device_id, token):
    url = f'https://dashboard.cphsense.com/api/v2/devices/{device_id}/latest'
    r = requests.get(url, headers={"Authorization": token})
    response = r.json()
    pprint(response)
    extractor = DataExtractor(response, ['co2', 'pm2.5'])

    return response


if __name__ == "__main__":
    app.run(debug=True, port=5000)
