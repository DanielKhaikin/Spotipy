from core.users import create_user, create_new_playlist, add_song_to_playlist
from core.search import get_songs_from_album, get_top_songs, get_artist_albums_names, get_artists_names, search
from core.spotipymusic import get_artists

user = create_user('Daniel', True)
if type(user) is not str:
    print(search(search_func=get_top_songs("71NBOcJ9lMeXqnbnya1z0x"), is_premium=user.get_is_premium()))

else:
    print(user)
