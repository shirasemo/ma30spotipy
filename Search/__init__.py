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

