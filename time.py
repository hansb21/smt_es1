from entidade import Entidade

class Time:
    def __init__(self, humano: Entidade, campo: list, reserva: list, entidadeAtual: int):
        self.humano = humano
        self.campo = campo
        self.reserva = reserva
        self.entidadeAtual = entidadeAtual

    def ordenaLista() -> None:
        pass

    def incluirEntidade(demonio: Entidade) -> None:
        pass

    def invocar(index: int, vazio: bool) -> None:
        pass

    def getTimeInterior() -> list:
        return self.campo.append(self.reserva)  
    def usarTime(local: int, entidadeIndex: int, tipo: str, itemPower:int) -> None:
        pass

    def mudaEntidadeAtual() -> None:
        pass

    def getAtaques(entidadeIndex: int) -> list:
        pass

    def getMpAtual(entidadeIndex: int) -> int:
        pass

    def getReserva() -> list:
        return self.reserva

    def getCampo() -> list:
        return self.campo

    def getTipoEntidade(local: int, entidadeIndex: int): -> Tipo:
        pass
    
    def causarDano(modificador: float, danoBase: int, entidadeIndex: int) -> None:
        pass

    def ataqueAbsorvido(entidadeIndex: int, danoBase: int) -> None:
        pass

    def diminuirMp(qtd: int, entidadeIndex: int) -> None:
        pass

    def fusao(local1: int, entidadeIndex1: int, local2: int, entidadeIndex2: int, novoDemonio: Entidade, novoLocal: int, novoIndex: int) -> None:
        pass

    def removerDemonio(local: int, entidadeIndex: int) -> None:
        pass

    def incluirNovo(novoDemonio: Entidade, local: int, index: int) -> None:
        pass
