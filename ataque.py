from tipo import Tipo

class Ataque:
    def __init__(self, nome: str, tipo: Tipo, dano: int, custo: int):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.custo = custo

    def getNome(self):
        return self.nome

    def getDano(self):
        return self.dano

    def getCusto(self):
        return self.custo

    def getTipo(self):
        return self.tipo
