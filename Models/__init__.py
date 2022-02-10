artists = {}
albums = {}
tracks = {}


class Artist:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.albums_id = []

    def add_album(self, id):
        self.albums_id.append(id)

    def save_to_dict(self):
        artists.update({self.id: self})

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, albums: {self.albums_id}'


class Album:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tracks_ids = []
        self.artists_id = []

    def add_artist(self, artist_id):
        self.artists_id.append(artist_id)

    def add_track(self, track_id):
        self.tracks_ids.append(track_id)

    def save_to_dict(self):
        albums.update({self.id: self})

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, tracks: {self.tracks_ids}, artists: {self.artists_id}'


class Track:
    def __init__(self, id, name, popularity):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.album_id = []
        self.artists_ids = []

    def add_artist(self, artist_id):
        self.artists_ids.append(artist_id)

    def add_album(self, album_id):
        self.album_id.append(album_id)

    def save_to_dict(self):
        tracks.update({self.id: self})

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, album: {self.album_id}, artists: {self.artists_ids},' \
               f' popularity: {self.popularity}'
