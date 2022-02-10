import json
import os
from core.spotipymusic.album import Album
from core.spotipymusic.artist import Artist
from core.spotipymusic.artists import Artists
from core.spotipymusic.song import Song
from helpers.conventionsfilereader import get_songs_location
from core.users.usersfile import insert_to_users_file, users_file_reader


def load_songs():
    artists = Artists([])
    users_id = [user['id'] for user in users_file_reader()]
    songs_location = get_songs_location()
    songs_dir = os.listdir(songs_location)
    for file in songs_dir:
        try:
            track_file = open(f'{songs_location}\\{file}', "r")
            track = json.load(track_file)
            song = Song(track['track']['id'], track['track']['name'], track['track']['popularity'])
            for artist in track['track']['artists']:
                if artists.artist_exists(artist['id']):

                    exist_artist = artists.get_artist(artist['id'])
                    artists.delete_artist(exist_artist.get_user_id())
                    if exist_artist.album_exists(track['track']['album']['id']):
                        album = exist_artist.get_album(track['track']['album']['id'])
                        exist_artist.delete_album(album.get_album_id())
                        album.add_song(song)
                        exist_artist.add_album(album)
                        artists.add_artist(exist_artist)

                    else:
                        album = Album(track['track']['album']['id'], track['track']['album']['name'], [song])
                        exist_artist.add_album(album)
                        artists.add_artist(exist_artist)

                else:
                    album = Album(track['track']['album']['id'], track['track']['album']['name'], [song])
                    new_artist = Artist(artist['id'], artist['name'], [album])
                    if new_artist.get_user_id() not in users_id:
                        insert_to_users_file(new_artist)
                    artists.add_artist(new_artist)
        except Exception as ex:
            print(ex)

    return artists
