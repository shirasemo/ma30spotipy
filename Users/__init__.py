from Exceptions import PlaylistAlreadyExists


class User:
    def __init__(self, name, type='Free'):
        self.name = name
        self.type = type
        self.playlists = {}

    def create_playlist(self, name, tracks):
        if self.playlists.get(name) is None:
            self.playlists.update({name: tracks})
        else:
            raise PlaylistAlreadyExists
