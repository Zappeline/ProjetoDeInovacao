"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Base.metadata.create_all(engine)
engine = create_engine(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Usuario(Base):

    
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key= True)
    nome = Column(String(50), nullable=False)
    contato = Column(String(50), nullable = False )
    cpf = Column(Integer(11), nullable = False, unique=True)
    senha = Column(String(50), nullable = False)
Session = sessionmaker(bind=engine)
session = Session()
def criar_usuarios(nome: str, contato: str, cpf: int, senha: str) -> 'Usuario':
    novo_usuario = Usuario(nome = nome, contato=contato,cpf=cpf,senha=senha)
    session.add(novo_usuario)
    session.commit
    return novo_usuario
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()




class Usuario(Base):

    
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key= True)
    nome = Column(String(50), nullable=False)
    contato = Column(String(50), nullable = False )
    cpf = Column(Integer, nullable = False, unique=True)
    senha = Column(String(50), nullable = False)
    def criar_usuarios(nome:str,contato:str,cpf:int,senha:str) -> 'Usuario':
        novo_usuario = Usuario(nome = nome, contato=contato,cpf=cpf,senha=senha)
        session.add(novo_usuario)
        session.commit
        return novo_usuario
   


