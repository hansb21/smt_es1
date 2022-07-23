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

        self.batalha = Batalha(self)

        #"ataque", "item", "invoca1", "invoca2", "fusao1", "fusao2"
        self.tipoSelecao = ""
        self.ataqueSelecionado = None
        self.itemSelecionado = None

        self.reservaSelecionado = None
        self.campoSelecionado = None

        self.fusao1 = None
        self.fusao2 = None

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
        self.defineSelectionLabel()
        self.defineCancelaButtons()

        #Inicializar
        self.placeFrames()
        self.placeMainButtons()
        self.placeTurnosCell()
        self.placePlayerCells()
        self.placeEnemyCells()
        self.formatEntityCells()

        #TESTE
        self.setJogadores()

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
        self.fundir_button = Button(self.menu_frame ,bg="grey99", text="Fusão", command=lambda:self.replaceMainWithFusao())
        self.invocar_button = Button(self.menu_frame ,bg="grey99", text="Invocar", command=lambda:self.replaceMainWithInvocar())
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
        
    #ATAQUE BUTTONS
    def defineAtaqueButtons(self):
        #Antes de selecionar ataque
        self.lista_ataque_botoes = []
        for _ in range(4):
            self.lista_ataque_botoes.append(StorageButton(self.menu_frame, 128, 65, "atq", self))

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

    #Selection Label
    def defineSelectionLabel(self):
        self.selectionLabel = Label(self.menu_frame, text = "")
        self.selectionLabel2 = Label(self.menu_frame, text = "")

    #Cancela buttons
    def defineCancelaButtons(self):
        self.cancelaItemButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceItemWithMain())
        self.cancelaAtaqueButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceAtaqueWithMain())
        self.cancelaAtaqueSelectButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceAtaqueSelectWithMain())
        self.cancelaItemSelectButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceItemSelectWithMain())
        self.cancelaInovcarButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceInvocarWithMain())
        self.cancelaFusaoButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceFusaoWithMain())

        self.confirmaInvocarButton = Button(self.menu_frame, bg = "grey99", text="Confirma", command=lambda:self.confirmaInvocar())
        self.confirmaFusaoButton = Button(self.menu_frame, bg = "grey99", text="Confirma", command=lambda:self.confirmaFusao())


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

    def setJogadores(self):
        self.defineJogadores()
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
            print(entidade)
            self.reservaCells[i].setEntidade(entidade)
        self.atualCell.setEntidade(self.campoCells[0].getEntidade())

        self.setItems(self.jogadorAtual.getTodosItens())
        self.setAtaques(self.atualCell.getEntidade().getAtaques())
        self.inimigoReservaEntidades = self.jogadorOutro.getReserva()

    def resetJogadores(self):
        self.defineJogadores()
        campoPassado = []
        for cell in self.campoCells:
            campoPassado.append(cell.getEntidade())
        reservaPassado = []
        for cell in self.reservaCells:
            reservaPassado.append(cell.getEntidade())
        inimigosPassado = []
        for cell in self.enemyCells:
            inimigosPassado.append(cell.getEntidade())
        inimigosReservaPassado = []
        for entidade in self.inimigoReservaEntidades:
            inimigosReservaPassado.append(entidade)

        for i in range(4):
            self.campoCells[i].setEntidade(inimigosPassado[i])
            self.reservaCells[i].setEntidade(inimigosReservaPassado[i])
            self.enemyCells[i].setEntidade(campoPassado[i])
            self.inimigoReservaEntidades[i] = reservaPassado[i]

        self.atualCell.setEntidade(self.campoCells[0].getEntidade())

        self.updateTurnos()
        
    #Seleção geral
    def alvoSelecionado(self, cell):
        if self.tipoSelecao == "ataque":
            self.alvoSelecionadoAtaque(cell)
        elif self.tipoSelecao == "item":
            self.alvoSelecionadoItem(cell)
        elif self.tipoSelecao == "invocar1":
            self.alvoSelecionadoInvocar1(cell)
        elif self.tipoSelecao == "invocar2":
            self.alvoSelecionadoInvocar2(cell)
        elif self.tipoSelecao == "fusao1":
            self.alvoSelecionadoFusao1(cell)
        elif self.tipoSelecao == "fusao2":
            self.alvoSelecionadoFusao2(cell)
        else:
            print("ERRO")

    #CASO DE USO ATAQUE
    def replaceMainWithAtaque(self):
        self.unplaceMainButtons()
        self.placeAtaqueButtons()

    def replaceAtaqueWithMain(self):
        self.unplaceAtaqueButtons()
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
        self.selectionLabel.configure(text=labelText)
        self.selectionLabel.place(x=0, y=75, width=128, height=75)
        self.cancelaAtaqueSelectButton.place(x=0, y=150, width=128, height=55)
        for inimigo in self.enemyCells:
            if inimigo.getEntidade() != None and inimigo.getVivo():
                inimigo.startSelection()
        self.ataqueSelecionado = atq
        self.tipoSelecao = "ataque"

    def replaceAtaqueSelectWithMain(self):
        self.selectionLabel.place_forget()
        self.cancelaAtaqueSelectButton.place_forget()
        for inimigo in self.enemyCells:
            inimigo.endSelection()
        self.ataqueSelecionado = None
        self.tipoSelecao = ""
        self.placeMainButtons()

    def alvoSelecionadoAtaque(self, alvo):
        alvoEntidade = alvo.getEntidade()
        self.batalha.executaAtaques(self.atualCell.getEntidade(), alvoEntidade, self.ataqueSelecionado, self.campoCells, self.atualCell)
        self.atualCell.updateStats()
        alvo.updateStats()
        self.updateTurnos()
        self.replaceAtaqueSelectWithMain()
        self.ataqueSelecionado = None

    #CASO DE USO USAR ITEM
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

    def replaceItemWithItemSelect(self, item):
        if item.getQtd() <= 0:
            return

        self.unplaceItemButtons()
        tempNome = item.getNome()
        tempPotencia = str(item.getPotencia())
        tempQtd = str(item.getQtd())
        labelText = "SELECIONADO: \n" + tempNome + ":\n" + tempPotencia + " potencia\n" + tempQtd + " unidades"
        self.selectionLabel.configure(text=labelText)
        self.selectionLabel.place(x=0, y=75, width=128, height=75)
        self.cancelaItemSelectButton.place(x=0, y=150, width=128, height=55)
        for i in range(4):
            self.campoCells[i].startSelection()
            self.reservaCells[i].startSelection()
        self.itemSelecionado = item
        self.tipoSelecao = "item"

    def replaceItemSelectWithMain(self):
        self.selectionLabel.place_forget()
        self.cancelaItemSelectButton.place_forget()
        for ent in self.campoCells:
            ent.endSelection()
        for ent in self.reservaCells:
            ent.endSelection()
        self.itemSelecionado = None
        self.tipoSelecao = ""
        self.placeMainButtons()

    def alvoSelecionadoItem(self, alvo):
        alvoEntidade = alvo.getEntidade()
        self.batalha.usarItem(self.itemSelecionado, alvoEntidade, self.campoCells, self.atualCell)
        alvo.updateStats()
        self.atualCell.updateStats()
        self.updateTurnos()
        self.replaceItemSelectWithMain()
        for button in self.lista_item_botoes:
            button.updateText()
        self.ataqueSelecionado = None

    #CASO DE USO INVOCAR
    def replaceMainWithInvocar(self):
        self.unplaceMainButtons()
        labelText = "SELECIONADO:"
        self.selectionLabel.configure(text=labelText)
        self.selectionLabel2.configure(text=labelText)
        self.selectionLabel.place(x=0, y=75, width=128, height=75)
        self.selectionLabel2.place(x=0, y=150, width=128, height=75)
        self.cancelaInovcarButton.place(x=0, y=225, width=128, height=55)
        for cell in self.reservaCells:
            cell.startSelection()
        self.tipoSelecao = "invocar1"

    def replaceInvocarWithMain(self):
        for cell in self.reservaCells:
            cell.endSelection()
        self.selectionLabel.place_forget()
        self.selectionLabel2.place_forget()
        self.cancelaInovcarButton.place_forget()
        self.confirmaInvocarButton.place_forget()
        self.tipoSelecao = ""
        self.reservaSelecionado = None
        self.campoSelecionado = None
        self.placeMainButtons()

    def alvoSelecionadoInvocar1(self, cell):
        tempNome = cell.getEntidadeNome()
        labelText = "SELECIONADO: \n" + tempNome
        self.selectionLabel.configure(text=labelText)
        self.reservaSelecionado = cell
        for ent in self.reservaCells:
            ent.endSelection()
        for ent in self.campoCells:
            if not ent.getEhHumano():
                ent.startSelection()
        self.tipoSelecao = "invocar2"

    def alvoSelecionadoInvocar2(self, cell):
        tempNome = cell.getEntidadeNome()
        labelText = "SELECIONADO: \n" + tempNome
        self.selectionLabel2.configure(text=labelText)
        for ent in self.campoCells:
            ent.endSelection()
        self.campoSelecionado = cell
        self.confirmaInvocarButton.place(x=0, y=280, width=128, height=55)
        
    def confirmaInvocar(self):
        self.batalha.invocar(self.reservaSelecionado, self.campoSelecionado, self.campoCells, self.atualCell)
        self.reservaSelecionado.updateStats()
        self.campoSelecionado.updateStats()
        self.reservaSelecionado = None
        self.campoSelecionado = None
        self.updateTurnos()
        self.replaceInvocarWithMain()

    #CASO DE USO FUSAO
    def replaceMainWithFusao(self):
        self.unplaceMainButtons()
        labelText = "SELECIONADO:"
        self.selectionLabel.configure(text=labelText)
        self.selectionLabel2.configure(text=labelText)
        self.selectionLabel.place(x=0, y=75, width=128, height=75)
        self.selectionLabel2.place(x=0, y=150, width=128, height=75)
        self.cancelaFusaoButton.place(x=0, y=225, width=128, height=55)
        for cell in self.reservaCells:
            cell.startSelection()
        for cell in self.campoCells:
            if not cell.getEhHumano() and not cell.getVazio():
                cell.startSelection()
        self.tipoSelecao = "fusao1"

    def replaceFusaoWithMain(self):
        for cell in self.reservaCells:
            cell.endSelection()
        for cell in self.campoCells:
            cell.endSelection()
        self.selectionLabel.place_forget()
        self.selectionLabel2.place_forget()
        self.cancelaFusaoButton.place_forget()
        self.confirmaFusaoButton.place_forget()
        self.fusao1 = None
        self.fusao2 = None
        self.tipoSelecao = ""
        self.placeMainButtons()

    def alvoSelecionadoFusao1(self, cell):
        tempNome = cell.getEntidadeNome()
        labelText = "SELECIONADO: \n" + tempNome
        self.selectionLabel.configure(text=labelText)
        self.fusao1 = cell
        self.tipoSelecao = "fusao2"
        cell.endSelection()

    def alvoSelecionadoFusao2(self, cell):
        tempNome = cell.getEntidadeNome()
        labelText = "SELECIONADO: \n" + tempNome
        self.selectionLabel2.configure(text=labelText)
        for ent in self.campoCells:
            ent.endSelection()
        for ent in self.reservaCells:
            ent.endSelection()
        self.fusao2 = cell
        self.confirmaFusaoButton.place(x=0, y=280, width=128, height=55)

    def confirmaFusao(self):
        self.batalha.fundir(self.fusao1, self.fusao2, self.campoCells, self.atualCell)
        self.fusao1 = None
        self.fusao2 = None
        self.updateTurnos()
        self.replaceFusaoWithMain()


    #CASO DE USO PASSAR TURNO
    def passarTurno(self):
        self.batalha.calcularTurnos("passar", "", self.campoCells, self.atualCell)
        self.updateTurnos()

    #Mudar entidade
