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
        self.songs_ids = []
        self.artists_id = []

    def add_artist(self, artist_id):
        self.artists_id.append(artist_id)

    def add_song(self, song_id):
        self.songs_ids.append(song_id)

    def save_to_dict(self):
        albums.update({self.id: self})

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, songs: {self.songs_ids}, artists: {self.artists_id}'


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


class User:
    def __init__(self, name, type, playlists=None):
        self.name = name
        self.type = type
        if playlists is None:
            self.playlists = {}
        else:
            self.playlists = playlists
