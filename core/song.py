class Song:
    def __init__(self, song_id, name: str, popularity: int):
        self.song_id = song_id
        self.name = name
        self.popularity = popularity

    def get_song_id(self):

        return self.song_id

    def get_song_name(self):

        return self.name

    def get_song_popularity(self):

        return self.popularity
