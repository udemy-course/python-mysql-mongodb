import mongoengine

from user import User, Address, Hobby


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
        print(" * [u]pdate password")
        print(" * [d]elete user")
        print(" * e[x]it")
        print()
        ch = input("> ").strip().lower()
        if ch == 'a':
            add_user()
        elif ch == 'l':
            list_users()
        elif ch == 'u':
            update_users()
        elif ch == 'd':
            delete_users()
        elif not ch or ch == 'x':
            print("Goodbye")
            break


def add_user():
    username = input("username = ")
    password = input("password = ")
    email = input("email = ")
    age = input("age = ")
    city = input("city = ")
    zip_code = input("zip code = ")

    user = User()
    user.username = username
    user.password = password
    user.email = email
    user.age = age

    addr = Address()
    addr.city = city
    addr.zip_code = zip_code

    user.address = addr

    h1 = Hobby()
    h1.type = 'running'
    h1.rating = 7

    user.hobbies = [h1]

    user.save()


def list_users():
    # users = User.objects(age__in=[25, 28])
    # users = User.objects(address__city="ShangHai")
    # users = User.objects(hobbies__match={'type': 'reading'})
    # users = User.objects()[2:4]

    users = User.objects()
    for user in users:
        print('username={}, passwd={}, age={}'.format(
            user.username, user.password, user.age))


def update_users():
    username = input('username = ')
    user = User.objects(username=username).first()
    if not user:
        print('user does not exist')
        return
    password = input('new password = ')
    user.password = password
    user.save()


def delete_users():
    username = input('username = ')
    user = User.objects(username=username).first()
    if not user:
        print('user does not exist')
        return
    user.delete()   


if __name__ == "__main__":
    setup()
    print_header()
    user_loop()
