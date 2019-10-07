from fnapi.routes.api import json_api

def init_app(app):
    app.register_blueprint(json_api, url_prefix='/')
