from flask import Flask
from core.search import get_top_songs, get_songs_from_album, get_artist_albums_names, get_artists_names, search

app = Flask(__name__)

@app.route("/artists>")
def get_all_artists():

    return search(get_artists_names(), True)

@app.route("/albums/<id>")
def get_all_albums(id):

    return search(get_artist_albums_names(id), True)

@app.route("top/<id>")
def get_top_songs(id):

    return search(get_top_songs(id), True)

@app.route("songs/<id>")
def get_all_songs_from_album(id):

    return search(get_songs_from_album(id), True)


app.run()