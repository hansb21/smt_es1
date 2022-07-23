from tipo import Tipo
from random import randint
from item import Item
from jogador import Jogador
from random import choice
from entidade import Entidade
from ataque import Ataque
from tkinter import PhotoImage
from team import Time
from random import randint

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
        self.sorteiaJogador()

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

        self.h1 = Entidade("Humano Teste 1", self.tipo_fisico, self.ataques, 400, 500, 100, 100, 10, 20, 30, True, 0, self.img_h1)
        self.h2 = Entidade("Humano Teste 2", self.tipo_fisico, self.ataques, 400, 500, 100, 100, 10, 20, 30, True, 0, self.img_h2)
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
        res = randint(1,2)
        if res == 1:
            self.jogadorAtual = self.j1
            self.jogadorOutro = self.j2
        else:
            self.jogadorAtual = self.j2
            self.jogadorOutro = self.j1
    
    def executaAtaques(self, atacante, alvo, ataque):
        res = self.avaliarAtaque(ataque.getTipo(), alvo.getTipo())
        #print(res)
        modificador = self.calcularModificadorDano(res)
        self.causarDano(atacante, alvo, ataque, res, modificador)
        atacante.modificarMagia(ataque.getCusto() * -1)
        self.calcularTurnos("ataque", res)

    def usarItem(self, item, alvo) -> None:
        tipo = item.getTipo()
        potencia = item.getPotencia()
        if tipo == "cura":
            alvo.modificarVida(potencia)
        elif tipo == "magia":
            alvo.modificarMagia(potencia)
        elif tipo == "revive":
            alvo.reviver(potencia)
        item.diminuiQtd()
        self.calcularTurnos("item", "")

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

    def escolherItem(self) -> int:
        pass

    def selecionarAlvoitem(itemIndex: int, local: int, entidadeIndex: int) -> list:
        pass

    def invocar(self, cell1, cell2) -> None:
        tempEnt = cell1.getEntidade()
        cell1.clearEntidade()
        cell1.setEntidade(cell2.getEntidade())
        cell2.setEntidade(tempEnt)
        self.calcularTurnos("invocar", "")

    def definirTrocaReserva(self, index: int) -> int:
        pass

    def definirTrocaCampo(self, index: int, vazio: bool) -> int:
        pass

    def calcularTurnos(self, caso: str, resAtaque: str) -> None:
        custoAtaque = 0
        if caso == "ataque":
            custoAtaque = self.calculaCustoAtaque(resAtaque)
        custoTurno = self.calculaCustoTurno(caso, custoAtaque)
        self.jogadorAtual.diminuiTurnos(custoTurno)
        #IMPLEMENTAR TROCA DE JOGADORES

    def calculaCustoAtaque(self, resAtaque: str) -> int:
        if resAtaque == "fraco":
            return -1
        elif resAtaque == "resiste":
            return 1
        elif resAtaque == "reflete":
            return 2
        elif resAtaque == "absorve":
            return 3
        else:
            return 0

    def calculaCustoTurno(self, caso: str, custoAtaque: int) -> int:
        if caso == "fusao":
            return 4
        elif caso == "item":
            return 3
        elif caso == "ataque":
            return 2 + custoAtaque
        elif caso == "invocar":
            return 5
        else:
            return 1

    def mudaJogadorAtual(self) -> None:
        pass

    def ataque(self) -> None:
        pass

    def validarAtaque(self, ataque, atacante) -> None:
        if atacante.getMpAtual() < ataque.getCusto():
            return False
        else:
            return True

    def definirAlvo(self, index: int) -> None:
        pass

    def avaliarAtaque(self, tipoAtaque: Tipo, tipoAlvo: Tipo) -> str:
        if tipoAtaque.getNome() == tipoAlvo.getFraqueza():
            return "fraco"
        elif tipoAtaque.getNome() == tipoAlvo.getResistencia():
            return "resiste"
        elif tipoAtaque.getNome() == tipoAlvo.getRepelir():
            return "reflete"
        elif tipoAtaque.getNome() == tipoAlvo.getAbsorver():
            return "absorve"
        else:
            return "normal"

    def calcularModificadorDano(self, res: str) -> float:
        if res == "fraco":
            return 1.5
        elif res == "resiste":
            return 0.5
        else:
            return 1

    def causarDano(self, atacante, alvo, ataque, res, modificador):
        danoTotal = modificador * ataque.getDano()
        if res == "reflete":
            atacante.modificarVida(danoTotal * -1)
        elif res == "absorve":
            alvo.modificarVida(danoTotal)
        elif (atacante.sorte + randint(0, 50) > 70:
              alvo.modificarVida(danoTotal * -2)
        else:
            alvo.modificarVida(danoTotal * -1)

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
        if self.jogadorAtual.vencedor == True:
            return self.jogadorAtual
        elif self.jogadorOutro.vencedor == True:
            return self.jogadorOutro

    def defineEscolha(escolha: str) -> None:
        pass

    def executaEscolha(escolha: str) -> None:
        pass

    def getJogadorAtual(self):
        return self.jogadorAtual

    def getJogadorOutro(self):
        return self.jogadorOutro



    demons = ['Will O Wisp', 'Preta', 'Zhen', 'Erthys', "Shiisaa", 'Take-Minakata', 'Ame-no-Uzume', 'Inugami', 'Shikigami', 'Angel', 'Karasu Tengu' 'Mara', 'Beelzebub', 'Mada', 'Hresvelgr', 'Yatagarasu', 'Vishnu', 'Shiva', 'Cu Chulainn', 'Metatron', 'Genesha']

    #demons[i][0] = tipo
    #demons[i][1] = Ataques
    #demons[i][2-6] = maxHp, maxMp, atk, deF, luk,
    defdemons = {
                    str(demons[0]) : ["Escuro", ["Mudom", "Hama", "Zan", "Mordida"], 200, 120, 55, 34, 21],
                    str(demons[1]) : ["Escuro", ["Mudom", "Mudoon", "Hamaon", "Zio"], 215, 90, 43, 65, 38],
                    str(demons[2]) : ["Raio", ["Zio", "Agi", "Hama", "Zionga"], 170, 140, 45, 77, 38],
                    str(demons[3]) : ["Vento", ["Agi", "Agilao", "Zan", "Zanma"], 195, 190, 60, 35, 26],
                    str(demons[4]) : ["Luz", ["Mudom", "Hama", "Hamabarion", "Zan"], 250, 120, 70, 50, 44],
                    str(demons[5]) : ["Fogo", ["Agilao", "Bufu", "Agidyne", "Hama"], 215, 90, 43, 65, 38],
                    str(demons[6]) : ["Raio", ["Zio", "Agi", "Mudom", "Ziobarion"], 170, 140, 80, 77, 38],
                    str(demons[7]) : ["Vento", ["Agi", "Hama", "Zan", "Zanma"], 195, 160, 60, 55, 26],
                    str(demons[8]) : ["Gelo", ["Bufu", "Hama", "Bufula", "Mordida"], 170, 130, 35, 54, 34],
                    str(demons[9]) : ["Escuro", ["Mudobarion", "Mudoon", "Hamaon", "Zionga"], 215, 110, 84, 70, 38],
                    str(demons[10]) : ["Raio", ["Zio", "Espingarda", "Hama", "Zionga"], 160, 80, 41, 33, 26],
                    str(demons[11]) : ["Fogo", ["Agi", "Agilao", "Corte", "Espingarda"], 195, 190, 60, 45, 40],
                    str(demons[12]) : ["Gelo", ["Bufubarion", "Hamabarion", "Hama", "Mudo"], 250, 140, 75, 64, 41],
                    str(demons[13]) : ["Luz", ["Hamabarion", "Mudoon", "Hamaon", "Ziodyne"], 215, 120, 65, 68, 39],
                    str(demons[14]) : ["Raio", ["Ziobarion", "Agibarion", "Hama", "Zionga"], 200, 180, 78, 42, 38],
                    str(demons[15]) : ["Vento", ["Hamaon", "Agilao", "Zanbaryon", "Zanma"], 195, 190, 78, 56, 32],
                    str(demons[16]) : ["Gelo", ["Bufula", "Hama", "Bufudyne", "Mordida"], 200, 130, 60, 44, 25],
                    str(demons[17]) : ["Escuro", ["Mudom", "Mudoon", "Hamaon", "Zio"], 215, 90, 43, 65, 38],
                    str(demons[18]) : ["Luz", ["Hamabarion", "Hamaon", "Mudobarion", "Mudoon"], 180, 146, 47, 77, 38],
                    str(demons[19]) : ["Fogo", ["Agi", "Agibarion", "Zan", "Mudoon"], 215, 190, 54, 37, 22],
}
    def createTeams(self):
        
        teams = []
        camp = []
        reserve = []
        while len(camp) < 3:
            demon = choice(self.demons)
            print(demon)
            if demon not in camp:
                camp.append(demon)
        while len(reserve) < 4:
            demon = choice(self.demons)
            if demon not in reserve and demon not in camp:
                reserve.append(demon)
        if (len(camp)+len(reserve)) == 7:
            teams.append(camp)
            teams.append(reserve)
            print(teams)
        
        return teams
    
    def createFusions(self) -> dict:
        fusoes = {}

        for i in self.defdemons.keys():
            for j in self.defdemons.keys():
                if [i, j] not in fusoes.values():
                    fusao = choice(self.demons)
                    if fusao in fusoes.keys():
                        fusoes[fusao].append([i, j])
                    else:
                        fusoes[fusao] = [[i, j]]
        return fusoes

    def Fusao(self, fusoes: dict, demonio1: Entidade, demonio2: Entidade) -> Entidade:
        r_fusao = 0
        for i, j in fusoes.items():
            if i == [demonio1.name(), demonio2.name()]:
                r_fusao = j
        return r_fusao

