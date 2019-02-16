from table import User, Tweet, Session


s = Session()

# insert user

# u = User(
#     username="test1",
#     password="test1",
#     email="test1@test1.com"
# )
# s.add(u)
# s.commit()

# t = Tweet(tweet="this is test1", user_id=1)
# s.add(t)
# s.commit()


# insert user and tweet

# u = User(
#     username='test2',
#     password='test2',
#     email='test2@test2.com'
# )
# s.add(u)

# s.commit()

u = s.query(User).filter(User.username == 'test2').first()

if u:
    t = Tweet(tweet='this is test2 again again', user_id=u.id)
    s.add(t)
    s.commit()
else:
    print('use does not exist')

s.close()
