from flask import Flask, request, jsonify
from utilities.query_to_api import QueryToApi
from utilities.format_data import formatData

app = Flask(__name__)


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
