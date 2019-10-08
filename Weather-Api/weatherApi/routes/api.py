from flask import Flask, Blueprint, request, render_template
import requests
import json

weather_api = Blueprint('api', __name__)


@weather_api.route('/connection', methods=['POST'])
def temperature():
    city_name = request.form['city']
    # r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',bd&appid=c8748a72a5ad0ec43d336d1afe8b7229')
    url = (
        'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + ',bd&appid=c8748a72a5ad0ec43d336d1afe8b7229')
    json = requests.get(url).json()


    if json == {'cod': '404', 'message': 'city not found'}:
        return {'cod': '404', 'message': 'city not found'}
    else:
        temp_k = (json['main']['temp'])
        temp_c = int(temp_k - 273.15)
        weather = {
        'city': json['name'],
        'temperature': temp_c
                }
    return render_template('connection.html', weather=weather)

@weather_api.route('/')
def index():
    return render_template('head.html')
