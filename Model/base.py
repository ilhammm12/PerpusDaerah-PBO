from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
db_path = os.path.join(os.path.dirname(__file__), 'Perpustakaan.db')
db_uri = 'sqlite:///{}'.format(db_path)
engine = create_engine(db_uri)


_SessionFactory = sessionmaker(bind=engine)

connection = engine.connect()

def sessionFactory():
    Base.metadata.create_all(engine)
    return _SessionFactory()