import json
import os
from core.spotipymusic.album import Album
from core.spotipymusic.artist import Artist
from core.spotipymusic.song import Song


songs = os.listdir(r'C:\Users\Daniel\PycharmProjects\Spotipy\helpers\documents\songs')
for file in songs:
    song_file = open(fr'C:\Users\Daniel\PycharmProjects\Spotipy\helpers\documents\songs\{file}', "r")
    track = json.load(song_file)
    print(track)
    song = Song(track['track']['id'], track['track']['name'], track['track']['popularity'])

    break
