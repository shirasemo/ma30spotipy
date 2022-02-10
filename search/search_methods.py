import functools

from exceptions import *
from resources.config import configuration


def limit_search_results(func):

    @functools.wraps(func)
    def inner(*args):
        if configuration.user.type == 'Free':
            return func(*args)[:configuration.limit_free_user_search_results:]
        return func(*args)

    return inner


@limit_search_results
def artists():
    return [artist.name for artist in configuration.artists.values()]


@limit_search_results
def artist_albums(artist_id):
    try:
        albums_id = configuration.artists.get(artist_id).albums_id
        return [configuration.albums.get(id).name for id in albums_id]
    except AttributeError:
        raise ArtistNotFound


@limit_search_results
def artist_top_tracks(artist_id):
    try:
        albums_id = configuration.artists.get(artist_id).albums_id
    except AttributeError:
        raise ArtistNotFound
    for id in albums_id:
        album = configuration.albums.get(id)
        tracks = album.tracks_ids
        result = []
        for track in tracks:
            pos = configuration.tracks.get(track)
            result.append(pos)
    return [track.name for track in sorted(result, key=lambda t: t.popularity, reverse=True)]


@limit_search_results
def track_in_album(album_id):
    try:
        album = configuration.albums.get(album_id)
        tracks = album.tracks_ids
        return [configuration.tracks.get(track).name for track in tracks]
    except AttributeError:
        raise AlbumNotFound
