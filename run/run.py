import extractor
from config import configuration


def main():
    extractor.parse_files(configuration.tracks_metadata_path)


if __name__ == "__main__":
    main()
