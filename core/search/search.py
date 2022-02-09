from core.spotipymusic import get_artists


def get_all_artists():
    artists = get_artists()

    return artists.get_artists()


def get_artists_names():
    for artist in get_all_artists():
        print(artist.get_artist_name())


def get_artist_albums(artist_id):
    for artist in get_all_artists():
        if artist.get_artist_id() == artist_id:
            for album in artist.get_albums():
                print(album.get_album_name())


get_artist_albums("7Ln80lUS6He07XvHI8qqHH")

