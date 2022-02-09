import Models
from ExtractSongs import read_files_from_zip, parse_track, parse_album, parse_artist


def parse_files(path):
    items = read_files_from_zip(path)
    for item in items:
        item = item.get('track')
        track = parse_track(item)
        album = parse_album(item.get('album'))
        album.add_song(track.id)
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


def main():
    parse_files(r"C:\Users\shira\Downloads\drive-download-20220209T075512Z-001.zip")
    print(Models.albums.get('3y7Mwv7UqhABQqsGlzSL6n'))


if __name__ == "__main__":
    main()
