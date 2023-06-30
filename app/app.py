# app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key

@app.route('/weather/<city>')
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
        return jsonify(weather)
    else:
        error_message = {'error': 'Weather information not available'}
        return jsonify(error_message), 404

if __name__ == '__main__':
    app.run(debug=True)
