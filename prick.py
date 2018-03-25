import configparser

from slackclient import SlackClient
import requests

import handlers


echo = lambda x: x

config = configparser.ConfigParser()
config.read('.env')
token = config['slack']['API_TOKEN']
client = SlackClient(token)

if client.rtm_connect():
    while client.server.connected is True:
        msg = client.rtm_read()
        if not msg or msg[0].get('type', '') != 'message':
            continue
        m = msg[0]['text'].split(' ')
        if len(m) == 1:
            m.append('')
        text = handlers.of.get(m[0], echo)(m[1])
        print(text)
        client.rtm_send_message(msg[0]['channel'], text)
else:
    print('Connection failed')