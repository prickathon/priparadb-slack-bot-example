import json

from clients.live import Live


def handler(arg):
    lives = Live()
    lives.get()
    text = '\n'.join(map(as_text, lives.rawdata['live']))
    return f'{arg} のライブは\n{text}'


def as_text(live):
    ep = f":apple: `{live['episode']['title']}` にて `{live['song']['title']}`を歌いました"
    dm = f"MD は `{live['MD']['title']}`"
    return '\n'.join([ep, dm])