import vk
import getpass


APP_ID = '6225304'


def get_user_login():
    login = input("input your login:")
    return login


def get_user_password():
    password = getpass.getpass(prompt='Password: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    online_friends_id = api.friends.getOnline()
    friends_online = api.users.get(user_ids=online_friends_id)
    return friends_online


def output_friends_to_console(friends_online):
    print("Friends Online:")
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
