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

def modificarVida(qtd: int) -> None:
        pass

    def modificarMagia(qtd: int) -> None:
        pass

    def reviver(qtd: int) -> None:
        pass

    def getAtaques() -> list :
        return self.ataques

    def getTipoEntidade() -> Tipo :
        return self.tipo

    def getEhHumano() -> bool :
        return self.ehHumano
    
    def getHpAtual() -> int :
        return self.hp

