import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'frac_invest.db')

engine = create_engine(f'sqlite:///{DATABASE_PATH}', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def get_session():
    return Session()