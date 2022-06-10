import os
import requests
from pprint import pprint


def main():
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

    if bearer_token:
        get_data('0123A8032A74EA58FF', bearer_token)


def get_data(device_id, token):
    url = f'https://dashboard.cphsense.com/api/v2/devices/{device_id}/data'
    r = requests.get(url, headers={"Authorization": token})
    response = r.json()
    pprint(response)
    breakpoint()


if __name__ == "__main__":
    main()

