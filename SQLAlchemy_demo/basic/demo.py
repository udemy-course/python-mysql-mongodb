from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class User(BASE):

    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(64), unique=True)
    password = sa.Column(sa.String(64))
    email = sa.Column(sa.String(128), unique=True)
    create_at = sa.Column(sa.DateTime, server_default=sa.func.now())

    def __repr__(self):
        return "id={}, username={}, email={}".format(
            self.id, self.username, self.email
        )


engine = sa.create_engine("mysql+pymysql://root:root@localhost:3306/demo", echo=False)
Session = sa.orm.sessionmaker(bind=engine)

BASE.metadata.create_all(engine)

#---------------------------------------------------------------------------
#                             Data  Insert
#---------------------------------------------------------------------------
# user1 = User(username='test1', password='test1', email='test1@test1.com')
# user2 = User(username='test2', password='test2', email='test2@test2.com')
# session = Session()
# session.add_all([user1, user2])
# session.commit()


#---------------------------------------------------------------------------
#                             Data  Query
#---------------------------------------------------------------------------

# s = Session()
# users = s.query(User)
# for u in users:
#     print(u)

# s = Session()
# users = s.query(User).filter(User.username == 'test1')
# for u in users:
#     print(u)

# s = Session()
# users = s.query(User).order_by(User.id.desc())
# for u in users:
#     print(u)

# s = Session()
# users = s.query(User).all()
# print(users)

# s = Session()
# users = s.query(User).filter(User.username == 'abc').first()

# if users:
#     print('user name exist')
#     pass
# else:
#     pass

# s = Session()
# users = s.query(User).order_by(User.id.desc()).limit(3).all()
# print(users)
# s.close()

# s = Session()
# users = s.query(User).filter(User.username.like("%est1%"))
# for u in users:
#     print(u)

# SELECT columns

# mysql> select id, username from user;
# +----+----------+
# | id | username |
# +----+----------+
# |  1 | test1    |
# |  2 | test2    |
# |  3 | test3    |
# |  4 | test4    |
# |  5 | test5    |
# |  6 | test6    |
# |  7 | test7    |
# |  9 | test8    |
# |  8 | test9    |
# +----+----------+
# 9 rows in set (0.00 sec)

# s = Session()

# u1 = s.query(User)
# for u in u1:
#     print(u, type(u))

# u2 = s.query(User.id, User.username)
# for u in u2:
#     print(u, type(u))




#---------------------------------------------------------------------------
#                             Data  Update
#---------------------------------------------------------------------------

# s = Session()
# u = s.query(User).filter(User.username == 'test1').first()
# print(u.password)
# u.password = 'test222'
# u.email = '2222@111.com'
# s.commit()
