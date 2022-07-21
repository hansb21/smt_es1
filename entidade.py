#from ast import Str
from tipo import Tipo
from ataque import *

class Entidade:
    def __init__(self, nome : str, tipo: Tipo, ataques: list[Ataque],
                 hp: int, hpMax:int, mpMax: int, mp: int, forca: int, defesa: int, 
                 sorte: int, ehHumano: bool, local: int, imagem):
        self.nome = nome
        self.tipo = tipo
        self.ataques = ataques
        self.vivo = True
        self.hp = hp
        self.hpMax = hpMax #já podemos pensar em algum valor fixo
        self.mpMax = mpMax
        self.mp = mp
        self.forca = forca
        self.defesa = defesa
        self.sorte = sorte
        self.ehHumano = ehHumano
        self.local = local
        self.imagem = imagem

    def getImagem(self):
        return self.imagem

    def modificarVida(self, qtd: int) -> None:
        if (self.vivo):
            if qtd > 0:
                self.hp += qtd
                if (self.hp > self.hpMax):
                    self.hp = self.hpMax
            else:
                self.hp += round(qtd/self.defesa)
                if self.hp <= 0:
                    self.vivo = False
                    self.hp = 0

    def modificarMagia(self, qtd: int) -> None:
        if (self.vivo):
            self.mp += qtd
            if (self.mp > self.mpMax):
                self.mp = self.mpMax
            elif self.mp < 0:
                self.mp = 0

    def reviver(self, qtd: int) -> None:
        if (self.vivo):
            self.hp = qtd
            self.vivo = True

    def getNome(self) -> str :
        return self.nome

    def getAtaques(self) -> list :
        return self.ataques

    def getTipo(self) -> Tipo :
        return self.tipo

    def getEhHumano(self) -> bool :
        return self.ehHumano

    def getHpAtual(self) -> int :
        return self.hp

    def getMpAtual(self) -> int :
        return self.mp

