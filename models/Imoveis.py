class Semanas:
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco
        self.dono = None
    

class Imoveis:
    def __init__(self, id: int, tipo: str, endereco: str, preco_total: float, quartos: int, banheiros: int, area: str, avaliacao: str):
        self.id = id
        self.tipo = tipo
        self.endereco = endereco
        self.preco_total = preco_total
        self.quartos = quartos
        self.banheiros - banheiros
        self.area = area
        self.avaliacao = avaliacao
        self.semanas = self.dividir_em_semanas()

    def __str__(self):
        return f"Imóvel(id={self.id}, Tipo:{self.tipo}, Endereço:{self.endereco}, , Quartos: {self.quartos}, Banheiros:{self.banheiros}, Área:{self.area} ,Preço:{self.preco_total}, Avaliação:{self.avaliacao})"

    def dividir_em_semanas_imv1(self):
        semanas = []
        for i in range(1, 53):
            if 48 <= i <= 52 or 1 <= i <= 8:  # Alta temporada: dezembro a fevereiro (13 semanas) T=1365000
                preco1 = 33720.93  # Alta temporada: dezembro a fevereiro (13 semanas)
            else:
                preco1 = 25939.18 # Baixa temporada: março a novembro (39 semanas)
            semanas.append(Semanas(i, preco1))
        return semanas    
    
    def dividir_em_semanas_imv2(self):
        semanas = []
        for i in range(1, 53):
            if 48 <= i <= 52 or 1 <= i <= 8:  # Alta temporada: dezembro a fevereiro (13 semanas) T=1365000
                preco2 = 337209.30  # Alta temporada: dezembro a fevereiro (13 semanas)
            else:
                preco2 = 28622.54 # Baixa temporada: março a novembro (39 semanas)
            semanas.append(Semanas(i, preco2))
        return semanas    
    