from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from database import engine

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    contato = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)

    transacoes = relationship("Transacao", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', cpf='{self.cpf}')>"

class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(50), nullable=False)
    endereco = Column(String(255), nullable=False)
    preco_total = Column(Float, nullable=False)
    quartos = Column(Integer)
    banheiros = Column(Integer)
    area = Column(String(50))
    avaliacao = Column(String(50))

    semanas = relationship("Semana", back_populates="imovel")

    def __repr__(self):
        return f"<Imovel(id={self.id}, tipo='{self.tipo}', endereco='{self.endereco}')>"

class Semana(Base):
    __tablename__ = "semanas"

    id = Column(Integer, primary_key=True)
    imovel_id = Column(Integer, ForeignKey('imoveis.id'), nullable=False)
    numero_semana = Column(Integer, nullable=False)
    periodo = Column(String(50), nullable=False)
    valor_cota = Column(Float, nullable=False)
    disponivel = Column(Integer, default=1)
    dono_id = Column(Integer, ForeignKey('usuarios.id'), nullable=True)

    imovel = relationship("Imovel", back_populates="semanas")
    dono = relationship("Usuario")

    def __repr__(self):
        return f"<Semana(id={self.id}, imovel_id={self.imovel_id}, semana={self.numero_semana}, valor={self.valor_cota}, disponivel={self.disponivel})>"

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    semana_id = Column(Integer, ForeignKey('semanas.id'), nullable=False, unique=True)
    data_compra = Column(String(50), nullable=False)
    valor_pago = Column(Float, nullable=False)

    usuario = relationship("Usuario", back_populates="transacoes")
    semana = relationship("Semana")

    def __repr__(self):
        return f"<Transacao(id={self.id}, usuario_id={self.usuario_id}, semana_id={self.semana_id}, valor={self.valor_pago})>"

Base.metadata.create_all(engine)