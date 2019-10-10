from flask import Flask, Blueprint, request, make_response, jsonify
import requests
import json
import os

silva_api = Blueprint('api', __name__)

BASE_URL = 'https://silvadev.service-now.com/api/now/table/x_inpgh_upmx_business_application?sysparm_query=external_id='
user = os.getenv('DEV_USERNAME')
password = os.getenv('DEV_PASSWORD')


@silva_api.route('/', methods=['POST'])
def getAppid():
    idinfo = request.json['appID']
    getIdinfo = requests.get(BASE_URL + '{}' .format(idinfo), auth=(user, password))
    result = getIdinfo.json()

    if result['result'] != []:
        return { 'result': True }
    else:
        return { 'result': False,  'message': "Id-{} not found" .format(idinfo) }
