from core.spotipymusic.artist import Artist
from typing import List


class Artists:
    def __init__(self, artists: List[Artist]):
        self.artists = artists

    def add_artist(self, artist):
        self.artists.append(artist)
        print(f'Added artist {artist.get_artist_name()}')

    def delete_artist(self, artist_id):
        for artist in self.artists:
            if artist.get_artist_id() == artist_id:
                self.artists.remove(artist)
                print(f'Deleted artist {artist.get_artist_name()}')

    def artist_exists(self, artist_id):
        artists_id = [artist.get_artist_id() for artist in self.artists]

        return artist_id in artists_id

    def get_artist(self, artist_id):
        for artist in self.artists:
            if artist.get_artist_id() == artist_id:

                return artist
