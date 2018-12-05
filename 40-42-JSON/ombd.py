import requests
import json
from pprint import pprint

from json_secrets import ombd_api_key


def main():
    myparams = {
        'apikey': ombd_api_key,
        't': 'Monty+Python'
    }
    url = 'https://www.omdbapi.com/'

    r = requests.get(url, params=myparams)

    data = json.loads(r.text)
    pprint(data)
    # for item in data.items():
    #     pprint(item)

if __name__ == "__main__":
    main()
