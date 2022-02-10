from core.spotipymusic import get_artists


def get_all_artists():
    artists = get_artists()

    return artists.get_artists()


def get_artists_names():

    return [artist.get_artist_name()for artist in get_all_artists()]


def get_artist_albums_names(artist_id):
    for artist in get_all_artists():
        if artist.get_artist_id() == artist_id:

            return [album.get_album_name() for album in artist.get_albums()]


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

            return [song.get_song_name() for song in album.get_songs()]


def get_all_songs(artist_id):
    songs = []
    for artist in get_all_artists():
        if artist.get_user_id() == artist_id:
            for album in artist.get_albums():
                [songs.append(song) for song in album.get_songs()]

            return songs


def get_top_songs(artist_id):
    songs = get_all_songs(artist_id)
    songs.sort(key=lambda song: song.popularity, reverse=True)
    return [f'{song.get_song_name()} - {song.get_song_popularity()}' for song in songs]



