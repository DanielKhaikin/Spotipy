from core.users.playlist import Playlist
from typing import List
import uuid


class User:
    def __init__(self, username, playlists: List[Playlist], user_id=uuid.uuid4(), is_premium=False):
        self.user_id = user_id
        self.username = username
        self.is_premium = is_premium
        self.playlists = playlists

    def get_user_id(self):

        return self.user_id

    def get_user_username(self):

        return self.username

    def get_is_premium(self):

        return self.is_premium

    def get_playlists(self):

        return self.playlists

    def playlist_name_exist(self, playlist_name):

        for playlist in self.playlists:
            if playlist.get_playlist_name() == playlist_name:

                return True

        return False

    def add_playlist(self, playlist_name):
        if len(self.playlists) is 5 and self.is_premium is False:
            print("You can't create this playlist, if you want upgrade to premium")
        else:
            self.playlists.append(Playlist(playlist_name, []))

    def add_song_to_playlist(self, playlist_name, song):
        for playlist in self.playlists:
            if playlist.get_playlist_name() == playlist_name:
                if (len(playlist.get_playlist_songs() is 20)) and self.is_premium is False:
                    print("You can't add this song to the playlist, if you want upgrade to premium")
                    break
                else:
                    self.playlists.remove(playlist)
                    playlist.add_song(song)
                    self.playlists.append(playlist)
                    break







