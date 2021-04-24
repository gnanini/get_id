import requests
import json
from datetime import date

file = "game_list.json"
url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"

def get_id(game_name):
    global file

    if check_time() == 1:
        # debugging print('upgrade == 1')
        upgrade_content()

    text = open(file, 'r')
    game_list = json.load(text)

    #print(game_list[game_name.lower()])
    return game_list[game_name.lower()]


def test():
    #get_id('MORDHAU')
    get_id(input('Type a correct game name: '))
    return

def upgrade_content(): # this function uploads the ids database, aka game_list.json
    global url
    global file
    response = requests.get(url)
    content = json.loads(response.text)
    table = open(file, 'w')
    game_list = {}

    for game in content['applist']['apps']:
        game_list[game['name'].lower()] = game['appid']

    # checking if it's time for an gamelist update
    today = date.today()
    game_list['data']  = {}
    for i in "ymd":
        game_list["data"][i] = today.strftime('%' + i)

    json.dump(game_list, table)
    table.close()


def check_time(): # this function check if it's time to update
    global file
    text = open(file, 'r')
    json_table = json.load(text)
    text.close()

    today = date.today()
    day = 0 # it controls how many days it's necessary for an update
    for i in 'ymd':
        if i == 'd':
            day = 7
        else:
            day = 0
        if int(today.strftime('%' + i)) > int(json_table['data'][i]) + day:
            return 1
        else:
            return 0


#test()
