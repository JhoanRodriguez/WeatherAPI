from dotenv import load_dotenv
import os
import requests
import json

# Fetch env vars
load_dotenv()
BASE_URL = os.environ['BASE_API_URL']
appid = os.environ['API_KEY']


def query_to_api(city, country):
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
    status_code = dataFromApi.status_code
    dataFromApi = json.loads(dataFromApi.text)
    return dataFromApi, status_code
