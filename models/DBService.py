from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.Usuarios import Usuarios, Base

# Conectar ao banco
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

