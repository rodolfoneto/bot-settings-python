import requests
import global_settings as gs
import login
import files_bot

def create_header():
    token = gs.get('login_token')
    return {
        'Authorization': 'Bearer ' + token,
        'Accept':'application/json',
        'User-Agent': 'BotRequest/0.1',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json'
    }

def make_request(account):
    api_url = gs.get('url_base')
    url = api_url + "/accounts/?accounts=" + account
    headers = create_header()
    response = requests.get(url, headers=headers)
    print('response.status_code', response.status_code)
    return response
