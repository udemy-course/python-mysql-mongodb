from table import User, Tweet, Session
from sqlalchemy import outerjoin

s = Session()

"""
SELECT
  tweet
FROM tweet INNER JOIN user
ON user.id=tweet.user_id WHERE user.username="test2"
"""

ts = s.query(Tweet).join(
    User,
    User.id == Tweet.user_id
).filter(User.username == 'test2')

for t in ts:
    print(t)


s.close()