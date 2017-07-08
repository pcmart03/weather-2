"""This module contains a subclass of the WeatherFormatter used for formatting
    the hourly weather it is used for both hourly and current reports
"""
from datetime import datetime

from .formatter import WeatherFormatter


class FormatHourly(WeatherFormatter):
    """A base class for formatting hourly forecasts

    Arguments: forecast_type = current, hourly, or daily
                        data: = arraycontaining the weather data points
    """
    def __init__(self,  data):
        WeatherFormatter.__init__(self, data)

    def format_time_period(self, timestamp):
        """Returns time in format 02:00 PM"""
        time = datetime.fromtimestamp(timestamp)
        return datetime.strftime(time, "%I:%M %p")

