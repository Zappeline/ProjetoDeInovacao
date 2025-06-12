class Semanas:
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco
        self.dono = None

def dividir_em_semanas_imv2(self):
        semanas = []
        for i in range(1, 53):
            if 48 <= i <= 52 or 1 <= i <= 8:  # Alta temporada: dezembro a fevereiro (13 semanas) T=1365000
                preco2 = 337209.30  # Alta temporada: dezembro a fevereiro (13 semanas)
            else:
                preco2 = 28622.54 # Baixa temporada: março a novembro (39 semanas)
            semanas.append(Semanas(i, preco2))
        return semanas    
print(dividir_em_semanas_imv2())  # Exemplo de chamada da função, substitua por uma instância real se necessário