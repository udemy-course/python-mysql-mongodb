from datetime import datetime
import json

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class Movie(BASE):

    __tablename__ = 'movie'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(100), nullable=False)
    title_year = sa.Column(sa.Integer, nullable=False)
    director_name = sa.Column(sa.String(50), nullable=False)
    actor_1_name = sa.Column(sa.String(50), nullable=False)
    actor_2_name = sa.Column(sa.String(50), nullable=False)
    duration = sa.Column(sa.Integer, nullable=False)
    country = sa.Column(sa.String(50), nullable=False)
    content_rating = sa.Column(sa.String(10), nullable=False)
    gross = sa.Column(sa.BigInteger, nullable=False)
    imdb_score = sa.Column(sa.Float)

    def __repr__(self):
        return "title={}, director_name={}, imdb_score={}".format(
            self.title, self.director_name, self.imdb_score
        )


engine = sa.create_engine("mysql+pymysql://root:root@localhost:3306/demo", echo=True)
Session = sa.orm.sessionmaker(bind=engine)

BASE.metadata.create_all(engine)

s = Session()

# insert all data in movie.json

with open('movie.json') as f:
    movie_list = json.load(f)
    for movie in movie_list:
        m = Movie(**movie)
        s.add(m)
s.commit()

# find out imdb score top 10 movie

top10 = s.query(Movie).order_by(Movie.imdb_score.desc()).limit(10)

for m in top10:
    print(m)

s.close()
