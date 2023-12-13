"""
weather.py

Get daily weather and forecast from location.
"""
import openmeteo_requests, location
from datetime import datetime
import pandas as pd
from openmeteo_sdk.Variable import Variable

om = openmeteo_requests.Client()

client_location = location.get_location()
lat = client_location["latitude"]
long = client_location["longitude"]

current_date = datetime.today().strftime('%Y-%m-%d')


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat,
    "longitude": long,
    "timezone": "auto",
    "daily": ["temperature_2m_max", "temperature_2m_min"],
	"timezone": "auto"
}

responses = om.weather_api(url, params=params)
response = responses[0]
print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s"),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min

daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)
current_date = datetime.today().strftime('%Y-%m-%d')
print(f"CHOSEN DATE: {daily_dataframe.loc[['date']] == current_date}")  
