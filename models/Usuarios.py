'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.DBService import engine
base = declarative_base()

class Usuarios(base):
  
    __tablename__= 'usuarios'
    id = Column (Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    contato = Column(String(15), nullable=False)
    semanas_adquiridas = Column(int, nullable=True, unique=True)
    aluguel_semana = Column(Integer, nullable=False)
    # Criar uma sessão
    Session = sessionmaker(bind=engine)
    session = Session()

    def cadastrar_usuarios(nome:str ,cpf: int,contato:str,):
        novo_usuario = Usuarios(nome=nome, cpf=cpf, contato=contato)
        session.add(novo_usuario)
        session.commit()
        return novo_usuario
'''
    
        
   