from xmlrpc.client import Boolean
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
    def __init__(self, interface):
        self.interface = interface
        self.batalhaEmAndamento = False
        self.estagio = "Escolha1"
        self.jogadorAtual = None
        self.jogadorOutro = None
        self.todosHumanos = []
        self.demoniosEscolha = []
        self.demonioFusao = []
        self.atualIndex = 0
        self.vencedor = None
        self.perdedor = None

        self.defineTipos()
        self.defineAtaques()
        self.defineItens()
        self.defineEntidades()
        self.defineFusoes()
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
        self.agi= Ataque("Agi", self.tipo_fogo, 130, 10)
        self.agilao = Ataque("Agilao", self.tipo_fogo, 160, 20)
        self.agidyne = Ataque("Agidyne", self.tipo_fogo, 215, 35)
        self.agibarion = Ataque("Agibarion", self.tipo_fogo, 265, 50)

        #Gelo
        self.bufu = Ataque("Bufu", self.tipo_gelo, 130, 10)
        self.bufula = Ataque("Bufula", self.tipo_gelo, 160, 20)
        self.bufudyne = Ataque("Bufudyne", self.tipo_gelo, 215, 35)
        self.bufubarion = Ataque("Bufubarion", self.tipo_gelo, 265, 50)

        #Vento
        self.zan = Ataque("Zan", self.tipo_vento, 130, 10)
        self.zanma = Ataque("Zanma", self.tipo_vento, 160, 20)
        self.zandyne = Ataque("Zandyne", self.tipo_vento, 215, 35)
        self.zanbarion = Ataque("Zanbarion", self.tipo_vento, 265, 50)

        #Raio
        self.zio = Ataque("Zio", self.tipo_raio, 130, 10)
        self.zionga = Ataque("Zionga", self.tipo_raio, 160, 20)
        self.ziodyne = Ataque("Ziodyne", self.tipo_raio, 215, 35)
        self.ziobarion = Ataque("Ziobarion", self.tipo_raio, 265, 50)

        #Luz
        self.hama = Ataque("Hama", self.tipo_luz, 140, 15)
        self.hamaon = Ataque("Hamaon", self.tipo_luz, 175, 25)
        self.hamabarion = Ataque("Hamabarion", self.tipo_luz, 265, 55)

        #Escuro
        self.mudo = Ataque("Mudo", self.tipo_escuro, 140, 15)
        self.mudoon = Ataque("Mudoon", self.tipo_escuro, 175, 25)
        self.mudobarion = Ataque("Mudobarion", self.tipo_escuro, 265, 5)

        #Fisico (todos custam 0)
        self.soco = Ataque("Soco", self.tipo_fisico, 70, 0)
        self.mordida = Ataque("Mordida", self.tipo_fisico, 80, 0)
        self.corte = Ataque("Corte", self.tipo_fisico, 90, 0)
        self.espingarda = Ataque("Espingarda", self.tipo_fisico, 100, 0)

        self.atqHumanos = [self.espingarda, self.agi, self.bufu, self.zio]

    def defineEntidades(self):
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

        self.img17 = PhotoImage(file='images/sprites/demonios/demo17.png')
        self.img17 = self.img17.zoom(2)

        self.img18 = PhotoImage(file='images/sprites/demonios/demo18.png')
        self.img18 = self.img18.zoom(2)

        self.img19 = PhotoImage(file='images/sprites/demonios/demo19.png')
        self.img19 = self.img19.zoom(2)

        self.img20 = PhotoImage(file='images/sprites/demonios/demo20.png')
        self.img20 = self.img20.zoom(2)
        
        self.e1 = Entidade('Will O Wisp', self.tipo_escuro, [self.mudo, self.hama, self.zan, self.mordida],
                200, 120, 55, 34, 21, False, 1, self.img1)
        self.e2 = Entidade('Slime', self.tipo_escuro, [self.mudo, self.mudoon, self.hamaon, self.zio],
                215, 90, 43, 65, 38, False, 1, self.img2)
        self.e3 = Entidade('Zhen', self.tipo_raio, [self.zio, self.agi, self.hama, self.zionga], 
                170, 140, 45, 77, 38, False, 1, self.img3)
        self.e4 = Entidade('Erthys', self.tipo_vento, [self.agi, self.agilao, self.zan, self.zanma], 
                195, 190, 60, 35, 26, False, 1, self.img4)
        self.e5 = Entidade("Shiisaa", self.tipo_luz, [self.mudo, self.hama, self.hamabarion, self.zan], 
                250, 120, 70, 50, 44, False, 1, self.img5)
        self.e6 = Entidade('Take-Minakata', self.tipo_fogo, [self.agilao, self.bufu, self.agidyne, self.hama], 
                215, 90, 43, 65, 38, False, 1, self.img6)
        self.e7 = Entidade('Ame-no-Uzume', self.tipo_raio, [self.zio, self.agi, self.mudo, self.ziobarion], 
                170, 140, 80, 77, 38, False, 1, self.img7)
        self.e8 = Entidade('Inugami', self.tipo_vento, [self.agi, self.hama, self.zan, self.zanma], 
                195, 160, 60, 55, 26, False, 1, self.img8)
        self.e9 = Entidade('Shikigami', self.tipo_gelo, [self.bufu, self.hama, self.bufula, self.mordida], 
                170, 130, 35, 54, 34, False, 1, self.img9)
        self.e10 = Entidade('Angel', self.tipo_escuro, [self.mudobarion, self.mudoon, self.hamaon, self.zionga], 
                215, 110, 84, 70, 38, False, 1, self.img10)
        self.e11 = Entidade('Karasu Tengu', self.tipo_raio, [self.zio, self.espingarda, self.hama, self.zionga], 
                160, 80, 41, 33, 26, False, 1, self.img11)
        self.e12 = Entidade('Mara', self.tipo_fogo, [self.agi, self.agilao, self.corte, self.espingarda], 
                195, 190, 60, 45, 40, False, 1, self.img12)
        self.e13 = Entidade('Beelzebub', self.tipo_gelo, [self.bufubarion, self.hamabarion, self.hama, self.mudo], 
                250, 140, 75, 64, 41, False, 1, self.img13)
        self.e14 = Entidade('Mada', self.tipo_luz, [self.hamabarion, self.mudoon, self.hamaon, self.ziodyne], 
                215, 120, 65, 68, 39, False, 1, self.img14)
        self.e15 = Entidade('Hresvelgr', self.tipo_raio, [self.ziobarion, self.agibarion, self.hama, self.zionga], 
                200, 180, 78, 42, 38, False, 1, self.img15)
        self.e16 = Entidade('Yatagarasu', self.tipo_vento, [self.hamaon, self.agilao, self.zanbarion, self.zanma], 
                195, 190, 78, 56, 32, False, 1, self.img16)
        self.e17 = Entidade('Vishnu', self.tipo_gelo, [self.bufula, self.hama, self.bufudyne, self.mordida], 
                200, 130, 60, 44, 25, False, 1, self.img17)
        self.e18 = Entidade('Shiva', self.tipo_escuro, [self.mudo, self.mudoon, self.hamaon, self.zio], 
                215, 90, 43, 65, 38, False, 1, self.img18)
        self.e19 = Entidade('Cu Chulainn', self.tipo_luz, [self.hamabarion, self.hamaon, self.mudobarion, self.mudoon], 
                180, 146, 47, 77, 38, False, 1, self.img19)
        self.e20 = Entidade('Metatron', self.tipo_fogo, [self.agi, self.agibarion, self.zan, self.mudoon], 
                215, 190, 54, 37, 22, False, 1, self.img20)

        self.todosDemonios = [
            self.e1,
            self.e2,
            self.e3,
            self.e4,
            self.e5,
            self.e6,
            self.e7,
            self.e8,
            self.e9,
            self.e10,
            self.e11,
            self.e12,
            self.e13,
            self.e14,
            self.e15,
            self.e16,
            self.e17,
            self.e18,
            self.e19,
            self.e20
        ]

        #HUMANOS
        self.img_h1 = PhotoImage(file='images/sprites/humanos/humano1.png')
        self.img_h1 = self.img_h1.zoom(2)

        self.img_h2 = PhotoImage(file='images/sprites/humanos/humano2.png')
        self.img_h2 = self.img_h2.zoom(2)

        self.img_h3 = PhotoImage(file='images/sprites/humanos/humano3.png')
        self.img_h3 = self.img_h3.zoom(2)

        self.img_h4 = PhotoImage(file='images/sprites/humanos/humano4.png')
        self.img_h4 = self.img_h4.zoom(2)

        self.h1 = Entidade("Humano Teste 1", self.tipo_fisico, self.atqHumanos, 400, 100, 10, 20, 30, True, 0, self.img_h1)
        self.h2 = Entidade("Humano Teste 2", self.tipo_fisico, self.atqHumanos, 400, 100, 10, 20, 30, True, 0, self.img_h2)
        self.h3 = Entidade("Humano Teste 3", self.tipo_fisico, self.atqHumanos, 500, 100, 10, 20, 30, True, 0, self.img_h3)
        self.h4 = Entidade("Humano Teste 4", self.tipo_fisico, self.atqHumanos, 500, 100, 10, 20, 30, True, 0, self.img_h4)

    def defineFusoes(self):
        self.fusoes = {}

        for i in self.todosDemonios:
            for j in self.todosDemonios:
                if [i.getNome(), j.getNome()] not in self.fusoes.values() and [j.getNome(), i.getNome()] not in self.fusoes.values():
                    fusao = choice(self.todosDemonios)
                    if fusao in self.fusoes.keys():
                        self.fusoes[fusao].append([i.getNome(), j.getNome()])
                    else:
                        self.fusoes[fusao] = [[i.getNome(), j.getNome()]]


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
        self.j1 = Jogador("1", self.time1, True, False, True, self.itens1, 10)
        self.j2 = Jogador("2", self.time2, True, False, True, self.itens1, 10)

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
    
    def executaAtaques(self, atacante, alvo, ataque, listaCampoCells, atualCell):
        res = self.avaliarAtaque(ataque.getTipo(), alvo.getTipo())
        modificador = self.calcularModificadorDano(res)
        self.causarDano(atacante, alvo, ataque, res, modificador)
        atacante.modificarMagia(ataque.getCusto() * -1)
        self.calcularTurnos("ataque", res, listaCampoCells, atualCell)

    def usarItem(self, item, alvo, listaCampoCells, atualCell) -> None:
        tipo = item.getTipo()
        potencia = item.getPotencia()
        if tipo == "cura":
            alvo.modificarVida(potencia)
        elif tipo == "magia":
            alvo.modificarMagia(potencia)
        elif tipo == "revive":
            alvo.reviver(potencia)
        item.diminuiQtd()
        self.calcularTurnos("item", "", listaCampoCells, atualCell)

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

    def invocar(self, cell1, cell2, listaCampoCells, atualCell) -> None:
        tempEnt = cell1.getEntidade()
        cell1.setEntidade(cell2.getEntidade())
        cell2.setEntidade(tempEnt)
        cell1.changeLocal()
        cell2.changeLocal()
        self.calcularTurnos("invocar", "", listaCampoCells, atualCell)

    def definirTrocaReserva(self, index: int) -> int:
        pass

    def definirTrocaCampo(self, index: int, vazio: bool) -> int:
        pass

    def calcularTurnos(self, caso: str, resAtaque: str, listaCampoCells: list, atualCell) -> None:
        custoAtaque = 0
        if caso == "ataque":
            custoAtaque = self.calculaCustoAtaque(resAtaque)
        custoTurno = self.calculaCustoTurno(caso, custoAtaque)
        self.jogadorAtual.diminuiTurnos(custoTurno)
        if not self.verificaVencedor():
            if self.jogadorAtual.getTurnos() <= 0:
                self.jogadorAtual.setTurnos(10)
                self.mudaJogadorAtual()
                self.interface.resetJogadores()
                self.atualIndex = 0
            self.mudaEntidadeAtual(listaCampoCells, atualCell)
            self.interface.setAtaques(self.interface.getAtualCell().getEntidade().getAtaques())
        else:
            self.interface.telaFinal()

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

    def mudaEntidadeAtual(self, listaCampoCells, atualCell):
        achouNovo = False
        #Checa se na frente
        for i in range(4):
            if achouNovo:
                break
            elif (not listaCampoCells[i].getVazio()) and i > self.atualIndex:
                self.atualIndex = i
                atualCell.setEntidade(listaCampoCells[i].getEntidade())
                atualCell.updateStats()
                achouNovo = True
            else:
                continue
        
        if achouNovo:
            return
        else:
            #Checa se a tras
            for i in range(4):
                if achouNovo:
                    break
                elif (not listaCampoCells[i].getVazio()) and i < self.atualIndex:
                    self.atualIndex = i
                    atualCell.setEntidade(listaCampoCells[i].getEntidade())
                    atualCell.updateStats()
                    achouNovo = True
                else:
                    continue

    def mudaJogadorAtual(self) -> None:
        temp = self.jogadorAtual
        self.jogadorAtual = self.jogadorOutro
        self.jogadorOutro = temp

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
        elif (atacante.sorte + randint(0, 50)) > 70:
              alvo.modificarVida(danoTotal * -2)
        else:
            alvo.modificarVida(danoTotal * -1)

    def fundir(self, cell1, cell2, listaCampoCells, atualCell) -> None:
        resRef = None
        d1 = cell1.getEntidade()
        d2 = cell2.getEntidade()

        for key, value in self.fusoes.items():
            if [d1.getNome(), d2.getNome()] in value or [d2.getNome(), d1.getNome()] in value:
                resRef = key
                break
        
        params = resRef.getParamsFusao()
        res = Entidade(params[0], params[1], params[2], params[3], params[4],
                        params[5], params[6], params[7], params[8],
                        params[9], params[10])
        
        newCell = None
        if d1.getLocal() == 1:
            newCell = cell1
        elif d2.getLocal() == 1:
            newCell = cell2
        else:
            newCell = cell1

        cell1.setEntidade(None)
        cell2.setEntidade(None)
        newCell.setEntidade(res)

        self.calcularTurnos("fusao", "", listaCampoCells, atualCell)

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

    def verificaVencedor(self) -> Boolean:
        timeAtual = self.jogadorAtual.getTimeInteiro()
        print("TIME ATUAL:")
        print(timeAtual)
        humanoMorto = False
        demoniosMortos = 0

        for i in timeAtual:
            if i.getEhHumano() and not i.getVivo():
                humanoMorto = True
                break
            elif not i.getEhHumano() and not i.getVivo():
                demoniosMortos += 1

        if humanoMorto or demoniosMortos == len(timeAtual) - 1:
            print("Jogador Outro ganhou!")
            self.vencedor = self.jogadorOutro
            self.perdedor = self.jogadorAtual
            self.interface.telaFinal()

        humanoMorto = False
        demoniosMortos = 0
        timeOutro = self.jogadorOutro.getTimeInteiro()
        print("TIME OUTRO")
        print(timeOutro)

        for i in timeOutro:
            if i.getEhHumano() and not i.getVivo():
                humanoMorto = True
                break
            elif not i.getEhHumano() and not i.getVivo():
                demoniosMortos += 1

        if humanoMorto or demoniosMortos == len(timeOutro) - 1:
            self.vencedor = self.jogadorAtual
            self.perdedor = self.jogadorOutro
            print("Jogador Atual ganhou!")
            return True

        return False

    def defineEscolha(escolha: str) -> None:
        pass

    def executaEscolha(escolha: str) -> None:
        pass

    def getJogadorAtual(self):
        return self.jogadorAtual

    def getJogadorOutro(self):
        return self.jogadorOutro

    def createTeam(self):
        team = []
        camp = []
        reserve = []
        while len(camp) < 3:
            demon = choice(self.todosDemonios)
            if demon not in camp:
                camp.append(demon)
        while len(reserve) < 4:
            demon = choice(self.todosDemonios)
            if demon not in reserve and demon not in camp:
                reserve.append(demon)
        if (len(camp)+len(reserve)) == 7:
            team.append(camp)
            team.append(reserve)
        
        return team

    def createTeams(self):
        team1 = self.createTeam()
        team2 = self.createTeam()
        for i in range(len(team1[0])):
            if team1[0][i] in team2[0]:
                    pos = team2[0].index(team1[0][i])
                    demon = choice(self.todosDemonios)
                    if demon not in team2[0] or demon not in team2[1]:
                        team2[0][pos] = demon
        
        return teams

    def getResultado(self):
        return [self.vencedor, self.perdedor]

    def restore(self):
        self.jogadorAtual.restore()
        self.jogadorOutro.restore()


