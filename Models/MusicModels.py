class Artist:
    def __init__(self, id, name, albums=None):
        self.id = id
        self.name = name
        if albums is None:
            self.albums = []
        else:
            self.albums = albums

