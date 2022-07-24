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

    def incluirEntidade(self, entidade: Entidade) -> None:
        self.time.reserva.append(entidade)

    def defineOrdemEntidades(self) -> None:
        self.time.ordenaLista()

    def getTodosItens(self) -> list:
        return self.itens
    
    def getItem(self, index: int) -> Item:
        return self.itens[index]

    def usarItem(self, itemIndex: int, local: int, entidadeIndex: int) -> None:
        self.time.usarItem(local, entidadeIndex, self.itens[itemIndex].tipoItem, self.itens[itemIndex].potencia)
        
    def diminuiQtdItem(self, index: int) -> None:
        self.itens[index].diminuiQtd()

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

    def mudaEntidadeAtual(self) -> None:
        self.time.entidadeAtual = self.time.campo[self.time.campo.index(self.time.entidadeAtual)+1]

    def getAtaques(self) -> list:
        return self.ataques

    def getMpAtual(self, entidadeIndex: int) -> int:
        return self.time.getMpAtual(entidadeIndex)

    def getTipoEntidade(self,local: int, entidadeIndex: int) -> Tipo:
        return self.time.getTipoEntidade(local, entidadeIndex)

    def causarDano(self, modificador: float, danoBase: int, entidadeIndex: int) -> None:
        self.time.causarDano(modificador, danoBase, entidadeIndex)

    def ataqueAbsorvido(self, entidadeIndex: int, danoBase: int) -> None:
        self.time.ataqueAbsorvido(entidadeIndex, danoBase)

    def diminuirMp(self, entidadeIndex: int, qtd: int) -> None:
        self.time.diminuirMp(qtd, entidadeIndex)

    def fusao(self, local1: int, entidadeIndex1: int,local2: int, entidadeIndex2: int, novoDemonio: Entidade, novoLocal: int, novoIndex: int) -> None:
        self.time.fusao(local1, entidadeIndex1, local2, entidadeIndex2, novoDemonio, novoLocal, novoIndex)
    
    def setVencedor(self, vencedor: bool) -> None:
            self.vencedor = vencedor

    def getNome(self):
        return self.nome

    def restore(self):
        self.time.restore()
        for i in self.itens:
            i.restore()

    def getHumano(self):
        return self.time.getHumano()

