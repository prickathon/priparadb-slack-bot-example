import json

from clients.live import Live


def handler(*arg):
    lives = Live()
    lives.get_all()
    text = '\n'.join(map(as_text, lives.data))
    return f'{arg[0]} のライブは\n{text}'


def as_text(live):
    ep = f":apple: `{live.episode.title}` にて `{live.song.title}`を歌いました"
    dm = f"MD は `{live.md.title}`"
    return '\n'.join([ep, dm])