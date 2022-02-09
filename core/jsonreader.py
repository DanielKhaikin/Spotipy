import json
import os
from core.spotipymusic.album import Album
from core.spotipymusic.artist import Artist
from core.spotipymusic.artists import Artists
from core.spotipymusic.song import Song


artists = Artists([])
songs_dir = os.listdir(r'C:\Users\Daniel\PycharmProjects\Spotipy\helpers\documents\songs')
count = 0
for file in songs_dir:
    try:
        track_file = open(fr'C:\Users\Daniel\PycharmProjects\Spotipy\helpers\documents\songs\{file}', "r")
        track = json.load(track_file)
        song = Song(track['track']['id'], track['track']['name'], track['track']['popularity'])
        print(song)
        for artist in track['track']['artists']:
            if artists.artist_exists(artist['id']):

                exist_artist = artists.get_artist(artist['id'])
                artists.delete_artist(exist_artist.get_artist_id())
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
                artists.add_artist(new_artist)
        print(song.get_song_name())

    except Exception as e:
        raise e

    finally:
        count += 1
        print(count)

print(artists)







