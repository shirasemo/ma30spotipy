import json
from zipfile import ZipFile
import Models
import Exceptions


def read_files_from_zip(path):
    files = []
    with ZipFile(path, 'r') as zip:
        for file_name in zip.namelist():
            with zip.open(file_name, 'r') as file:
                file_content = json.dumps(file.read().decode('utf-8'))
                files.append(json.loads(json.loads(file_content)))
    zip.close()
    return files


def parse_track(track: {}):
    id = track.get('id')
    name = track.get('name')
    popularity = track.get('popularity')
    if Models.tracks.get(id) is None:
        return Models.Track(id, name, popularity)
    else:
        raise Exceptions.TrackAlreadyExists


def parse_album(album: {}):
    id = album.get('id')
    name = album.get('name')
    pos = Models.albums.get(id)
    if Models.albums.get(id) is None:
        return Models.Album(id, name)
    else:
        return pos


def parse_artist(artist: {}):
    id = artist.get('id')
    name = artist.get('name')
    pos = Models.artists.get(id)
    if pos is None:
        return Models.Artist(id, name)
    else:
        return pos
