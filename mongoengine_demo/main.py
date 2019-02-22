import mongoengine

from user import User


def setup():
    mongoengine.register_connection(
        alias='core',
        db='demo',
        host='127.0.0.1',
        port=27017
    )


def print_header():
    print('----------------------------------------------')
    print('|                                             |')
    print('|           User Management v.02              |')
    print('|               demo edition                  |')
    print('|                                             |')
    print('----------------------------------------------')
    print()


def user_loop():
    while True:
        print("Available actions:")
        print(" * [a]dd user")
        print(" * [l]ist users")
        print(" * e[x]it")
        print()
        ch = input("> ").strip().lower()
        if ch == 'a':
            add_user()
        elif ch == 'l':
            list_users()
        elif not ch or ch == 'x':
            print("Goodbye")
            break


def add_user():
    username = input("username = ")
    password = input("password = ")
    email = input("email = ")

    user = User()
    user.username = username
    user.password = password
    user.email = email

    user.save()


if __name__ == "__main__":
    setup()
    print_header()
    user_loop()
