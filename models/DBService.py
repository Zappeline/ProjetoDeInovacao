"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.Usuarios import Base

# Conectar ao banco
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

"""

from models import Imoveis, Usuarios

ZenithPlace = Imoveis(1, "Casa", "Rua das Flores, 123", 1365000., 5, 3, "100m²", "9.7 - Excelente")
usuarios = [Usuarios(1, "João", 00000000000, 99999999999)]

banco_dados = {
    "imovel": Imoveis,
    "usuarios": usuarios
}
