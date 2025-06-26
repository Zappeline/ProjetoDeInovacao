import re

def is_cpf_valido(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, str(cpf)))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False

    return True

def is_nome_valido(nome: str) -> tuple[bool, str]:
    if not nome or not nome.strip():
        return False,
    if len(nome.strip()) < 3:
        return False, 
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", nome.strip()):
        return False, 
    return True, ""

def is_contato_valido(contato: str) -> tuple[bool, str]:
    if not contato or not contato.strip():
        return False, 
    return True, ""

