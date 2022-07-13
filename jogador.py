from team import Time
from item import Item
class Jogador:
    def __init__(self, time: Time, seuTurno: bool, vencedor: bool, jogando: bool, itens: list, turnos: int):
        self.time = time,
        self.seuTurno = seuTurno,
        self.vencedor = vencedor,
        self.jogando = jogando,
        self.itens = itens,
        self.turnos = turnos

    def incluirEntidade(entidade: Entidade) -> None:
        pass

    def defineOrdemEntidades() -> None:
        pass

    def getTodosItens() -> list:
        pass
    
    def getItem(index: int) -> Item:
        pass

    def usarItem(itemIndex: int, local: int, entidadeIndex: int) -> None:
        pass

    def diminuiQtdItem(index: int) -> None:
        pass

    def getTimeInteiro() -> list:
        return self.time.getTimeInteiro()

    def getReserva() -> list:
        return self.time.getReserva()

    def getCampo() -> list:
        return self.time.getCampo()

    def invocar(index: int, vazio: bool) -> None:
        pass

    def diminuiTurnos(qtd: int) -> None:
        self.turnos -= qtd

    def getTurnos() -> int:
        return self.turnos

    def mudaEntidadeAtual() -> None:
        pass

    def getAtaques() -> list:
        pass

    def getMpAtual(entidadeIndex: int) -> int:
        pass

    def getTipoEntidade(local: int, entidadeIndex: int) -> Tipo:
        pass

    def causarDano(modificador: float, danoBase: int, entidadeIndex: int) -> None:
        pass

    def ataqueAbsorvido(entidadeIndex: int, danoBase: int) -> None:
        pass

    def diminuirMp(entidadeIndex: int, qtd: int) -> None:
        pass

    def fusao(local1: int, entidadeIndex1: int,local1: int, entidadeIndex2: int, novoDemonio: Entidade, novoLocal: int, novoIndex: int) -> None:
        pass
    
    def setVencedor(vencedor: bool) -> None:
            pass

