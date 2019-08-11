from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def hello_docker():
    return 'Version #1 running in docker'

@app.route('/city/<city>')
def get_weather(city):
    weather = get_data(city)
    return render_template("weather.html",city=city, weather=weather)

def get_data(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = os.environ['API_KEY']
    payload = {'q': city +',de', 'appid':api_key , 'units': 'metric'}
    r = requests.get(url, params=payload)
    data = r.json()
    return data['main']

 
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)