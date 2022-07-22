#from ast import Str


class Item:
    def __init__(self, nome: str, tipoItem: str, potencia: int, qtd: int):
        self.nome = nome
        self.tipoItem = tipoItem
        self.potencia = potencia
        self.qtd = qtd

    def getNome(self) -> str :
        return self.nome

    def getPotencia(self) -> int :
        return self.potencia

    def getQtd(self) -> int:
        return self.qtd

    def getTipo(self) -> str:
        return self.tipoItem

    def diminuiQtd(self) -> None:
            self.qtd -= 1
