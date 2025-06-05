class Imoveis:
    def __init__(self, id: int, tipo: str, endereco: str, preco: float, quartos: int, banheiros: int, area: str, avaliacao: str):
        self.id = id
        self.tipo = tipo
        self.endereco = endereco
        self.preco = preco
        self.quartos = quartos
        self.banheiros - banheiros
        self.area = area
        self.avaliacao = avaliacao

    def __str__(self):
        return f"Imóvel(id={self.id}, Tipo:{self.tipo}, Endereço:{self.endereco}, Preço={self.preco})"

    def __repr__(self):
        return self.__str__()   
    
