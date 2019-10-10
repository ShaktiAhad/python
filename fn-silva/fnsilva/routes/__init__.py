from fnsilva.routes.api import silva_api


def init_app(app):
    app.register_blueprint(silva_api, url_prefix='/')
