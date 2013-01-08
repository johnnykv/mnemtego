import requests
from canari.config import config


def query(query):
    full_url = config['mnemosyne/api_url'] + query
    #TODO: Check for errors
    response = requests.get(full_url)
    return response.json()
