from core.spotipymusic import get_artists


def get_all_artists():
    artists = get_artists()

    return artists.get_artists()


def get_artists_names():
    for artist in get_all_artists():
        print(artist.get_artist_name())


def get_artist_albums():
    
