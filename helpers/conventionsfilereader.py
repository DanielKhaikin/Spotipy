import json


def get_songs_location():
    with open("C:\\Users\\Daniel\\PycharmProjects\\Spotipy\\helpers\\documents\\conventions.json", 'r') as conv_file:
        data = json.load(conv_file)

    return data["songs location"]


def get_users_location():
    with open("C:\\Users\\Daniel\\PycharmProjects\\Spotipy\\helpers\\documents\\conventions.json", 'r') as conv_file:
        data = json.load(conv_file)

    return data["users location"]
