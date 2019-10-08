from weatherApi.routes.api import weather_api


def init_app(app):
    app.register_blueprint(weather_api, url_prefix='/')
