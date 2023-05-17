import requests
import time
from config import KEY


def get_overview(match_id):
    time.sleep(10)
    _URL = 'https://sea.api.riotgames.com/lol/match/v5/matches/' + match_id + '?api_key=' + KEY
    try:
        response = requests.get(_URL, timeout=5)
        response.raise_for_status()
        print(response)
        game_info = response.json()
        print(game_info)
        return game_info
        # Code here will only run if the request is successful
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return None


def get_data(match_id):
    time.sleep(10)
    _URL = 'https://sea.api.riotgames.com/lol/match/v5/matches/' + match_id + '/timeline?api_key=' + KEY
    print(_URL)
    try:
        response = requests.get(_URL, timeout=5)
        response.raise_for_status()
        print(response)
        game_info = response.json()
        return game_info
        # Code here will only run if the request is successful
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    return None
