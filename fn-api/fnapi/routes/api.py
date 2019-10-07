from flask import Flask, Blueprint, jsonify, request
import requests
import json

json_api = Blueprint('api', __name__)



@json_api.route('/', methods=['GET'])
def index():
    result = requests.get('https://my-json-server.typicode.com/ShaktiAhad/python/db/')
    r = result.json()
    return r

@json_api.route('/<route>', methods=['GET'])
def route(route):
    result = requests.get('https://my-json-server.typicode.com/ShaktiAhad/python/%s' %str(route))
    r = result.json()
    return {'a':r}

@json_api.route('/<route>/<id>', methods=['GET'])
def hello(route,id):
    result = requests.get('https://my-json-server.typicode.com/ShaktiAhad/python/%s/%d' %(str(route), int(id)))
    r = result.json()

    if r != {}:
       return r
    else:
        return "<h3>ID: %d does not exist</h3>" %int(id)



    
    