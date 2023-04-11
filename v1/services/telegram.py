import requests

token = '5591221567:AAHT9mNb1KzB7541wzf9PfcGiup23oqA34s'


# 5556042404
def notify(msg, chat_id='5556042404', parse_mode='html'):
    payload = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=' + parse_mode + '&text=' + msg

    response = requests.get(payload)

    return response.json()


def get_update():
    payload = f'https://api.telegram.org/bot{token}/getUpdates'
    response = requests.get(payload).json()

    update_id = 0
    if response['ok']:
        for update in response['result']:
            update_id = update['update_id']

    payload = f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}'
    requests.get(payload).json()

    return response
