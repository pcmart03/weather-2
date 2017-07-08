"""This module contains a base class for formatting forecasts"""

from texttable import Texttable


class weather_formatter(object):
    """A base class for formatting forecasts

    Arguments: forecast_type = current, hourly, or daily
                        data: = arraycontaining the weather data points
    """
    def __init__(self, forecast_type, data):
        self.type = forecast_type
        self.data = data

    def format_time_period(self, timestamp):
        """Overide in subclasses"""
        return timestamp

    def drawforecast(self):
        header = [self.type, "Temp", "Summary", "Chance Perciptation"]
