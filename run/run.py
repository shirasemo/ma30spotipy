from consolemenu import *
from consolemenu.items import *

import extractor
from search.search_methods import *
from resources.config import configuration
from users.users_models import User

extractor.parse_files(configuration.tracks_metadata_path)
configuration.read_configuration()

configuration.user = User('username', 'password')

menu = ConsoleMenu("spotipy")

menu_item = MenuItem("search")

search_artists = FunctionItem("show artists", artists)
search_artist_top_tracks = FunctionItem('artist top tracks', artist_top_tracks)
search_artist_albums = FunctionItem('artist album', artist_albums)
search_track_in_album = FunctionItem('tracks in album', track_in_album)

menu.append_item(search_artists)
menu.append_item(search_artist_albums)
menu.append_item(search_artist_top_tracks)
menu.append_item(search_track_in_album)

menu.show()
