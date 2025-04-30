# db/session.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base as declarative_base

from os import getenv

DATABASE_URL = "postgresql://clean_hub_user:XTHpGpyUwRcSIGwbuP8qLyxwDkyZ5LZO@dpg-d08n7ch5pdvs739mn9ig-a.ohio-postgres.render.com/clean_hub" # TODO: Set this according to the proper URL

print("DATABASE_URL", DATABASE_URL)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()