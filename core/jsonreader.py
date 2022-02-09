import json
import os
from core.spotipymusic.album import Album
from core.spotipymusic.artist import Artist
from core.spotipymusic.song import Song

songs = []
albums = []
artists = []
songs_dir = os.listdir(r'C:\Users\Daniel\PycharmProjects\Spotipy\helpers\documents\songs')
for file in songs_dir:
    track_file = open(fr'C:\Users\Daniel\PycharmProjects\Spotipy\helpers\documents\songs\{file}', "r")
    track = json.load(track_file)
    print(track)
    song = Song(track['track']['id'], track['track']['name'], track['track']['popularity'])
    songs.append(song)
    for index in track['track']['artists']:
        
    album = Album(track['track']['album']['id'], track['track']['album']['name'], [])

    break
