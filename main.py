from core.users import create_user, create_new_playlist, add_song_to_playlist
from core.search import get_songs_from_album, get_top_songs, get_artist_albums_names, get_artists_names
from core.spotipymusic import get_artists


users = get_artists()
users[0]