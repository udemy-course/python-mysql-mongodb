import sqlalchemy as sa

from movie import Movie, BASE


engine = sa.create_engine("mysql+pymysql://root:root@localhost:3306/demo", echo=True)
Session = sa.orm.sessionmaker(bind=engine)

BASE.metadata.create_all(engine)

s = Session()

# SELECT 
#     director_name, COUNT(title)
# FROM movie GROUP BY director_name ORDER BY COUNT(title) DESC LIMIT 10;

m1 = s.query(
    Movie.director_name, sa.func.count(Movie.title)
).group_by(Movie.director_name).order_by(sa.func.count(Movie.title).desc()).limit(10)

for m in m1:
    print(m)

# SELECT
#     director_name, SUM(gross)
# FROM movie GROUP BY director_name ORDER BY SUM(gross) DESC LIMIT 10;

m2 = s.query(
    Movie.director_name,
    sa.func.sum(Movie.gross)
).group_by(Movie.director_name).order_by(sa.func.sum(Movie.gross).desc()).limit(10)

for m in m2:
    print(m)
