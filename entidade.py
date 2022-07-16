from tipo import Tipo
from ataque import *

class Entidade:
    def __init__(self, nome : str, tipo: Tipo, ataques: list[Ataque], vivo: bool, hp: int, hpMax:int, mpMax: int, mp: int, forca: int, defesa: int, sorte: int, ehHumano: bool, local: int ):
        self.nome = nome
        self.tipo = tipo
        self.ataques = ataques
        self.vivo = vivo
        self.hp = hp
        self.hpMax = hpMax #já podemos pensar em algum valor fixo
        self.mpMax = mpMax
        self.mp = mp
        self.forca = forca
        self.defesa = defesa
        self.sorte = sorte
        self.ehHumano = ehHumano
        self.local = local

    def modificarVida(self, qtd: int) -> None:
        if (self.vivo):
            self.hp += qtd
            if (self.hp > self.hpMax):
                self.hp = self.hpMax

    def modificarMagia(self, qtd: int) -> None:
        if (self.vivo):
            self.mp += qtd
            if (self.mp > self.mpMax):
                self.mp = self.mpMax

    def reviver(self, qtd: int) -> None:
        if (self.vivo):
            self.hp = qtd
            self.vivo = True

    def getAtaques(self) -> list :
        return self.ataques

    def getTipoEntidade(self) -> Tipo :
        return self.tipo

    def getEhHumano(self) -> bool :
        return self.ehHumano

    def getHpAtual(self) -> int :
        return self.hp

