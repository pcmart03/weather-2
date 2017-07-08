"""Module for making weather requests"""

import json
import sys
import requests
import geocoder
import settings


class NewForecast(object):
    """A class for creating new forecasts

    Arguments: city = name of forecast city
                       units = "imperial" or "metric" default is imperial
    """

    def __init__(self, city=settings.DEFAULT_CITY, units="imperial"):
        """Intialize forecast."""
        self.base_url = settings.BASE_URL
        self.api_key = settings.API_KEY
        self.location = geocoder.google(city)
        self.lat_lng = self.location.latlng
        if units == "imperial":
            self.units = "us"
        else:
            self.units = "si"

        self.forecast = self._make_forecast_request()

    def _make_forecast_request(self):
        """Retrieve forecast from API."""
        payload = {
            "exclude": "minutely,alerts,flags",
            "units": self.units
            }

        corodinates = ",".join(map(str, self.lat_lng))

        url = "{url}{api_key}/{lat_lng}".format(
            url=self.base_url,
            api_key=self.api_key, lat_lng=corodinates)

        try:
            forecast = requests.get(url, params=payload)
            forecast.raise_for_status()
            return json.loads(forecast.text)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    def get_weather(self):
        """Returns complete forecast."""
        return self.forecast

    def get_current(self):
        """Returns current weather."""
        return self.forecast['currently']

    def get_daily(self):
        """Returns daily forcast."""
        return self.forecast['daily']["data"]

    def get_hourly(self):
        """Returns hourly forecast."""
        return self.forecast['hourly']["data"]
