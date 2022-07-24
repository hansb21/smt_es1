#from ast import Str
from inspect import _void
from tipo import Tipo
from ataque import *

class Entidade:
    def __init__(self, nome : str, tipo: Tipo, ataques: list[Ataque],
                 hp: int, mp: int, forca: int, defesa: int, 
                 sorte: int, ehHumano: bool, local: int, imagem):
        self.nome = nome
        self.tipo = tipo
        self.ataques = ataques
        self.vivo = True
        self.hp = hp
        self.hpMax = hp
        self.mpMax = mp
        self.mp = mp
        self.forca = forca
        self.defesa = defesa
        self.sorte = sorte
        self.ehHumano = ehHumano
        self.local = local
        self.imagem = imagem
    
    def name(self):
        return self.nome

    def getImagem(self):
        return self.imagem

    def modificarVida(self, qtd: int) -> None:
        if (self.vivo):
            if qtd > 0:
                self.hp += qtd
                if (self.hp > self.hpMax):
                    self.hp = self.hpMax
            else:
                self.hp += round(qtd - self.defesa)
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
        if not (self.vivo):
            self.hp = qtd
            if self.hp > self.hpMax:
                self.hp = self.hpMax
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

    def getHpMax(self) -> int :
        return self.hpMax

    def getMpAtual(self) -> int :
        return self.mp

    def getLocal(self) -> int :
        return self.local

    def setLocal(self, novo) -> None :
        self.local = novo

    def getEhHumano(self) -> bool :
        return self.ehHumano

    def getVivo(self) -> bool :
        return self.vivo

    def getParamsFusao(self):
        return [self.nome,
                self.tipo,
                self.ataques,
                self.hp,
                self.mp,
                self.forca,
                self.defesa,
                self.sorte,
                self.ehHumano,
                self.local,
                self.imagem]

    def restore(self):
        self.vivo = True
        self.hp = self.hpMax
        self.mp = self.mpMax
