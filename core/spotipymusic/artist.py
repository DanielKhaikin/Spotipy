from core.spotipymusic.album import Album
from typing import List
from core.users.user import User


class Artist(User):
    def __init__(self, artist_id, name, albums: List[Album]):
        User.__init__(self, name, [], artist_id, True)
        self.albums = albums

    def get_albums(self):

        return self.albums

    def add_album(self, new_album: Album):
        self.albums.append(new_album)

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
                break


