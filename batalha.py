from jogador import *
from entidade import Entidade
from ataque import Ataque

class Batalha:
    def __init__(self):
        self.batalhaEmAndamento = False
        self.estagio = "Escolha1"
        self.jogadorAtual = None
        self.jogadorOutro = None
        self.todosHumanos = []
        self.demoniosEscolha = []
        self.demonioFusao = []

        self.defineTipos()
        self.defineAtaques()
        self.defineItens()

    def defineTipos(self):
        self.tipo_fogo = Tipo("Fogo", None, "Gelo", None, "Raio")
        self.tipo_gelo = Tipo("Gelo", "Fogo", "Vento", None, None)
        self.tipo_vento = Tipo("Vento", "Gelo", "Raio", "Fogo", None)
        self.tipo_raio = Tipo("Raio", None, "Raio", None, None)
        self.tipo_luz = Tipo("Luz", "Profano", "Gelo", "Fisico", None)
        self.tipo_escuro = Tipo("Escuro", "Divino", "Fogo", None, "Fisico")
        self.tipo_fisico = Tipo("Fisico", "Divino", None, None, None)

    def defineAtaques(self):
        #Fogo
        self.atq_fogo1 = Ataque("Agi", self.tipo_fogo, 130, 10)
        self.atq_fogo2 = Ataque("Agilao", self.tipo_fogo, 160, 20)
        self.atq_fogo3 = Ataque("Agidyne", self.tipo_fogo, 215, 35)
        self.atq_fogo4 = Ataque("Agibarion", self.tipo_fogo, 265, 50)

        #Gelo
        self.atq_gelo1 = Ataque("Bufu", self.tipo_gelo, 130, 10)
        self.atq_gelo2 = Ataque("Bufula", self.tipo_gelo, 160, 20)
        self.atq_gelo3 = Ataque("Bufudyne", self.tipo_gelo, 215, 35)
        self.atq_gelo4 = Ataque("Bufubarion", self.tipo_gelo, 265, 50)

        #Vento
        self.atq_vento1 = Ataque("Zan", self.tipo_vento, 130, 10)
        self.atq_vento2 = Ataque("Zanma", self.tipo_vento, 160, 20)
        self.atq_vento3 = Ataque("Zandyne", self.tipo_vento, 215, 35)
        self.atq_vento4 = Ataque("Zanbaryon", self.tipo_vento, 265, 50)

        #Raio
        self.atq_raio1 = Ataque("Zio", self.tipo_raio, 130, 10)
        self.atq_raio2 = Ataque("Zionga", self.tipo_raio, 160, 20)
        self.atq_raio3 = Ataque("Ziodyne", self.tipo_raio, 215, 35)
        self.atq_raio4 = Ataque("Ziobarion", self.tipo_raio, 265, 50)

        #Luz
        self.atq_luz1 = Ataque("Hama", self.tipo_luz, 140, 15)
        self.atq_luz2 = Ataque("Hamaon", self.tipo_luz, 175, 25)
        self.atq_luz3 = Ataque("Hamabarion", self.tipo_luz, 265, 55)

        #Escuro
        self.atq_escuro1 = Ataque("Mudo", self.tipo_escuro, 140, 15)
        self.atq_escuro2 = Ataque("Mudoon", self.tipo_escuro, 175, 25)
        self.atq_escuro3 = Ataque("Mudobarion", self.tipo_escuro, 265, 5)

        #Fisico (todos custam 0)
        self.atq_fisico1 = Ataque("Soco", self.tipo_fisico, 70, 0)
        self.atq_fisico2 = Ataque("Mordida", self.tipo_fisico, 80, 0)
        self.atq_fisico3 = Ataque("Corte", self.tipo_fisico, 90, 0)
        self.atq_fisico4 = Ataque("Espingarda", self.tipo_fisico, 100, 0)

        self.ataques = [self.atq_fogo1, self.atq_fogo2, self.atq_raio1, self.atq_gelo2]

    def defineItens(self):
        #Cura
        self.item1 = Item("Curativo 1", "cura", 50, 10)
        self.item2 = Item("Curativo 2", "cura", 100, 5)

        #MP
        self.item3 = Item("Grimorio 1", "mp", 50, 10)
        self.item4 = Item("Grimorio 2", "mp", 100, 5)

        #Revive
        self.item5 = Item("Desfibrilador 1", "revive", 1, 5)
        self.item6 = Item("Desfibrilador 2", "revive", 100, 2)

        self.itens = [self.item1, self.item2, self.item3, self.item4, self.item5, self.item6]


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

