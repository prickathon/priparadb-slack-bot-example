from constants import URL

import requests


class Live:
    endpoint = URL
    def get(self):
        self.rawdata = requests.get(self.endpoint).json()