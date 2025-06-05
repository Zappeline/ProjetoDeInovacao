class SistemaTransacao:
    def __init__(self, preco_total):
        self.preco_total = preco_total
    
    
    def dividir_em_semanas(self):
        semanas = []
        for i in range(1, 53):
            if 48 <= i <= 52 or 1 <= i <= 8:  # Alta temporada: dezembro a fevereiro
                preco = self.preco_total * 0.03
            else:
                preco = self.preco_total * 0.015
            semanas.append(Semana(i, preco))
        return semanas