from extractor.extract_songs import *


def parse_files(path):
    items = read_files_from_zip(path)
    artists_obj = []
    albums = []
    tracks = []
    for item in items:
        item = item.get('track')
        track = parse_track(item)
        album = parse_album(item.get('album'))
        album.add_track(track.id)
        track.add_album(album.id)
        artists = item.get('artists')
        for artist in artists:
            artist = parse_artist(artist)
            track.add_artist(artist.id)
            album.add_artist(artist.id)
            artist.add_album(album.id)
            artists_obj.append(artist.__dict__)
        albums.append(album.__dict__)
        tracks.append(track.__dict__)
    configuration.write_configuration([artists_obj, albums, tracks])
