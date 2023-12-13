# Flask Jinja Weather App
A simple app to track weather using the Open-Meteo API. It uses IP to determine location.

# About
The app's purpose was to for me to learn more about using APIs and Python, along with the Flask framework. It uses the aformentioned Open-Meteo API for weather tracking, as well as IPFY and IP-API for determining location. 

Right now the app is very basic, and uses datetime to print the current minimum nad maximum temperatures using datetime.

![V1.0](/screenshot/v1.0.png)

# TODO
- Implement forecast for week feature
- Speed up program (one major bottleneck is that the location and weather calls are made every time the home page is loaded)

