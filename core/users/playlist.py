from core.spotipymusic.song import Song
from typing import List
import uuid


class Playlist:
    def __init__(self, name, songs: List[Song]):
        self.id = uuid.uuid4()
        self.name = name
        self.songs = songs

    def get_playlist_name(self):

        return self.name

    def get_playlist_id(self):

        return self.id

    def get_playlist_songs(self):

        return self.songs

    def add_song(self, song: Song):

        self.songs.append(song)

    def change_name(self, name):

        self.name = name
    