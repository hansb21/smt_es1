from entidade import Entidade
from item import Item
from team import Time
from tipo import Tipo
class Jogador:
    def __init__(self, nome: str, time: Time, seuTurno: bool, vencedor: bool, jogando: bool, itens: list, turnos: int):
        self.nome = nome
        self.time = time
        self.seuTurno = seuTurno
        self.vencedor = vencedor
        self.jogando = jogando
        self.itens = itens
        self.turnos = turnos

    def getTodosItens(self) -> list:
        return self.itens

    def getTimeInteiro(self) -> list:
        return self.time.getTimeInteiro()

    def getReserva(self) -> list:
        return self.time.getReserva()

    def getCampo(self) -> list:
        return self.time.getCampo()

    def getHumano(self) -> Entidade :
        return self.time.getHumano()

    def diminuiTurnos(self, qtd: int) -> None:
        self.turnos -= qtd

    def setTurnos(self, qtd: int) -> None:
        self.turnos = qtd

    def getTurnos(self) -> int:
        return self.turnos

    def getNome(self):
        return self.nome

    def restore(self):
        self.time.restore()
        for i in self.itens:
            i.restore()
        self.turnos = 10

    def getHumano(self):
        return self.time.getHumano()

