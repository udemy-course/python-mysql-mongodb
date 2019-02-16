from table import User, Tweet, Session


s = Session()

u = s.query(User).filter(User.username == "test2").first()

t = s.query(Tweet).filter(Tweet.user_id == u.id)

for tweet in t:
    print(tweet)

s.close()