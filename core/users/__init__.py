from core.users.usersfile import users_file_reader


def create_user(username, is_premium=False):
    from core.users.user import User
    from core.users.usersfile import insert_to_users_file, users_file_reader
    users_names = [user['username'] for user in users_file_reader()]
    if username in users_names:

        # create my own exception
        return "Name is taken"

    user = User(username=username, playlists=[], is_premium=is_premium)
    insert_to_users_file(user)

    return user


def create_new_playlist(user, playlist_name):
    from core.users.user import User
    user.add_playlist(playlist_name)

    return user


def add_song_to_playlist(user, playlist_name, song):
    from core.users.user import User
    user.add_song_to_playlist(playlist_name, song)

    return user
