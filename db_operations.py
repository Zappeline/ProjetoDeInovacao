from database import get_session, engine, Base
from models import Usuario, Imovel, Semana, Transacao
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from datetime import datetime

Base.metadata.create_all(engine)

def criar_usuario_db(nome, cpf, contato, senha):
    session = get_session()
    try:
        usuario_existente = session.query(Usuario).filter_by(cpf=cpf).first()
        if usuario_existente:
            return None, "CPF já cadastrado."

        novo_usuario = Usuario(nome=nome, cpf=cpf, contato=contato, senha=senha)
        session.add(novo_usuario)
        session.commit()
        return novo_usuario, "Usuário cadastrado com sucesso!"
    except IntegrityError as e:
        session.rollback()
        return None, f"Erro de integridade: {e}. Certifique-se de que o CPF é único."
    except Exception as e:
        session.rollback()
        return None, f"Erro ao criar usuário: {e}"
    finally:
        session.close()

def verificar_login_db(cpf, senha):
    session = get_session()
    try:
        usuario = session.query(Usuario).filter_by(cpf=cpf).first()
        if usuario and usuario.senha == senha:
            return usuario
        return None
    finally:
        session.close()

def atualizar_contato_usuario_db(usuario_id, novo_contato):
    session = get_session()
    try:
        usuario = session.query(Usuario).filter_by(id=usuario_id).first()
        if usuario:
            usuario.contato = novo_contato
            session.commit()
            return True, "Contato atualizado com sucesso!"
        return False, "Usuário não encontrado."
    except Exception as e:
        session.rollback()
        return False, f"Erro ao atualizar contato: {e}"
    finally:
        session.close()

def get_semanas_disponiveis(imovel_id):
    session = get_session()
    try:
        semanas = session.query(Semana).filter_by(imovel_id=imovel_id, disponivel=1).all()
        return semanas
    finally:
        session.close()

def comprar_semana_db(usuario_id, semana_id):
    session = get_session()
    try:
        semana = session.query(Semana).filter_by(id=semana_id, disponivel=1).first()
        if not semana:
            return False, "Semana não disponível ou não encontrada."

        semana.disponivel = 0
        semana.dono_id = usuario_id

        nova_transacao = Transacao(
            usuario_id=usuario_id,
            semana_id=semana_id,
            data_compra=datetime.now().strftime("%d-%m-%y %H:%M:%S"),
            valor_pago=semana.valor_cota
        )
        session.add(nova_transacao)
        session.commit()
        return True, "Compra realizada com sucesso!"
    except IntegrityError:
        session.rollback()
        return False, "Esta semana já foi comprada."
    except Exception as e:
        session.rollback()
        return False, f"Erro ao comprar semana: {e}"
    finally:
        session.close()

def desfazer_compra_semana_db(usuario_id, semana_id):
    session = get_session()
    try:
        transacao = session.query(Transacao).filter_by(usuario_id=usuario_id, semana_id=semana_id).first()
        if not transacao:
            return False, "Transação não encontrada para esta semana e usuário."

        semana = session.query(Semana).filter_by(id=semana_id, dono_id=usuario_id).first()
        if not semana:
            return False, "Semana não encontrada ou não pertence a este usuário."

        semana.disponivel = 1
        semana.dono_id = None

        session.delete(transacao)
        session.commit()
        return True, "Semana disponibilizada para venda novamente!"
    except Exception as e:
        session.rollback()
        return False, f"Erro ao disponibilizar semana: {e}"
    finally:
        session.close()

def get_transacoes_usuario_db(usuario_id):
    session = get_session()
    try:
        transacoes = session.query(Transacao)\
                            .filter(Transacao.usuario_id == usuario_id)\
                            .options(joinedload(Transacao.semana).joinedload(Semana.imovel))\
                            .all()
        return transacoes
    finally:
        session.close()
def inicializar_dados_imoveis():
    session = get_session()
    try:
        if session.query(Imovel).count() == 0:
            imovel1 = Imovel(
                id=1,
                tipo="Residencial",
                endereco="Av Atlântica, 3750 - Centro, Balneário Camboriú",
                preco_total=1365000.00,
                quartos=3,
                banheiros=2,
                area="120m²",
                avaliacao="Excelente"
            )
            session.add(imovel1)

            for i in range(1, 53):
                periodo_str = f"Semana {i}"
                if 48 <= i <= 52 or 1 <= i <= 8:
                    preco = 33720.93
                else:
                    preco = 25939.18
                semana = Semana(
                    imovel_id=imovel1.id,
                    numero_semana=i,
                    periodo=periodo_str,
                    valor_cota=preco,
                    disponivel=1
                )
                session.add(semana)

            imovel2 = Imovel(
                id=2,
                tipo="Hotel",
                endereco="Av Beira Mar, 1020 - Centro, Torres",
                preco_total=2000000.00,
                quartos=1,
                banheiros=1,
                area="40m²",
                avaliacao="Muito Bom"
            )
            session.add(imovel2)

            for i in range(1, 53):
                periodo_str = f"Semana {i}"
                if 48 <= i <= 52 or 1 <= i <= 8:
                    preco = 337209.30 / 10
                else:
                    preco = 28622.54
                semana = Semana(
                    imovel_id=imovel2.id,
                    numero_semana=i,
                    periodo=periodo_str,
                    valor_cota=preco,
                    disponivel=1
                )
                session.add(semana)

            imovel3 = Imovel(
                id=3,
                tipo="Residencial",
                endereco="Vigilante, 400 - Dutra, Gramado",
                preco_total=1800000.00,
                quartos=4,
                banheiros=3,
                area="180m²",
                avaliacao="Ótima Localização"
            )
            session.add(imovel3)

            for i in range(1, 53):
                periodo_str = f"Semana {i}"
                if 48 <= i <= 52 or 1 <= i <= 8:
                    preco = 40000.00
                else:
                    preco = 30000.00
                semana = Semana(
                    imovel_id=imovel3.id,
                    numero_semana=i,
                    periodo=periodo_str,
                    valor_cota=preco,
                    disponivel=1
                )
                session.add(semana)

            session.commit()
            print("Imóveis e semanas iniciais adicionados ao banco de dados.")
        else:
            print("Imóveis e semanas já existem no banco de dados. Pulando inicialização.")
    except Exception as e:
        session.rollback()
        print(f"Erro ao inicializar imóveis: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    inicializar_dados_imoveis()