from jogador import *
from entidade import Entidade
from ataque import Ataque
from tkinter import PhotoImage

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
        self.defineEntidades()
        self.defineTimes()
        self.jogadoresTeste()

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

        self.ataques = [self.atq_fisico1, self.atq_fogo1, self.atq_raio1, self.atq_gelo1]

    def defineEntidades(self):
        #Demonios
        self.img1 = PhotoImage(file='images/sprites/demonios/demo1.png')
        self.img1 = self.img1.zoom(2)

        self.img2 = PhotoImage(file='images/sprites/demonios/demo2.png')
        self.img2 = self.img2.zoom(2)

        self.img3 = PhotoImage(file='images/sprites/demonios/demo3.png')
        self.img3 = self.img3.zoom(2)

        self.img4 = PhotoImage(file='images/sprites/demonios/demo4.png')
        self.img4 = self.img4.zoom(2)

        self.img5 = PhotoImage(file='images/sprites/demonios/demo5.png')
        self.img5 = self.img5.zoom(2)

        self.img6 = PhotoImage(file='images/sprites/demonios/demo6.png')
        self.img6 = self.img6.zoom(2)

        self.img7 = PhotoImage(file='images/sprites/demonios/demo7.png')
        self.img7 = self.img7.zoom(2)

        self.img8 = PhotoImage(file='images/sprites/demonios/demo8.png')
        self.img8 = self.img8.zoom(2)

        self.img9 = PhotoImage(file='images/sprites/demonios/demo9.png')
        self.img9 = self.img9.zoom(2)

        self.img10 = PhotoImage(file='images/sprites/demonios/demo10.png')
        self.img10 = self.img10.zoom(2)

        self.img11 = PhotoImage(file='images/sprites/demonios/demo11.png')
        self.img11 = self.img11.zoom(2)

        self.img12 = PhotoImage(file='images/sprites/demonios/demo12.png')
        self.img12 = self.img12.zoom(2)

        self.img13 = PhotoImage(file='images/sprites/demonios/demo13.png')
        self.img13 = self.img13.zoom(2)

        self.img14 = PhotoImage(file='images/sprites/demonios/demo14.png')
        self.img14 = self.img14.zoom(2)

        self.img15 = PhotoImage(file='images/sprites/demonios/demo15.png')
        self.img15 = self.img15.zoom(2)

        self.img16 = PhotoImage(file='images/sprites/demonios/demo16.png')
        self.img16 = self.img16.zoom(2)

        self.e1 = Entidade("Demonio Teste 1", self.tipo_fogo, self.ataques, 123, 123, 200, 200, 50, 40, 20, False, 0, self.img1)
        self.e2 = Entidade("Demonio Teste 2", self.tipo_gelo, self.ataques, 456, 456, 300, 200, 50, 40, 20, False, 0, self.img2)
        self.e3 = Entidade("Demonio Teste 3", self.tipo_vento, self.ataques, 789, 789, 400, 200, 50, 40, 20, False, 0, self.img3)
        self.e4 = Entidade("Demonio Teste 4", self.tipo_raio, self.ataques, 912, 912, 500, 200, 50, 40, 20, False, 0, self.img4)
        self.e5 = Entidade("Demonio Teste 5", self.tipo_fogo, self.ataques, 123, 123, 200, 200, 50, 40, 20, False, 0, self.img5)
        self.e6 = Entidade("Demonio Teste 6", self.tipo_gelo, self.ataques, 456, 456, 300, 200, 50, 40, 20, False, 0, self.img6)
        self.e7 = Entidade("Demonio Teste 7", self.tipo_vento, self.ataques, 789, 789, 400, 200, 50, 40, 20, False, 0, self.img7)
        self.e8 = Entidade("Demonio Teste 8", self.tipo_raio, self.ataques, 912, 912, 500, 200, 50, 40, 20, False, 0, self.img8)
        self.e9 = Entidade("Demonio Teste 9", self.tipo_fogo, self.ataques, 123, 123, 200, 200, 50, 40, 20, False, 0, self.img9)
        self.e10 = Entidade("Demonio Teste 10", self.tipo_gelo, self.ataques, 456, 456, 300, 200, 50, 40, 20, False, 0, self.img10)
        self.e11 = Entidade("Demonio Teste 11", self.tipo_vento, self.ataques, 789, 789, 400, 200, 50, 40, 20, False, 0, self.img11)
        self.e12 = Entidade("Demonio Teste 12", self.tipo_raio, self.ataques, 912, 912, 500, 200, 50, 40, 20, False, 0, self.img12)
        self.e13 = Entidade("Demonio Teste 13", self.tipo_fogo, self.ataques, 123, 123, 200, 200, 50, 40, 20, False, 0, self.img13)
        self.e14 = Entidade("Demonio Teste 14", self.tipo_gelo, self.ataques, 456, 456, 300, 200, 50, 40, 20, False, 0, self.img14)
        self.e15 = Entidade("Demonio Teste 15", self.tipo_vento, self.ataques, 789, 789, 400, 200, 50, 40, 20, False, 0, self.img15)
        self.e16 = Entidade("Demonio Teste 16", self.tipo_raio, self.ataques, 912, 912, 500, 200, 50, 40, 20, False, 0, self.img16)

        #Humanos
        self.img_h1 = PhotoImage(file='images/sprites/humanos/humano1.png')
        self.img_h1 = self.img_h1.zoom(2)

        self.img_h2 = PhotoImage(file='images/sprites/humanos/humano2.png')
        self.img_h2 = self.img_h2.zoom(2)

        self.img_h3 = PhotoImage(file='images/sprites/humanos/humano3.png')
        self.img_h3 = self.img_h3.zoom(2)

        self.img_h4 = PhotoImage(file='images/sprites/humanos/humano4.png')
        self.img_h4 = self.img_h4.zoom(2)

        self.h1 = Entidade("Humano Teste 1", self.tipo_fisico, self.ataques, 500, 500, 100, 100, 10, 20, 30, True, 0, self.img_h1)
        self.h2 = Entidade("Humano Teste 2", self.tipo_fisico, self.ataques, 500, 500, 100, 100, 10, 20, 30, True, 0, self.img_h2)
        self.h3 = Entidade("Humano Teste 3", self.tipo_fisico, self.ataques, 500, 500, 100, 100, 10, 20, 30, True, 0, self.img_h3)
        self.h4 = Entidade("Humano Teste 4", self.tipo_fisico, self.ataques, 500, 500, 100, 100, 10, 20, 30, True, 0, self.img_h4)

    def defineItens(self):
        #Cura
        self.item1 = Item("Curativo Pequeno", "cura", 50, 10)
        self.item2 = Item("Curativo Grande", "cura", 100, 5)

        #MP
        self.item3 = Item("Elixir Pequeno", "mp", 50, 10)
        self.item4 = Item("Elixir Grande ", "mp", 100, 5)

        #Revive
        self.item5 = Item("Desfibrilador Fraco", "revive", 1, 5)
        self.item6 = Item("Desfibrilador Forte", "revive", 100, 2)

        self.itens1 = [self.item1, self.item2, self.item3, self.item4, self.item5, self.item6]

    def defineTimes(self):
        self.time1_demos = [self.e1, self.e2, self.e3, self.e4]
        self.time1 = Time(self.h1, [], self.time1_demos)

        self.time2_demos = [self.e5, self.e6, self.e7, self.e8]
        self.time2 = Time(self.h2, [], self.time2_demos)

        self.time3_demos = [self.e9, self.e10, self.e11, self.e12]
        self.time3 = Time(self.h3, [], self.time3_demos)

        self.time4_demos = [self.e13, self.e14, self.e15, self.e16]
        self.time4 = Time(self.h4, [], self.time4_demos)

    #Só para teste, remover depois
    def jogadoresTeste(self):
        self.j1 = Jogador(self.time1, True, False, True, self.itens1, 10)
        self.j2 = Jogador(self.time2, True, False, True, self.itens1, 10)

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

