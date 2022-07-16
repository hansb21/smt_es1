from entidade import Entidade
from item import Item
from team import Time
class Jogador:
    def __init__(self, time: Time, seuTurno: bool, vencedor: bool, jogando: bool, itens: list, turnos: int, ataques: list):
        self.time = time
        self.seuTurno = seuTurno
        self.vencedor = vencedor
        self.jogando = jogando
        self.itens = itens
        self.turnos = turnos
        self.ataques = ataques

    def incluirEntidade(self, entidade: Entidade) -> None:
        self.time.reserva.append(entidade)

    def defineOrdemEntidades(self) -> None:
        pass

    def getTodosItens(self) -> list:
        return self.itens
    
    def getItem(self, index: int) -> Item:
        return self.itens[index]

    def usarItem(self, itemIndex: int, local: int, entidadeIndex: int) -> None:
        pass

    def diminuiQtdItem(self, index: int) -> None:
        pass

    def getTimeInteiro(self) -> list:
        return self.time.getTimeInteiro()

    def getReserva(self) -> list:
        return self.time.getReserva()

    def getCampo(self) -> list:
        return self.time.getCampo()

    def invocar(self, index: int, vazio: bool) -> None:
        pass

    def diminuiTurnos(self, qtd: int) -> None:
        self.turnos -= qtd

    def getTurnos(self) -> int:
        return self.turnos

    def mudaEntidadeAtual(self) -> None:
        pass

    def getAtaques(self) -> list:
        return self.ataques

    def getMpAtual(self, entidadeIndex: int) -> int:
        return self.time.getMpAtual(entidadeIndex)

    def getTipoEntidade(self,local: int, entidadeIndex: int) -> Tipo:
        return self.time.getTipoEntidade(local, entidadeIndex)

    def causarDano(self, modificador: float, danoBase: int, entidadeIndex: int) -> None:
        pass

    def ataqueAbsorvido(self, entidadeIndex: int, danoBase: int) -> None:
        pass

    def diminuirMp(self, entidadeIndex: int, qtd: int) -> None:
        pass

    def fusao(self, local1: int, entidadeIndex1: int,local1: int, entidadeIndex2: int, novoDemonio: Entidade, novoLocal: int, novoIndex: int) -> None:
        pass
    
    def setVencedor(self, vencedor: bool) -> None:
            pass

