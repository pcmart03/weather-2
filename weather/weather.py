"""This module contains the weather CLI"""

from forecast.weather_request import NewForecast
from settings import DEFAULT_CITY
from weather_format.format_daily import FormatDaily
from weather_format.format_hourly import FormatHourly

import click


class Config(object):
    """Creates cli config object"""
    def __init__(self):
        self.city = ""

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--city', default=DEFAULT_CITY, help="Set forecast location")
@pass_config
def cli(config, city):
    """Main cli function.
        Arguments: config = pass_config object
                            city = text, the name of the city of
                                     desired forecast
    """
    config.city = city
    config.weather = NewForecast(config.city)


@cli.command()
@pass_config
def current(config):
    forecast = config.weather.get_current()
    formatted = FormatHourly([forecast])
    table = formatted.draw_forecast()
    click.echo("Current Conditions:")
    click.echo(table.draw())


@cli.command()
@pass_config
def hourly(config):
    forecast = config.weather.get_hourly()
    formatted = FormatHourly(forecast[:12])
    table = formatted.draw_forecast()
    click.echo("Weather for the next twelve hours:")
    click.echo(table.draw())


@cli.command()
@pass_config
def week(config):
    forecast = config.weather.get_daily()
    formatted = FormatDaily(forecast)
    table = formatted.draw_forecast()
    click.echo("Weather for the next week")
    click.echo(table.draw())


if __name__ == "__main__":
    cli()

