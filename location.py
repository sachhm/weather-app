"""
location.py

Get location using ipfy and ip-api
"""

import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
    print(response)
    location_data = {
        "city": response.get("city"),
        "country": response.get("country"),
        "latitude": response.get("lat"),
        "longitude": response.get("lon")
    }
    return location_data


print(get_location())
