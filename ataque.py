import tipo

class Ataque:
    def __init__(self, nome: str, tipo: Tipo, dano: int, custo: int):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.custo = custo
