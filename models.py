class Team:
    def __init__(self, pk, name, members):
        self.pk = pk
        self.name = name
        self.members = members


class Song:
    foreign_keys = {
        'team': Team,
    }

    def __init__(self, pk, title, team):
        self.pk = pk
        self.title = title
        self.team = team


class Series:
    def __init__(self, pk, title):
        self.pk = pk
        self.title = title


class Character:
    def __init__(self, pk, first_name, last_name, icon_url):
        self.pk = pk
        self.first_name = first_name
        self.last_name = last_name
        self.icon_url = icon_url


class Brand:
    def __init__(self, pk, name):
        self.pk = pk
        self.name = name


class Coordinate:
    foreign_keys = {
        'brand': Brand,
        'character': Character,
    }

    def __init__(self, pk, name, brand, character):
        self.pk = pk
        self.name = name
        self.brand = brand
        self.character = character


class Episode:
    foreign_keys = {
        'series': Series,
    }

    def __init__(self, pk, series, number, title):
        self.pk = pk
        self.series = series
        self.number = number
        self.title = title


class Md:
    foreign_keys = {
        'team': Team,
    }

    def __init__(self, pk, title, team):
        self.pk = pk
        self.title = title
        self.team = team



class Live:
    foreign_keys = {
        'episode': Episode,
        'team': Team,
        'song': Song,
        'md': Md,
        'coordinate': Coordinate,
    }

    def __init__(self, pk, episode, team, song, md, coordinate):
        self.pk = pk
        self.episode = episode
        self.team = team
        self.song = song
        self.md = md
        self.coordinate = coordinate

class TeamMember:
    foreign_keys = {
        'team': Team,
        'member': Character,
    }    

    def __init__(self, pk, team, character):
        self.pk = pk
        self.team = team
        self.member = character