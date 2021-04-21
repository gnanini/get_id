import requests
import json


def get_id(game_name):
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    text = json.loads(response.text)
    dicionario = {}

    for game in text['applist']['apps']:
        dicionario[game['name'].lower()] = game['appid']

    print(dicionario[game_name.lower()])

    return dicionario[game_name.lower()]


def test():
    # get_id('MORDHAU')
    get_id(input('Type a correct game name: '))
    return


# test()
