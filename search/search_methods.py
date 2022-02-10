import functools
from flask import Flask

from exceptions import *
from resources.config import configuration

app = Flask('__name__')


def limit_search_results(func):
    @functools.wraps(func)
    def inner(*args):
        if configuration.user.type == 'Free':
            return func(*args)[:configuration.limit_free_user_search_results:]
        return func(*args)

    return inner


@app.route('/search/artists')
@limit_search_results
def artists():
    return [artist.name for artist in configuration.artists.values()]


@app.route('/search/artist_album/<artist_id>')
@limit_search_results
def artist_albums(artist_id):
    try:
        albums_id = configuration.artists.get(artist_id).albums_id
        return [configuration.albums.get(id).name for id in albums_id]
    except AttributeError:
        raise ArtistNotFound


@app.route('/search/artist_top_tracks/<artist_id>')
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


@app.route('/search/tracks_in_album/<album_id>')
@limit_search_results
def track_in_album(album_id):
    try:
        album = configuration.albums.get(album_id)
        tracks = album.tracks_ids
        return [configuration.tracks.get(track).name for track in tracks]
    except AttributeError:
        raise AlbumNotFound


if __name__ == "__main__":
    app.run()
