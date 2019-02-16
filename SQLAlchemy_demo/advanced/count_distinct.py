import sqlalchemy as sa

from movie import Movie, BASE


engine = sa.create_engine("mysql+pymysql://root:root@localhost:3306/demo", echo=True)
Session = sa.orm.sessionmaker(bind=engine)

BASE.metadata.create_all(engine)

s = Session()

# select count(*) from movie where director_name="Christopher Nolan";
# select count(*) from movie where actor_1_name="Tom Hardy" or actor_2_name="Tom Hardy";
# select count(distinct(director_name)) from movie; 

c1 = s.query(Movie).filter(Movie.director_name == "Christopher Nolan").count()
print(c1)


c2 = s.query(Movie).filter(
    sa.or_(Movie.actor_1_name == "Tom Hardy", Movie.actor_2_name == "Tom Hardy")
).count()

print(c2)

# distinct

c3 = s.query(
    sa.distinct(Movie.director_name)
)

for i in c3:
    print(i[0])

# distinct + count

c4 = s.query(
    sa.distinct(Movie.director_name)
).count()

print(c4)

s.close()