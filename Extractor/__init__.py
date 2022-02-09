from ExtractSongs import read_files_from_zip, parse_tracks, parse_album, parse_artist


def get_tracks(path):
    tracks = read_files_from_zip(path)
    return [parse_tracks(track) for track in tracks]


def main():
    print(get_tracks(r"C:\Users\shira\Downloads\drive-download-20220209T075512Z-001.zip"))


if __name__ == "__main__":
    main()
