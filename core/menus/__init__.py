from core.users import create_user
from core.users import users_file_reader
from helpers.exceptions import NotAnOptionException, UsernameDoesNotExistsException


def login_menu():
    print("1- login to spotipy")
    print("2- sign up to spotipy")
    ans = input(">>>")
    print("-----------------------------")
    if ans == 1:
        login()
    elif ans == 2:
        sign_up()
    else:
        raise NotAnOptionException


def sign_up():
    username = input("choose username")
    is_premium = input("1 for premium, else for free")
    print("-----------------------------")
    if is_premium == 1:
        user = create_user(username, True)

    else:
        user = create_user(username)

    print("sign in completed successfully")


def login():
    username = input("enter username")
    usernames = [user["username"] for user in users_file_reader()]
    print("-----------------------------")
    if username in usernames:
        print("login completed successfully")
    else:
        raise UsernameDoesNotExistsException
