import os


class StaticsDir:
    def __init__(self, dir_path):
        self._dir_path = dir_path

    def read_bytes(self, path):
        if path[0] == '/':
            path = path[1:]

        try:
            full_path = os.path.join(self._dir_path, path)
            with open(full_path, 'rb') as f:
                return f.read()
        except (FileNotFoundError, IsADirectoryError):
            raise FileDoesNotExistException


class FileDoesNotExistException(Exception):
    pass
