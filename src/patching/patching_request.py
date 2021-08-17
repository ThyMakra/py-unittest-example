import requests
from requests.exceptions import ConnectionError


def requesting_github():
    try:
        r = requests.get('http://github.com/ThyMakra')

        print("response: ", r)
        if r.status_code == 200:
            return r.json()
    except ConnectionError:
        return "ConnectionError was raised"
    return None
