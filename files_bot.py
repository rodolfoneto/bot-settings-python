import requests
import tkinter as tk
import simplejson as json
from pathlib import Path
import global_settings as gs
import login

def get_accounts_directory():
    bot_path = gs.get('bot_path')
    list_accounts = []
    for child in Path(bot_path+'/config').iterdir():
        if child.is_dir() and child.name != 'global':
            list_accounts.append(child.name)
    return list_accounts
# print(get_accounts_directory())

def get_account_setting_file_path(account):
    path_file = gs.get('bot_path') + '/config/' + account + '/settings.json'
    if Path(path_file).exists() == False:
        raise Exception('File '+account+'/settings.json not found')
    return path_file

def get_settings_by_account(account):
    path_file = get_account_setting_file_path(account)
    file = open(path_file, 'r')
    settings = json.load(file)
    file.close()
    return settings

def create_new_settings_content(local, web):
    local['speedUpSettings'] = web['speedUpSettings']
    local['connectionSettings']['otherLoginTime'] = web['connectionSettings']['otherLoginTime']
    local['gatherSettings'] = web['gatherSettings']
    local['rallySettings'] = web['rallySettings']
    local['cargoShipSettings'] = web['cargoShipSettings']
    local['supplySettings'] = web['supplySettings']
    local['heroSettings'] = web['heroSettings']
    local['heroStageSettings'] = web['heroStageSettings']
    local['arenaSettings'] = web['arenaSettings']
    local['buildSettings'] = web['buildSettings']
    local['eventSettings'] = web['eventSettings']
    return local

def write_file(account, local, web):
    new_content = create_new_settings_content(local, web)
    path_file = get_account_setting_file_path(account)
    file = open(path_file, 'w')
    return json.dump(new_content, file, sort_keys=True, indent=4)

def save_web_settings(account, web_content):
    local = get_settings_by_account(account)
    # print(web_content, local)
    # return
    write_file(account, local, web_content)
# save_web_settings('1625103499', '{}')
