from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func, \
    ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class User(BASE):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True)
    password = Column(String(64))
    email = Column(String(128), unique=True)
    create_at = Column(DateTime, server_default=func.now())

    tweets = relationship('Tweet')

    def __repr__(self):
        return "id={}, username={}, email={}".format(
            self.id, self.username, self.email
        )
    
class Tweet(BASE):

    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tweet = Column(String(140))

    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return 'tweet: {}'.format(self.tweet)


engine = create_engine("mysql+pymysql://root:root@localhost:3306/demo", echo=True)
Session = sessionmaker(bind=engine)


if __name__ == "__main__":

    BASE.metadata.create_all(engine)
