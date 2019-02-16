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
