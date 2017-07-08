"""This module contains a base class for formatting forecasts"""

from texttable import Texttable


class WeatherFormatter(object):
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

    def get_percent(self, ratio):
        return "{0:.0f}%".format(ratio * 100)

    def drawforecast(self):
        header = [self.type, "Temp", "Summary", "Chance Perciptation"]
        row = []
        table = Texttable()

        table.set_deco(texttable.HEADER)
        table.set_cols_align(['l', 'c', 'l', 'c'])
        table.add_row(header)

        for data_point in self.data:
            table.add_row([
                self.format_time_period(data_point["time"]),
                data_point["temperature"],
                data_point["summary"],
                self.get_percent(data_point["precipProbability"])
                ])

        return table
