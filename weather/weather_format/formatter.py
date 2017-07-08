"""This module contains a base class for formatting forecasts"""

from texttable import Texttable


class WeatherFormatter(object):
    """A base class for formatting forecasts

    Arguments: forecast_type = current, hourly, or daily
                        data: = arraycontaining the weather data points
    """
    def __init__(self, data):
        self.data = data
        self.time_period = "Time"

    def format_time_period(self, timestamp):
        """Overide in subclasses Returns formatted date of time for forecast"""
        return timestamp

    def get_percent(self, ratio):
        return "{0:.0f}%".format(ratio * 100)

    def format_temp(self, datapoint):
        return round(datapoint["temperature"])

    def draw_forecast(self):
        """Returns a texttable object containing the forecast."""
        header = [
            self.time_period,
            "Temp", "Summary",
            "Chance Perciptation"
            ]
        row = []
        table = Texttable()

        # table.set_deco(Texttable.HLINES | Texttable.HEADER)
        table.set_cols_align(['l', 'c', 'l', 'c'])
        table.add_row(header)

        for data_point in self.data:
            table.add_row([
                self.format_time_period(data_point["time"]),
                self.format_temp(data_point),
                data_point["summary"],
                self.get_percent(data_point["precipProbability"])
                ])

        return table
