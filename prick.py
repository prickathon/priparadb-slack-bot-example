import configparser
import re

from slackclient import SlackClient
import requests

import handlers


def cmd_parser(text):
    # FIXME: so tired
    parsed = re.match(r'^(live-who)\s+(.+)?$', text)
    if not parsed:
        return None, None

    parsed = parsed.groups()
    return parsed[0], parsed[1:]
    

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
        (cmd, args) = cmd_parser(msg[0]['text'])
        if not cmd:
            continue
        handler = handlers.of.get(cmd)
        import pdb; pdb.set_trace();
        if not handler:
            continue
        client.rtm_send_message(msg[0]['channel'], handler(*args))
else:
    print('Connection failed')