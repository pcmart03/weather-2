"""This module contains a subclass of the WeatherFormatter used for formatting
    the daily  weather it is used for both hourly and current reports
"""
from datetime import datetime

from .formatter import WeatherFormatter


class FormatDaily(WeatherFormatter):
    """A base class for formatting daily forecasts

    Arguments: forecast_type = current, hourly, or daily
                        data: = arraycontaining the weather data points
    """
    def __init__(self,  data):
        WeatherFormatter.__init__(self, data)
        self.time_period = "Day"

    def format_time_period(self, timestamp):
        """Returns time in format Mon 02/10"""
        time = datetime.fromtimestamp(timestamp)
        return datetime.strftime(time, "%a %m/%d")
