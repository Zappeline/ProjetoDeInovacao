from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.Usuarios import Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# Conectar ao banco
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

base = declarative_base()
class Usuario(base):

    __tablename__ = Usuario
    id = Column(Integer, primary_key= True)
    nome = Column(String(50), nullable=False)
    contato = Column(String(50), nullable = False )
    cpf = Column(Integer(11), nullable = False, unique=True)
    senha = Column(String(50), nullable = False)
sessionmaker(bind=engine)
session = Session()
def criar_usuarios(nome:str,contato:str,cpf:int,senha:str) -> Usuario:
    novo_usuario = Usuario(Nome =)

    