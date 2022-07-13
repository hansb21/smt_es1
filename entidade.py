from tipo import *
from ataque import *

class Entidade:
    def __init__(self, nome : str, tipo: Tipo, ataques: list, hp: int, hpMax: int, mp: int, forca: int, defesa: int, sorte: int, ehHumano: bool, local: int ):
        self.nome = nome,
        self.tipo = tipo,
        self.ataques = ataques,
        self.hp = hp,
        self.hpMax = hpMax #já podemos pensar em algum valor fixo
        self.mp = mp,
        self.forca = forca,
        self.defesa = defesa,
        self.sorte = sorte,
        self.ehHumano = ehHumano,
        self.local = local

def modificarVida(self, qtd: int) -> None:
        pass

    def modificarMagia(self, self,qtd: int) -> None:
        pass

    def reviver(self, qtd: int) -> None:
        pass

    def getAtaques(self) -> list :
        return self.ataques

    def getTipoEntidade(self) -> Tipo :
        return self.tipo

    def getEhHumano(self) -> bool :
        return self.ehHumano
    
    def getHpAtual(self) -> int :
        return self.hp

