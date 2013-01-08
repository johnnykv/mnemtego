import request
from urllib.parse import urljoin
from canari.config import config


def query(query):
    full_url = urljoin(config[mnemosyne / api_url], query)
    #TODO: Check for errors
    response = requests.get('/sessions?source_ip={0}'.format(ip_addr))

    #return as dict
    return json.loads(response.json())
