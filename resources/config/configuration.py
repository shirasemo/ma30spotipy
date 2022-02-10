import json

data = {}
tracks_metadata_path = r"C:\Users\shira\Downloads\drive-download-20220209T075512Z-001.zip"
logs_file_path = r'C:\Users\shira\Code\spotipy\resources\logs\logs.json'
config_file_path = r'C:\Users\shira\Code\spotipy\resources\config\configuration.json'
artists = {}
albums = {}
tracks = {}
users = {}


def read_configuration():
    with open(config_file_path, 'r') as config_json:
        text = json.dumps(config_json.read())
        data = json.loads(json.loads(text))
        artists = data[0]
        albums = data[1]
        tracks = data[2]
        #users = data[3]
    config_json.close()


def write_configuration(content):
    with open(config_file_path, 'w') as config_json:
        json.dump(content, config_json)
    config_json.close()


user = None

limit_free_user_playlists = data.get('limit_free_user_playlists')
limit_free_user_tracks_in_playlist = data.get('limit_free_user_tracks_in_playlist')
limit_free_user_search_results = data.get('limit_free_user_search_results')
