import extractor
from menus import menus
from users import *

extractor.parse_files(configuration.tracks_metadata_path)
configuration.read_configuration()


def main():
    menus.login_signup_menu()
    menus.search_menu()


if __name__ == "__main__":
    main()
