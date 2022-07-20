from entidade import Entidade
from tipo import Tipo

class Time:
    def __init__(self, humano: Entidade, campo: list, reserva: list):
        self.humano = humano
        self.campo = campo
        self.reserva = reserva
        self.entidadeAtual = 0

    def ordenaLista(self) -> None:
        self.campo = sorted(self.campo, key=lambda x: x.velocidade)

    def incluirEntidade(self, demonio: Entidade) -> None:

        if (demonio.ehHumano):
            self.campo.append(demonio)
        else:
            self.reserva.append(demonio)
        
    def invocar(self, entidadeIndex1: int, entidadeIndex2: int, vazio: bool) -> None:
        
        tempReserva = self.removerDemonio(1, entidadeIndex1)
        if not (vazio):
            tempCampo = self.removerDemonio(0, entidadeIndex1)
            self.incluirNovo(tempReserva, 0, entidadeIndex2)
            self.incluirNovo(tempCampo, 1, entidadeIndex2)
        else:
            self.incluirNovo(tempReserva, 0, entidadeIndex2)

    def getTimeInterior(self) -> list:
        self.campo.append(self.reserva)
        return self.campo

    def usarItem(self, local: int, entidadeIndex: int, tipo: str, itemPower:int) -> None:

        if (local == 0):
            alvo = self.campo[entidadeIndex]
        else:
            alvo = self.reserva[entidadeIndex]

        if tipo == "hp":
            if (alvo.hp < alvo.hpMax) and (alvo.hp > 0):
                alvo.hp += itemPower
                if (alvo.hp) >= alvo.hpMax:
                    alvo.hp = alvo.hpMax

        elif tipo == "mp":
            if (alvo.mp < alvo.mpMax) and (alvo.mp > 0):
                alvo.mp += itemPower
                if (alvo.mp) >= alvo.mpMax:
                    alvo.mp = alvo.mpMax
        else:
            if (alvo.hp == 0) and not (alvo.vivo):
                alvo.vivo = True
                alvo.hp = itemPower

    def mudaEntidadeAtual(self) -> None:
        self.entidadeAtual += 1
        if (self.entidadeAtual >= len(self.campo)):
                entidadeAtual = 0

    def getAtaques(self, entidadeIndex: int) -> list:
        return self.campo[entidadeIndex].ataques

    def getMpAtual(self, entidadeIndex: int) -> int:
        return self.campo[entidadeIndex].mp

    def getReserva(self) -> list:
        return self.reserva

    def getCampo(self) -> list:
        return self.campo

    def getHumano(self) -> Entidade:
        return self.humano

    def getTipoEntidade(self, local: int, entidadeIndex: int) -> Tipo:
        if (local == 0):
            return self.campo[entidadeIndex].tipo 
        else:
            return (self.reserva[entidadeIndex].tipo) 
    
    def causarDano(self, modificador: float, danoBase: int, entidadeIndex: int) -> None:

        danoTotal = round(danoBase * modificador)
        alvo = self.campo[entidadeIndex]
        alvo.modificarVida(danoTotal)

    def ataqueAbsorvido(self, entidadeIndex: int, danoBase: int) -> None:

        alvo = self.campo[entidadeIndex]
        alvo.modificarVida(danoBase)

    def diminuirMp(self, qtd: int, entidadeIndex: int) -> None:
        self.campo[entidadeIndex].mp -= qtd
        if self.campo[entidadeIndex].mp < 0:
                self.campo[entidadeIndex].mp = 0

    def fusao(self, local1: int, entidadeIndex1: int, local2: int, entidadeIndex2: int, novoDemonio: Entidade, novoLocal: int, novoIndex: int) -> None:

        self.removerDemonio(local1, entidadeIndex1)
        self.removerDemonio(local2, entidadeIndex2)
        self.incluirNovo(novoDemonio=novoDemonio, local=novoIndex, index=novoIndex)    

    def removerDemonio(self, local: int, entidadeIndex: int) -> Entidade:
        if local == 0:
            alvo = self.campo[entidadeIndex]
            self.campo[entidadeIndex] = None
            return alvo
        else:
            alvo = self.reserva[entidadeIndex]
            self.reserva[entidadeIndex] = None
            return alvo
    def incluirNovo(self, novoDemonio: Entidade, local: int, index: int) -> None:
        if local == 0:
            if self.campo[index] != None:
                self.removerDemonio(local, index)
            
            self.campo[index] = novoDemonio
        else:
            if self.reserva[index] != None:
                self.removerDemonio(local, index)

            self.campo[index] = novoDemonio

