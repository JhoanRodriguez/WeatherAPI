import datetime
from utilities.degToCompass import deg_to_compass
from utilities.beaufortScale import wind_beaufort_scale


def format_data(data):
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
    Wind = f"{wind_beaufort_scale(data['wind']['speed'])},{data['wind']['speed']} m/s, {deg_to_compass(data['wind']['deg'])}"
    Cloudiness = data['weather'][0]['description']
    Pressure = f"{data['main']['pressure']} hpa"
    Humidity = f"{data['main']['humidity']}%"
    Sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    Sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    Geo_coordinates = f"[{data['coord']['lat']:.2f}, {data['coord']['lon']:.2f}]"
    Requested_time = datetime.datetime.fromtimestamp(data['dt'])

    # Update of the new Data dict
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
