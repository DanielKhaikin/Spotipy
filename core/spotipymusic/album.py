from core.spotipymusic.song import Song
from typing import List


class Album:
    def __init__(self, album_id, name, songs: List[Song]):
        self.album_id = album_id
        self.name = name
        self.songs = songs

    def get_album_id(self):

        return self.album_id

    def get_album_name(self):

        return self.name

    def get_songs(self):

        return self.songs

    def add_song(self, new_song: Song):

        self.songs.append(new_song)

    def song_exists(self, song: Song):

        return song in self.songs

