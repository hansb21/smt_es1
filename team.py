from entidade import Entidade
from tipo import Tipo

class Time:
    def __init__(self, humano: Entidade, campo: list, reserva: list):
        self.humano = humano
        self.campo = campo
        self.reserva = reserva
        self.entidadeAtual = 0

    def getTimeInteiro(self) -> list:
        inteiro = []
        for i in self.campo:
            inteiro.append(i)
        for i in self.reserva:
            inteiro.append(i)
        inteiro.append(self.humano)
        return inteiro

    def getReserva(self) -> list:
        return self.reserva

    def getCampo(self) -> list:
        return self.campo

    def getHumano(self) -> Entidade:
        return self.humano

    def restore(self):
        timeInteiro = self.getTimeInteiro()
        for i in timeInteiro:
            i.restore()

