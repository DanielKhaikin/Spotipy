import json
from core.users.user import User
from helpers.conventionsfilereader import get_users_location
from core.users import create_user


def insert_to_users_file(user: User):
    file_location = get_users_location()
    with open(file_location, 'r') as users_file:
        users = json.load(users_file)

    print()
    users.append({
        "id": user.get_user_id(),
        "username": user.get_user_username(),
        "is premium": user.get_is_premium()
    })
    with open(file_location, 'w') as users_file:
        json.dump(users, users_file, separators=(',', ': '), indent=4)




insert_to_users_file(user=create_user("Akiva", True))