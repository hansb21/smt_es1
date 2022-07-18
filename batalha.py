from jogador import *
from entidade import Entidade

class Batalha:
    def __init__(self):
        self.batalhaEmAndamento = False
        self.estagio = "Escolha1"
        self.jogadorAtual = None
        self.jogadorOutro = None
        self.todosHumanos = []
        self.demoniosEscolha = []
        self.demonioFusao = []

    def iniciar(self) -> None:
        pass

    def sorteiaJogador(self) -> None:
        pass
    
    def iniciarBatalha(self) -> None:
        pass

    def escolherHumanos(self) -> None:
        pass

    def getHumanos(self, index: int) -> Entidade:
        pass

    def incluirHumano1(self, escolha: Entidade) -> None:
        pass

    def incluirHumano2(self, escolha: Entidade) -> None:
        pass

    def escolherDemonios(self) -> None:
        pass

    def getDemonio(self, index: int) -> Entidade:
        pass

    def incluirDemonio1(self, escolha: Entidade) -> None:
        pass

    def incluirDemonio2(self, escolha: Entidade) -> None:
        pass

    def usarItem(self) -> None:
        pass

    def escolherItem(self) -> int:
        pass

    def selecionarAlvoitem(itemIndex: int, local: int, entidadeIndex: int) -> list:
        pass

    def invocar(self) -> None:
        pass

    def definirTrocaReserva(self, index: int) -> int:
        pass

    def definirTrocaCampo(self, index: int, vazio: bool) -> int:
        pass

    def calcularTurnos(self, caso: str, resAtaque: str) -> None:
        pass

    def calculaCustoAtaque(self, resAtaque: str) -> int:
        pass

    def calculoCustoTurno(self, caso: str, custoAtaque: int) -> int:
        pass

    def mudaJogadorAtual(self) -> None:
        pass

    def ataque(self) -> None:
        pass

    def validarAtaque(self, ataqueIndex: int) -> None:
        pass

    def definirAlvo(self, index: int) -> None:
        pass

    def avaliarAtaque(self, tipoAtaque: Tipo, tipoAlvo: Tipo) -> str:
        pass

    def calcularModificadorDano(self, res: str) -> None:
        pass

    def fundir(self) -> None:
        pass

    def definirFusão1(self, material: Entidade, local: int) -> None:
        pass


    def definirFusão2(self, material: Entidade, local: int) -> None:
        pass

    def validarFusao(self, material1: Entidade, material2: Entidade) -> bool:
        pass

    def definirResultado(self, material1: Entidade, material2: Entidade, local: int) -> Entidade:
        pass

    def definirLocalFusao(self, local1: int, local2: int) -> int:
        pass

    def avaliaVencedor(self) -> None:
        pass

    def verificaVencedor(self) -> Jogador:
        if self.jogador1.vencedor == True:
            return self.jogador1
        elif self.jogador2.vencedor == True:
            return self.jogador2

    def defineEscolha(escolha: str) -> None:
        pass

    def executaEscolha(escolha: str) -> None:
        pass

