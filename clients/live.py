import requests

from constants import URL
import models


class Live:
    model = models.Live
    fk = models.Live.foreign_keys
    endpoint = URL

    def get_all(self):
        raw = requests.get(self.endpoint).json()
        self.data = [self._parse(i) for i in raw['live']]

    def _parse(self, x):
        ep = x['episode']
        series = self.fk['episode'].foreign_keys['series'](None, ep['series'])
        episode = self.fk['episode'](None, series, ep['number'], ep['title'])

        team = self.fk['team'](None, x['team'], x['team']['members'])

        song = self.fk['song'](None, x['song']['title'], team) 

        md = self.fk['md'](None, x['MD']['title'], team)

        coordinate = None  # FIXME: so dull

        return self.model(
            None,
            episode,
            team,
            song,
            md,
            coordinate,
        )