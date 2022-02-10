import json
from zipfile import ZipFile
import models
import exceptions
from config import configuration


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
    if configuration.tracks.get(id) is None:
        return models.Track(id, name, popularity)
    else:
        raise exceptions.TrackAlreadyExists


def parse_album(album: {}):
    id = album.get('id')
    name = album.get('name')
    pos = configuration.albums.get(id)
    if configuration.albums.get(id) is None:
        return models.Album(id, name)
    else:
        return pos


def parse_artist(artist: {}):
    id = artist.get('id')
    name = artist.get('name')
    pos = configuration.artists.get(id)
    if pos is None:
        return models.Artist(id, name)
    else:
        return pos
