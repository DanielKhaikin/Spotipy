def create_user(username, is_premium=False):
    from core.users.user import User
    user = User(username=username, playlists=[], is_premium=is_premium)
    return user


def create_new_playlist(user, playlist_name):
    from core.users.user import User
    user.add_playlist(playlist_name)

    return user


def add_song_to_playlist(user, playlist_name, song):
    from core.users.user import User
    user.add_song_to_playlist(playlist_name, song)

    return user
