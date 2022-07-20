from tkinter import *
from turtle import width
from typing import TextIO
from item import Item
from ataque import Ataque
from tipo import Tipo
from batalha import Batalha

class StorageButton:
    def __init__(self, parent, width, height, itemOuAtq):
        self.parent = parent
        self.width = width
        self.height = height
        self.itemOuAtq = itemOuAtq #String, com valor item ou ent

        self.stored = None
        self.text = ""
        self.button = Button(self.parent, bg="grey99", command=lambda:self.returnCommand())

    def setStored(self, store):
        #print("eeeee")
        self.stored = store
        tempNome = self.stored.getNome()
        if self.itemOuAtq == "item":
            #print("Chegou")
            tempPotencia = str(self.stored.getPotencia())
            #print(tempPotencia)
            tempQtd = str(self.stored.getQtd())
            #print(tempQtd)
            self.text = tempNome + ":\n" + tempPotencia + " potencia\n" + tempQtd + " unidades"
        else:
            tempDano = str(self.stored.getDano())
            tempTipo = self.stored.getTipo().getNome()
            tempCusto = str(self.stored.getCusto())
            self.text = tempNome + ":\n" + tempDano + " dano\n" + tempTipo + "\n" + tempCusto + " MP"
        self.button.configure(text=self.text)

    def returnCommand(self):
        return self.stored

    def place(self, x, y):
        self.button.place(x=x, y=y, width=self.width, height=self.height)

    def place_forget(self):
        self.button.place_forget()


class DisplayCell:
    def __init__(self, parent, width, height, frameBorder, frameText, textOnly):
        self.parent = parent
        self.width = width
        self.height = height
        self.frameBorder = frameBorder
        self.frameText = frameText
        self.textOnly = textOnly
        self.entidade = None

        self.frame = LabelFrame(self.parent, bd=self.frameBorder, text=self.frameText)
        self.imagemLabel = Label(self.frame, text="Imagem")
        self.text = Text(self.frame, state='disabled')
        self.button = Button(self.frame, bg="grey99", text="Selecionar")

    def place(self,x,y):
        self.frame.place(x=x, y=y, height=self.height, width=self.width)
        if self.textOnly:
            self.text.place(relheight=1, relwidth=0.5, relx=0, rely=0)
            #self.button.place(relheight=1, relwidth=0.5, relx=0.5, rely=0)
        else:
            self.imagemLabel.place(relheight=0.75, relwidth=1, relx=0, rely=0)
            self.text.place(relheight=0.125, relwidth=1, relx=0, rely=0.75)
            #self.button.place(relheight=0.125, relwidth=1, relx=0, rely=0.875)

    def startSelection(self):
        if self.textOnly:
            self.button.place(relheight=1, relwidth=0.5, relx=0.5, rely=0)
        else:
            self.button.place(relheight=0.125, relwidth=1, relx=0, rely=0.875)

    def endSelection(self):
        self.button.place_forget()

    def insertText(self, texto):
        self.text.configure(state="normal")
        self.text.insert("0.0", texto)
        self.text.configure(state="disabled")

    #Pos no formato "x.0" onde x é a linha do texto
    #Começa por "1.0"
    #Não mudar o .0
    def replaceText(self, pos, texto):
        self.text.configure(state="normal")
        end = pos + " lineend"
        self.text.replace(pos, end, texto)
        self.text.configure(state="disabled")

    def setEntidade(self, entidade):
        self.entidade = entidade

        self.imagemLabel.configure(image=self.entidade.getImagem())

        self.replaceText("1.0", self.entidade.getNome())

        hpText = "HP = " + str(self.entidade.getHpAtual())
        self.replaceText("2.0", hpText)

        mpText = "MP = " + str(self.entidade.getMpAtual())
        self.replaceText("3.0", mpText)

    def getEntidade(self):
        return self.entidade

class BattleInterface:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Press Turn Battle")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(FALSE,FALSE)

        self.batalha = Batalha()

        #Definindo elementos
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
        self.passar_button = Button(self.menu_frame ,bg="grey99", text="Passar Turno", command=lambda:self.replaceText())

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

    def replaceAtaqueWithMain(self):
        self.unplaceAtaqueButtons()
        self.placeMainButtons()

        #PROVISORIO
        for inimigo in self.enemyCells:
            inimigo.endSelection()

    #ITEM BUTTONS
    def defineItemButtons(self):
        self.lista_item_botoes = []
        for _ in range(6):
            self.lista_item_botoes.append(StorageButton(self.menu_frame, 128, 55, "item"))
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
        self.lista_ataque_botoes = []
        for _ in range(4):
            self.lista_ataque_botoes.append(StorageButton(self.menu_frame, 128, 65, "atq"))
        self.cancelaAtaqueButton = Button(self.menu_frame, bg = "grey99", text="Cancela", command=lambda:self.replaceAtaqueWithMain())

    def placeAtaqueButtons(self):
        for i, botao in enumerate(self.lista_ataque_botoes):
            calc_pos = 75+65*i
            botao.place(0, calc_pos)
        self.cancelaAtaqueButton.place(x=0, y=335, width=128, height=55)

    def unplaceAtaqueButtons(self):
        for botao in self.lista_ataque_botoes:
            botao.place_forget()
        self.cancelaAtaqueButton.place_forget()

    def replaceMainWithAtaque(self):
        self.unplaceMainButtons()
        self.placeAtaqueButtons()

        #PROVISORIO
        for inimigo in self.enemyCells:
            inimigo.startSelection()

    #TURNOS CELL
    def defineTurnosCell(self):
        self.turnosCell = DisplayCell(self.menu_frame, 128, 75, 5, "Turnos", True)

    def placeTurnosCell(self):
        self.turnosCell.place(0,0)

    #PLAYER CELLS
    def definePlayerCells(self):
        self.campoCells = []
        for i in range(4):
            texto = "Campo {}".format(i)
            newCell = DisplayCell(self.entity_frame, 320, 96, 5, texto, True)
            self.campoCells.append(newCell)

        self.reservaCells = []
        for i in range(4):
            texto = "Reserva {}".format(i)
            newCell = DisplayCell(self.entity_frame, 320, 96, 5, texto, True)
            self.reservaCells.append(newCell)

            self.atualCell = DisplayCell(self.field_frame, 230, 528, 5, "Entidade Atual", False)

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
            newCell = DisplayCell(self.field_frame, 230, 528, 5, texto, False)
            self.enemyCells.append(newCell)

    def placeEnemyCells(self):
        for i, cell in enumerate(self.enemyCells):
            calc_pos=230*i+230
            cell.place(calc_pos, 0)

    #ENTIDADE ATUAL
    def formatEntityCells(self):
        for (campo, reserva, inimigo) in zip(self.campoCells, self.reservaCells, self.enemyCells):
            campo.insertText("NOME\nHP=100\nMP=100")
            reserva.insertText("NOME\nHP=100\nMP=100")
            inimigo.insertText("NOME\nHP=100\nMP=100")

        self.atualCell.insertText("NOME\nHP=100\nMP=100")
        self.turnosCell.insertText("10")

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
        atual = self.batalha.j1
        outro = self.batalha.j2

        inimigos = outro.getCampo()
        inimigos_humano = outro.getHumano()
        self.enemyCells[0].setEntidade(inimigos_humano)
        for i, entidade in enumerate(inimigos):
            self.enemyCells[i+1].setEntidade(entidade)

        campo = atual.getCampo()
        reserva = atual.getReserva()
        humano = atual.getHumano()
        self.campoCells[0].setEntidade(humano)
        for i, entidade in enumerate(campo):
            self.campoCells[i+1].setEntidade(entidade)
        for i, entidade in enumerate(reserva):
            self.reservaCells[i].setEntidade(entidade)
        self.atualCell.setEntidade(self.campoCells[0].getEntidade())

        self.setItems(atual.getTodosItens())
        self.setAtaques(self.atualCell.getEntidade().getAtaques())