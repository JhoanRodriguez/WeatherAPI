from flask import Flask, request, jsonify
from flask_caching import Cache
from utilities.query_to_api import QueryToApi
from utilities.format_data import formatData


cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

app = Flask(__name__)
cache.init_app(app)


@app.route('/weather', methods=['GET'])
@cache.memoize(timeout=120)
def get_weather():
    city = request.args.get('city', default='Bogota', type=str)
    country = request.args.get('country', default='CO', type=str)
    response = []
    dataFromApi = QueryToApi(city, country)
    finalData = formatData(dataFromApi)
    response.append(finalData)
    print('se ejecuto')
    return jsonify({'response_items': response}), 200


if __name__ == "__main__":
    app.run(debug=True)
