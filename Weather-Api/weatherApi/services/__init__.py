import os
from eventgateway import EventGateway
from pprint import pprint


EG_URL = os.getenv("EG_URL", "http://localhost:4000")
eg = EventGateway(url=EG_URL, space="weather")

if eg.checkConnection():
    print("Connection succesfull")
else:
    print("Issue while connecting")


def init_app(app):
    @app.before_first_request
    def setupEventGateway():
        weatherEndpoint = os.getenv("WEATHER_ENDPOINT", "http://localhost:8080")
        functions = {
        "functionId": "weather-forecasts",
        "type": "http",
        "provider": {
            "url": "{}/weather/weather-forecast".format(weatherEndpoint)
                    }
        }
        eventtypes = {
        "name": "http.request"
        }
        subscriptions = {
        "functionId": "weather-forecasts",
        "event": "http",
        "method": "POST",
        "path": "/weather/weather-forecast",
        "eventType": "http.request",
        "type": "sync"
        }
        eg.createEventType(eventtypes)
        eg.createFunction(functions)
        eg.createSubscription(subscriptions)
        pprint(eg.getAllFunction())
        pprint(eg.getAllSubscription())
