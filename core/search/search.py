from core.spotipymusic import get_artists


def get_all_artists():
    artists = get_artists()

    return artists.get_artists()


def get_artists_names():
    for artist in get_all_artists():
        print(artist.get_artist_name())


def get_artist_albums_names(artist_id):
    for artist in get_all_artists():
        if artist.get_artist_id() == artist_id:
            for album in artist.get_albums():
                print(album.get_album_name())


def get_all_albums():
    artists = get_all_artists()
    albums = []
    for artist in artists:

        for album in artist.get_albums():
            albums.append(album)

    return albums


def get_songs_from_album(album_id):
    for album in get_all_albums():
        if album.get_album_id() == album_id:
            [print(song.get_song_name()) for song in album.get_songs()]


get_songs_from_album("1Y1kv5n86UzcV3dBkkAsSq")
get_artist_albums_names("7Ln80lUS6He07XvHI8qqHH")

