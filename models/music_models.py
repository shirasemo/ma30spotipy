import logging
from config import configuration

logging.basicConfig(filename=configuration.logs_file_path, filemode='w', format='%(name)s, %(levelname)s, %(message)s',
                    datefmt='%Y:%m:%d %H:%M:%S')


class Artist:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.albums_id = []
        configuration.artists.update({self.id: self})
        logging.debug('new artist was added')

    def add_album(self, id):
        self.albums_id.append(id)
        configuration.artists.update({self.id: self})

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, albums: {self.albums_id}'


class Album:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tracks_ids = []
        self.artists_id = []
        configuration.albums.update({self.id: self})
        logging.debug('new album was added')

    def add_artist(self, artist_id):
        self.artists_id.append(artist_id)

    def add_track(self, track_id):
        self.tracks_ids.append(track_id)
        configuration.albums.update({self.id: self})

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, tracks: {self.tracks_ids}, artists: {self.artists_id}'


class Track:
    def __init__(self, id, name, popularity):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.album_id = []
        self.artists_ids = []
        configuration.tracks.update({self.id: self})
        logging.debug('new track was added')

    def add_artist(self, artist_id):
        self.artists_ids.append(artist_id)

    def add_album(self, album_id):
        self.album_id.append(album_id)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, album: {self.album_id}, artists: {self.artists_ids},' \
               f' popularity: {self.popularity}'
