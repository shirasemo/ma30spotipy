import Models
import Extractor
from Exceptions import *

Extractor.parse_files(r"C:\Users\shira\Downloads\drive-download-20220209T075512Z-001.zip")


def artists():
    return [artist.name for artist in Models.artists.values()]


def artist_albums(artist_id):
    try:
        albums_id = Models.artists.get(artist_id).albums_id
        return [Models.albums.get(id).name for id in albums_id]
    except AttributeError:
        raise ArtistNotFound


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


def track_in_album(album_id):
    try:
        album = Models.albums.get(album_id)
        tracks = album.tracks_ids
        return [Models.tracks.get(track).name for track in tracks]
    except AttributeError:
        raise AlbumNotFound
