from extractor.extract_songs import *


def parse_files(path):
    items = read_files_from_zip(path)
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
            artist.save_to_dict()
        track.save_to_dict()
        album.save_to_dict()
