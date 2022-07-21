from tkinter import *
from turtle import width
from typing import TextIO
from item import Item
from ataque import Ataque
from tipo import Tipo
from batalha import Batalha
from storagebutton import StorageButton
from displaycell import DisplayCell

class BattleInterface:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Press Turn Battle")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(FALSE,FALSE)

        self.batalha = Batalha()

        self.ataqueSelecionado = None
        #self.alvoSelecionado = None

        #Definindo objetos
        self.defineJogadores()

        #Definindo elementos GUI
        self.defineFrames()
        self.defineMainButtons()
        self.defineItemButtons()
        self.defineAtaqueButtons()
        self.defineTurnosCell()
        self.definePlayerCells()
        self.defineEnemyCells()

        #Inicializar
        self.placeFrames()
        self.placeMainButtons()
        self.placeTurnosCell()
        self.placePlayerCells()
        self.placeEnemyCells()
        self.formatEntityCells()

        #TESTE
        #self.setItemsTest()
        self.setAtaquesTest()
        self.setJogadoresTest()

        #SEMPRE POR ULTIMO
        self.main_window.mainloop()

    #Jogadores
    def defineJogadores(self):
        self.jogadorAtual = self.batalha.getJogadorAtual()
        self.jogadorOutro = self.batalha.getJogadorOutro()

    #FRAMES
    def defineFrames(self):
        self.menu_frame = Frame(self.main_window, bg="grey99", width=128, height=528)
        self.field_frame = Frame(self.main_window, bg="green", width=1152, height=528)
        self.entity_frame = Frame(self.main_window, bg="blue", width=1280, height=192)

    def placeFrames(self):
        self.menu_frame.place(x=0, y=0)
        self.field_frame.place(x=128, y=0)
        self.entity_frame.place(x=0, y=528)
    
    #MAIN BUTTONS
    def defineMainButtons(self):
        self.ataque_button = Button(self.menu_frame ,bg="grey99", text="Ataque", command=lambda:self.replaceMainWithAtaque())
        self.item_button = Button(self.menu_frame ,bg="grey99", text="Itens", command=lambda:self.replaceMainWithItem())
        self.fundir_button = Button(self.menu_frame ,bg="grey99", text="Fusão", command=lambda:self.debug_button("Ritual de fusão") )
        self.invocar_button = Button(self.menu_frame ,bg="grey99", text="Invocar", command=lambda:self.debug_button("Ritual de invocação"))
        self.passar_button = Button(self.menu_frame ,bg="grey99", text="Passar Turno", command=lambda:self.passarTurno())

        self.lista_botoes = [   self.ataque_button, 
                                self.item_button, 
                                self.fundir_button, 
                                self.invocar_button,
                                self.passar_button]

    def placeMainButtons(self):
        for i, botao in enumerate(self.lista_botoes):
            calc_pos=75+55*i
            botao.place(x=0, y=calc_pos, width=128, height=55)

    def unplaceMainButtons(self):
        for botao in self.lista_botoes:
            botao.place_forget()

    def replaceItemWithMain(self):
        self.unplaceItemButtons()
        self.placeMainButtons()

        #PROVISORIO
        for i in range(4):
            self.campoCells[i].endSelection()
            self.reservaCells[i].endSelection()

    #ITEM BUTTONS
    def defineItemButtons(self):
        self.lista_item_botoes = []
        for _ in range(6):
            self.lista_item_botoes.append(StorageButton(self.menu_frame, 128, 55, "item", self))
        self.cancelaItemButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceItemWithMain())

    def placeItemButtons(self):
        for i, botao in enumerate(self.lista_item_botoes):
            calc_pos = 75+55*i
            botao.place(0, calc_pos)
        self.cancelaItemButton.place(x=0, y=405, width=128, height=55)

    def unplaceItemButtons(self):
        for botao in self.lista_item_botoes:
            botao.place_forget()
        self.cancelaItemButton.place_forget()

    def replaceMainWithItem(self):
        self.unplaceMainButtons()
        self.placeItemButtons()

        #PROVISORIO
        for i in range(4):
            self.campoCells[i].startSelection()
            self.reservaCells[i].startSelection()

    #ATAQUE BUTTONS
    def defineAtaqueButtons(self):
        #Antes de selecionar ataque
        self.lista_ataque_botoes = []
        for _ in range(4):
            self.lista_ataque_botoes.append(StorageButton(self.menu_frame, 128, 65, "atq", self))
        self.cancelaAtaqueButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceAtaqueWithMain())

        #Depois de selecionar ataque
        self.atqSelecionado = None
        self.atqSelectLabel = Label(self.menu_frame, text = "")
        self.cancelaAtaqueSelectButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceAtaqueSelectWithMain())

    def placeAtaqueButtons(self):
        for i, botao in enumerate(self.lista_ataque_botoes):
            calc_pos = 75+65*i
            botao.place(0, calc_pos)
        self.cancelaAtaqueButton.place(x=0, y=335, width=128, height=55)

    def unplaceAtaqueButtons(self):
        for botao in self.lista_ataque_botoes:
            botao.place_forget()
        self.cancelaAtaqueButton.place_forget()

    #TURNOS CELL
    def defineTurnosCell(self):
        self.turnosCell = DisplayCell(self.menu_frame, 128, 75, 5, "Turnos", True, self)

    def placeTurnosCell(self):
        self.turnosCell.place(0,0)

    #PLAYER CELLS
    def definePlayerCells(self):
        self.campoCells = []
        for i in range(4):
            texto = "Campo {}".format(i)
            newCell = DisplayCell(self.entity_frame, 320, 96, 5, texto, True, self)
            self.campoCells.append(newCell)

        self.reservaCells = []
        for i in range(4):
            texto = "Reserva {}".format(i)
            newCell = DisplayCell(self.entity_frame, 320, 96, 5, texto, True, self)
            self.reservaCells.append(newCell)

            self.atualCell = DisplayCell(self.field_frame, 230, 528, 5, "Entidade Atual", False, self)

    def placePlayerCells(self):
        for i, cell in enumerate(self.campoCells):
            calc_pos=320*i
            cell.place(calc_pos, 0)

        for i, cell in enumerate(self.reservaCells):
            calc_pos=320*i
            cell.place(calc_pos, 96)

        self.atualCell.place(0, 0)

    #INIMIGO CELLS
    def defineEnemyCells(self):
        self.enemyCells = []
        for i in range(4):
            texto = "Inimigo {}".format(i)
            newCell = DisplayCell(self.field_frame, 230, 528, 5, texto, False, self)
            self.enemyCells.append(newCell)

    def placeEnemyCells(self):
        for i, cell in enumerate(self.enemyCells):
            calc_pos=230*i+230
            cell.place(calc_pos, 0)

    #INICIALIZAR CELULAS
    def formatEntityCells(self):
        for (campo, reserva, inimigo) in zip(self.campoCells, self.reservaCells, self.enemyCells):
            campo.insertText("VAZIO\n\n")
            reserva.insertText("VAZIO\n\n")
            inimigo.insertText("VAZIO\n\n")

        self.atualCell.insertText("VAZIO\n\n")

        turnos = str(self.jogadorAtual.getTurnos())
        self.turnosCell.insertText(turnos)

    def updateTurnos(self):
        self.turnosCell.replaceText("1.0", str(self.jogadorAtual.getTurnos()))

    #MUDA TEXTO BOTOES
    def setItems(self, items):
        for i in range(6):
            self.lista_item_botoes[i].setStored(items[i])

    def setAtaques(self, ataques):
        for i in range(4):
            self.lista_ataque_botoes[i].setStored(ataques[i])

    #FUNCS TESTE EXCLUIR DPS
    def debug_button(self, escolha):
        print(f"{escolha} realizado sucesso")

    def unplaceAll(self):
        for widget in self.main_window.place_slaves():
            widget.place_forget()

    def setItemsTest(self):
        self.setItems(self.batalha.itens)

    def setAtaquesTest(self):
        self.setAtaques(self.batalha.ataques)

    def setInimigosTest(self):
        inimigos = self.batalha.eInimigosTeste
        for i, entidade in enumerate(inimigos):
            self.enemyCells[i].setEntidade(entidade)

    def setJogadoresTest(self):
        inimigos = self.jogadorOutro.getCampo()
        inimigos_humano = self.jogadorOutro.getHumano()
        self.enemyCells[0].setEntidade(inimigos_humano)
        for i, entidade in enumerate(inimigos):
            self.enemyCells[i+1].setEntidade(entidade)

        campo = self.jogadorAtual.getCampo()
        reserva = self.jogadorAtual.getReserva()
        humano = self.jogadorAtual.getHumano()
        self.campoCells[0].setEntidade(humano)
        for i, entidade in enumerate(campo):
            self.campoCells[i+1].setEntidade(entidade)
        for i, entidade in enumerate(reserva):
            self.reservaCells[i].setEntidade(entidade)
        self.atualCell.setEntidade(self.campoCells[0].getEntidade())

        self.setItems(self.jogadorAtual.getTodosItens())
        self.setAtaques(self.atualCell.getEntidade().getAtaques())

    #CASO DE USO ATAQUE
    def replaceMainWithAtaque(self):
        self.unplaceMainButtons()
        self.placeAtaqueButtons()

    def replaceAtaqueWithMain(self):
        self.unplaceAtaqueButtons()
        self.placeMainButtons()

    def replaceAtaqueSelectWithMain(self):
        self.atqSelectLabel.place_forget()
        self.cancelaAtaqueSelectButton.place_forget()
        for inimigo in self.enemyCells:
            inimigo.endSelection()
        self.ataqueSelecionado = None
        self.placeMainButtons()

    def replaceAtaqueWithAtaqueSelect(self, atq):
        
        if not self.batalha.validarAtaque(atq, self.atualCell.getEntidade()):
            return

        self.unplaceAtaqueButtons()
        #Place Atq Label
        tempNome = atq.getNome()
        tempDano = str(atq.getDano())
        tempTipo = atq.getTipo().getNome()
        tempCusto = str(atq.getCusto())
        labelText = "SELECIONADO: \n"  + tempNome + ":\n" + tempDano + " dano\n" + tempTipo + "\n" + tempCusto + " MP"
        self.atqSelectLabel.configure(text=labelText)
        self.atqSelectLabel.place(x=0, y=75, width=128, height=75)
        self.cancelaAtaqueSelectButton.place(x=0, y=150, width=128, height=55)
        for inimigo in self.enemyCells:
            if inimigo.getEntidade() != None:
                inimigo.startSelection()
        self.ataqueSelecionado = atq

    def alvoAtaqueSelecionado(self, alvo):
        alvoEntidade = alvo.getEntidade()
        self.batalha.executaAtaques(self.atualCell.getEntidade(), alvoEntidade, self.ataqueSelecionado)
        self.atualCell.updateStats()
        alvo.updateStats()
        self.updateTurnos()
        self.replaceAtaqueSelectWithMain()

    #CASO DE USO PASSAR TURNO
    def passarTurno(self):
        self.batalha.calcularTurnos("passar", "")
        self.updateTurnos()

    def selecionaItem(self):
        pass
