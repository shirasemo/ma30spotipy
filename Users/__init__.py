from Exceptions import *

users = {}


class User:
    def __init__(self, username, password, type='Free'):
        self.username = username
        self.password = password
        self.type = type
        self.playlists = {}
        users.update({username: self})

    def create_playlist(self, name):
        if self.type == 'Free' and len(self.playlists) <= 5:
            if self.playlists.get(name) is None:
                self.playlists.update({name: []})
                users.update({self.username: self})
            else:
                raise PlaylistAlreadyExists
        else:
            raise NotAPremiumUser

    def add_track(self, playlist_name, track):
        user = users.get(self.username)
        playlist = user.playlists.get(playlist_name)
        if user.type == 'Free':
            if len(playlist) <= 20:
                playlist.append(track)
            else:
                raise NotAPremiumUser
