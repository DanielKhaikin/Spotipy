import json
from core.users.user import User
from helpers.conventionsfilereader import get_users_location


def users_file_reader():
    file_location = get_users_location()
    try:
        with open(file_location, 'r') as users_file:
            users = json.load(users_file)

        return users

    except Exception as e:

        return []


def insert_to_users_file(user: User):
    file_location = get_users_location()
    users = users_file_reader()
    users.append({
        "id": user.get_user_id(),
        "username": user.get_user_username(),
        "is premium": user.get_is_premium()
    })
    with open(file_location, 'w') as users_file:
        json.dump(users, users_file, separators=(',', ': '), indent=4)



