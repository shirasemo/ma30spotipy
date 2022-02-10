import extractor
from resources.config import configuration


def main():
    extractor.parse_files(configuration.tracks_metadata_path)
    configuration.read_configuration()


if __name__ == "__main__":
    main()
