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


engine = sa.create_engine("mysql+pymysql://root:root@localhost:3306/demo")
session = sa.orm.sessionmaker(bind=engine)

BASE.metadata.create_all(engine)
