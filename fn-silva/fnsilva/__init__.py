import warnings
from flask import Flask, jsonify


def page_not_found(e):
    error = {
        "message": "E_NOT_FOUND",
        "status_code": 404
    }
    return jsonify(error), 404


def error_server(e):
    error = {
        "message": "SERVER_ERROR",
        "status_code": 500
    }
    return jsonify(error), 500


def method_not_allowed(e):
    error = {
        "message": "E_NOT_ALLOWED",
        "status_code": 405
    }
    return jsonify(error), 405

def create_app():
    warnings.filterwarnings("ignore")
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, error_server)
    app.register_error_handler(405, method_not_allowed)
    from . import routes
    routes.init_app(app)
    return app






#from flask import Flask

#app = Flask(__name__)

#from fnapi.routes.api import json_api

#app.register_blueprint(json_api, url_prefix='/')