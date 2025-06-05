class Semanas:
    def __init__(self, semana: int):
        if semana < 1 or semana > 52:
            return ValueError("Semana deve estar entre 1 e 52")
        self.semana = semana

    
