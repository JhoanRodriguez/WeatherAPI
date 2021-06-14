from flask import Flask, request, jsonify
from flask_caching import Cache
from flask_cors import CORS
from utilities.queryToApi import query_to_api
from utilities.formatData import format_data


cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

app = Flask(__name__)
cache.init_app(app)
CORS(app)


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', default='Bogota', type=str)
    country = request.args.get('country', default='CO', type=str)
    response = []
    response.append(get_and_format_data(city, country))

    if 'message' in response[0]:
        return jsonify({'Response': response[0]}), response[0]['cod']

    return jsonify({'Response': response[0]}), 200


@cache.memoize(timeout=120)
def get_and_format_data(city, country):
    """Func used for cache

    Args:
        city ([string])
        country ([string]): Country Code

    Returns:
        [string]: json
    """
    dataFromApi, status_code = query_to_api(city, country)
    if status_code == 200:
        finalData = format_data(dataFromApi)
        return finalData

    return dataFromApi


if __name__ == "__main__":
    app.run(debug=True)
