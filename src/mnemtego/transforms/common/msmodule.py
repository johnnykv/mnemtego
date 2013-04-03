import requests
from canari.config import config


def query(query):
    full_url = config['mnemtego/api_url'] + query
    #maybe fetch creds through maltego popup?
    username = config['mnemtego/username']
    password = config['mnemtego/password']

    sess = requests.Session()

    #login and store session cookie
    payload = {'username': username, 'password': password}
    response = sess.post(config['mnemtego/login_url'], payload, verify=False)
    if response.status_code != 200:
        raise Exception("Error while requesting session cookie from mnemtego: {0}".format(response.status_code))
        return []

    response = sess.get(full_url, verify=False)
    #TODO: Check statuscode

    return response.json()