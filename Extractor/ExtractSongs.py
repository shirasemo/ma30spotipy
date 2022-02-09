import json
from zipfile import ZipFile
import Models


def read_files_from_zip(path):
    files = []
    with ZipFile(path, 'r') as zip:
        for file_name in zip.namelist():
            with zip.open(file_name, 'r') as file:
                file_content = json.dumps(file.read().decode('utf-8'))
                files.append(json.loads(json.loads(file_content)))
    zip.close()
    return files


def parse_tracks(track: {}):
    track = track.get('track')
    album = parse_album(track.get('album'))
    artists = []
    for artist in track.get('artists'):
        artists.append(parse_artist(artist))
    id = track.get('id')
    name = track.get('name')
    popularity = track.get('popularity')
    return Models.Track(album, artists, id, name, popularity)


def parse_album(album: {}):
    id = album.get('id')
    name = album.get('name')
    return Models.Album(id, name)


def parse_artist(artist: {}):
    id = artist.get('id')
    name = artist.get('name')
    return Models.Artist(id, name)
