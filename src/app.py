from flask import Flask, request, jsonify
from dotenv import load_dotenv
from utilities.degToCompass import degToCompass
from utilities.beaufort_scale import wind_beaufort_scale
import os
import requests
import datetime
import json

# Fetch env vars
load_dotenv()
BASE_URL = os.environ['BASE_API_URL']
appid = os.environ['API_KEY']


app = Flask(__name__)


def QueryToApi(city, country):
    """
    Function for getting the data from the Weather API

    Args:
        city ([string])
        country ([string])

    Returns:
        [string]: json
    """
    URL = BASE_URL + '/weather?q=' + city + ',' + country + '&appid=' + appid
    dataFromApi = requests.get(URL)
    dataFromApi = json.loads(dataFromApi.text)
    return dataFromApi


def formatData(data):
    newData = {
        "location_name": "",
        "temperature": "",
        "wind": "",
        "cloudiness": "",
        "pressure": "",
        "humidity": "",
        "sunrise": "",
        "sunset": "",
        "geo_coordinates": "",
        "requested_time": "",
        "forecast": []
    }
    # Making the convertion of units and formats
    Name = f"{data['name']},{data['sys']['country']}"
    Temperature = f"{data['main']['temp'] - 273 :.2f} °C"
    Wind = f"{wind_beaufort_scale(data['wind']['speed'])},{data['wind']['speed']} m/s, {degToCompass(data['wind']['deg'])}"
    Cloudiness = data['weather'][0]['description']
    Pressure = f"{data['main']['pressure']} hpa"
    Humidity = f"{data['main']['humidity']}%"
    Sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    Sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    Geo_coordinates = f"[{data['coord']['lat']:.2f}, {data['coord']['lon']:.2f}]"
    Requested_time = datetime.datetime.fromtimestamp(data['dt'])

    # Update of the newData dict
    newData['location_name'] = Name
    newData['temperature'] = Temperature
    newData['wind'] = Wind
    newData['cloudiness'] = Cloudiness
    newData['pressure'] = Pressure
    newData['humidity'] = Humidity
    newData['sunrise'] = Sunrise.strftime('%H:%M')
    newData['sunset'] = Sunset.strftime('%H:%M')
    newData['geo_coordinates'] = Geo_coordinates
    newData['requested_time'] = Requested_time.strftime('%Y-%m-%d %H:%M:%S')

    return newData


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', default='Bogota', type=str)
    country = request.args.get('country', default='CO', type=str)
    response = []
    dataFromApi = QueryToApi(city, country)
    finalData = formatData(dataFromApi)
    response.append(finalData)
    return jsonify({'response_items': response}), 200


if __name__ == "__main__":
    app.run(debug=True)
