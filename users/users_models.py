import logging
from exceptions import *
from config import configuration

logging.basicConfig(filename=configuration.logs_file_path, filemode='w', format='%(name)s, %(levelname)s, %(message)s',
                    datefmt='%Y:%m:%d %H:%M:%S')


class User:
    def __init__(self, username, password, type='Free'):
        self.username = username
        self.password = password
        self.type = type
        self.playlists = {}
        configuration.users.update({username: self})
        logging.debug('new user was created')

    def create_playlist(self, name):
        if self.type == 'Free' and len(self.playlists) <= configuration.limit_free_user_playlists:
            if self.playlists.get(name) is None:
                self.playlists.update({name: []})
                configuration.users.update({self.username: self})
            else:
                raise PlaylistAlreadyExists
        else:
            raise NotAPremiumUser
        logging.debug(f'{self.username} created a playlist')

    def add_track(self, playlist_name, track):
        user = configuration.users.get(self.username)
        playlist = user.playlists.get(playlist_name)
        if user.type == 'Free':
            if len(playlist) <= configuration.limit_free_user_tracks_in_playlist:
                playlist.append(track)
            else:
                raise NotAPremiumUser
