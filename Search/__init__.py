import functools

import Models
import Extractor
import Users
from Exceptions import *

Extractor.parse_files(r"C:\Users\shira\Downloads\drive-download-20220209T075512Z-001.zip")
user = Users.User('shira', 'semo')


def limit_search_results(func):

    @functools.wraps(func)
    def inner(*args):
        if user.type == 'Free':
            return func(*args)[:5:]
        return func(*args)

    return inner


@limit_search_results
def artists():
    return [artist.name for artist in Models.artists.values()]


@limit_search_results
def artist_albums(artist_id):
    try:
        albums_id = Models.artists.get(artist_id).albums_id
        return [Models.albums.get(id).name for id in albums_id]
    except AttributeError:
        raise ArtistNotFound


@limit_search_results
def artist_top_tracks(artist_id):
    try:
        albums_id = Models.artists.get(artist_id).albums_id
    except AttributeError:
        raise ArtistNotFound
    for id in albums_id:
        album = Models.albums.get(id)
        tracks = album.tracks_ids
        result = []
        for track in tracks:
            pos = Models.tracks.get(track)
            result.append(pos)
    return [track.name for track in sorted(result, key=lambda t: t.popularity, reverse=True)]


@limit_search_results
def track_in_album(album_id):
    try:
        album = Models.albums.get(album_id)
        tracks = album.tracks_ids
        return [Models.tracks.get(track).name for track in tracks]
    except AttributeError:
        raise AlbumNotFound
