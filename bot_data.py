import requests
import tkinter as tk
import simplejson
from pathlib import Path
import global_settings as gs
import login


def read_directory():
    bot_path = gs.get('bot_path')
    for child in Path(bot_path+'/config').iterdir():
        if child.is_dir() and child.name != 'global':
            if Path(bot_path+'/config/'+child.name+'/settings.json').exists():
                f_settings = open(bot_path+'/config/'+child.name+'/settings.json', 'r')
                print(f_settings.readlines())
# read_directory()

def get_accounts_directory():
    bot_path = gs.get('bot_path')
    list_accounts = []
    for child in Path(bot_path+'/config').iterdir():
        if child.is_dir() and child.name != 'global':
            list_accounts.append(child.name)
    return list_accounts
# print(get_accounts_directory())

def get_settings_txt_by_account_id(account_id):
    bot_path = gs.get('bot_path')
    path = bot_path+'/config/' + account_id
    if Path(path).exists() and Path(path).is_dir():
        path_file = path + '/settings.json'
        if Path(path_file).exists() and Path(path_file).is_file():
            file = open(path_file, 'r')
            content_file = file.readlines()
            return content_file
# get_settings_txt_by_account_id(get_accounts_directory()[0])

def get_settings_like_object(settings_txt):
    settings = simplejson.load(settings)
    print(settings)
# get_settings_like_object(get_settings_txt_by_account_id(get_accounts_directory()[0]))



def write_file(path, content):
    bot_path = gs.get('bot_path')
    path = bot_path+'/config/' + path + '/settings.json'
    if Path(path).exists():
        f_settings = open(path, 'w')
        f_settings.write(content)
        f_settings.close
        return True

def create_header():
    token = gs.get('login_token')
    return {'Authorization': 'Bearer '+token,'Accept':'application/json'}

def make_request(account):
    api_url = gs.get('url_base')
    url = api_url + "/accounts/?accounts=" + account
    headers = create_header()
    response = requests.get(url, headers=headers)
    print('response.status_code', response.status_code)
    if response.status_code == 200:
        json_data = response.json()
        for i in json_data:
            write_file(i, json_data[i])
    elif response.status_code == 401:
        login.main()
    else:
        print(response)

