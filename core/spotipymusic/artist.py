from core.spotipymusic.album import Album
from typing import List


class Artist:
    def __init__(self, artist_id, name, albums: List[Album]):
        self.artist_id = artist_id
        self.name = name
        self.albums = albums

    def get_artist_id(self):

        return self.artist_id

    def get_artist_name(self):

        return self.name

    def get_albums(self):

        return self.albums

    def add_album(self, new_album: Album):
        self.albums.append(new_album.get_album_id())
        print(f"Added album {new_album.get_album_name()} to artist {self.name}")

    def album_exists(self, album_id):
        albums_id = [album.get_album_id() for album in self.albums]

        return album_id in albums_id

    def get_album(self, album_id):
        for album in self.albums:
            if album.get_album_id() == album_id:

                return album

    def delete_album(self, album_id):
        for album in self.albums:
            if album.get_album_id() == album_id:
                self.albums.remove(album)
                print(f'Removed album {album.get_album_name()}')
                break


