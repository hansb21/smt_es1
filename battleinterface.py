from tkinter import *
from turtle import width
from typing import TextIO

class DisplayCell:
    def __init__(self, parent, width, height, frameBorder, frameText, textOnly):
        self.parent = parent
        self.width = width
        self.height = height
        self.frameBorder = frameBorder
        self.frameText = frameText
        self.textOnly = textOnly

        self.frame = LabelFrame(self.parent, bd=self.frameBorder, text=self.frameText)
        self.imagem = Label(self.frame, text="Imagem")
        self.text = Text(self.frame, state='disabled')

    def place(self,x,y):
        self.frame.place(x=x, y=y, height=self.height, width=self.width)
        if self.textOnly:
            self.text.place(relheight=1, relwidth=1, relx=0, rely=0)
        else:
            self.imagem.place(relheight=0.75, relwidth=1, relx=0, rely=0)
            self.text.place(relheight=0.25, relwidth=1, relx=0, rely=0.75)
        print("placed")

    def insertText(self, texto):
        self.text.configure(state="normal")
        self.text.insert("0.0", texto)
        self.text.configure(state="disabled")

    def replaceTest(self, pos, texto):
        self.text.configure(state="normal")
        end = pos + " lineend"
        self.text.replace(pos, end, texto)
        self.text.configure(state="disabled")

class BattleInterface:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Press Turn Battle")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(FALSE,FALSE)

        #Definindo elementos
        self.defineFrames()
        self.defineMainButtons()
        self.defineTurnosCell()
        self.definePlayerCells()
        self.defineEnemyCells()

        #self.fill_main_window()
        self.placeFrames()
        self.placeMainButtons()
        self.placeTurnosCell()
        self.placePlayerCells()
        self.placeEnemyCells()

        self.formatEntityCells()

        self.main_window.mainloop()

    def defineFrames(self):
        self.menu_frame = Frame(self.main_window, bg="red", width=128, height=528)
        self.field_frame = Frame(self.main_window, bg="green", width=1152, height=528)
        self.entity_frame = Frame(self.main_window, bg="blue", width=1280, height=192)

    def placeFrames(self):
        self.menu_frame.place(x=0, y=0)
        self.field_frame.place(x=128, y=0)
        self.entity_frame.place(x=0, y=528)

    def defineMainButtons(self):
        self.ataque_button = Button(self.menu_frame ,bg="grey99", text="Ataque", command=lambda:self.unplaceAll())
        self.item_button = Button(self.menu_frame ,bg="grey99", text="Itens", command=lambda:self.debug_button("Uso de item"))
        self.fundir_button = Button(self.menu_frame ,bg="grey99", text="Fusão", command=lambda:self.debug_button("Ritual de fusão") )
        self.invocar_button = Button(self.menu_frame ,bg="grey99", text="Invocar", command=lambda:self.debug_button("Ritual de invocação"))
        self.passar_button = Button(self.menu_frame ,bg="grey99", text="Passar Turno", command=lambda:self.replaceTest())

        self.lista_botoes = [   self.ataque_button, 
                                self.item_button, 
                                self.fundir_button, 
                                self.invocar_button,
                                self.passar_button]

    def placeMainButtons(self):
        for i, botao in enumerate(self.lista_botoes):
            calc_pos=75+55*i
            botao.place(x=0, y=calc_pos, width=128, height=55)

    def defineTurnosCell(self):
        self.turnosCell = DisplayCell(self.menu_frame, 128, 75, 5, "Turnos", True)

    def placeTurnosCell(self):
        self.turnosCell.place(0,0)

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

    def formatEntityCells(self):
        for (campo, reserva, inimigo) in zip(self.campoCells, self.reservaCells, self.enemyCells):
            campo.insertText("NOME\nHP=100\nMP=100")
            reserva.insertText("NOME\nHP=100\nMP=100")
            inimigo.insertText("NOME\nHP=100\nMP=100")

        self.atualCell.insertText("NOME\nHP=100\nMP=100")
        self.turnosCell.insertText("10")

    def replaceTest(self):
        self.campoCells[0].replaceTest("2.0", "REPLACE")

    def debug_button(self, escolha):
        print(f"{escolha} realizado sucesso")

    def unplaceAll(self):
        for widget in self.main_window.place_slaves():
            widget.place_forget()

battle_interface = BattleInterface()
