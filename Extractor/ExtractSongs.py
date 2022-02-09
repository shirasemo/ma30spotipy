import json
from zipfile import ZipFile


def read_files_from_zip(path):
    files = []
    with ZipFile(path, 'r') as zip:
        for file_name in zip.namelist():
            with zip.open(file_name, 'r') as file:
                files.append(json.dumps(file.read().decode('utf-8')))
    zip.close()
    return files
