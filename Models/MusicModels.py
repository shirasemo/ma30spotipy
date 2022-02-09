class Artist:
    def __init__(self, id, name, albums=None):
        self.id = id
        self.name = name
        if albums is None:
            self.albums = []
        else:
            self.albums = albums


class Album:
    def __init__(self, id, name, songs=None):
        self.id = id
        self.name = name
        if songs is None:
            self.songs = []
        else:
            self.songs = songs


class Track:
    def __init__(self, album, artists, id, name, popularity):
        self.album = album
        self.artists = artists
        self.id = id
        self.name = name
        self.popularity = popularity
        