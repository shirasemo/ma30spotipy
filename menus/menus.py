from consolemenu import *
from consolemenu.items import *

from search.search_methods import *


def login_signup_menu():
    pass


def search_menu():
    console_menu = ConsoleMenu("spotipy")

    menu_item = MenuItem("search")

    search_artists = FunctionItem("show artists", artists)
    search_artist_top_tracks = FunctionItem('artist top tracks', artist_top_tracks)
    search_artist_albums = FunctionItem('artist album', artist_albums)
    search_track_in_album = FunctionItem('tracks in album', track_in_album)

    console_menu.append_item(search_artists)
    console_menu.append_item(search_artist_albums)
    console_menu.append_item(search_artist_top_tracks)
    console_menu.append_item(search_track_in_album)

    console_menu.show()
