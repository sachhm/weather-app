"""
location.py

Get location from ip using ipfy and ipapi api 
Code from: https://www.freecodecamp.org/news/how-to-get-location-information-of-ip-address-using-python/
"""

import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }
    return location_data


print(get_location())
