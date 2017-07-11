This is a CLI app for getting current, hourly and seven day forcasts from the [Dark Sky API](https://darksky.net/dev/).

## weather/settings.py
Before using, create a file called settings.py to hold your API key and default city.

    BASE_URL = "https://api.darksky.net/forecast/"
    API_KEY = "YOURAPIKEY"
    DEFAULT_CITY = "Washington, DC"

### Usage

`weather current` Returns current weather conditions

`weather hourly` Returns the hourly forecast for the next 12 hours

`weather week`  Returns weather for the next seven days

To change the city use the `--city` option. For example:

    weather current --city="Champlin, MN"