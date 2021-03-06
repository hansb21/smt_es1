from tkinter import *

class StorageButton:
    def __init__(self, parent, width, height, itemOuAtq, interface):
        self.parent = parent
        self.width = width
        self.height = height
        self.itemOuAtq = itemOuAtq #String, com valor item ou ent
        self.interface = interface

        self.stored = None
        self.text = ""
        self.button = Button(self.parent, bg="grey99", command=self.buttonCommand)

    def setStored(self, store):
        self.stored = store
        tempNome = self.stored.getNome()
        if self.itemOuAtq == "item":
            tempPotencia = str(self.stored.getPotencia())
            tempQtd = str(self.stored.getQtd())
            self.text = tempNome + ":\n" + tempPotencia + " potencia\n" + tempQtd + " unidades"
        else:
            tempDano = str(self.stored.getDano())
            tempTipo = self.stored.getTipo().getNome()
            tempCusto = str(self.stored.getCusto())
            self.text = tempNome + ":\n" + tempDano + " dano\n" + tempTipo + "\n" + tempCusto + " MP"
        self.button.configure(text=self.text)

    def updateText(self):
        self.setStored(self.stored)

    def buttonCommand(self):
        if self.itemOuAtq == "atq":
            self.interface.replaceAtaqueWithAtaqueSelect(self.stored)
        else:
            self.interface.replaceItemWithItemSelect(self.stored)

    def place(self, x, y):
        self.button.place(x=x, y=y, width=self.width, height=self.height)

    def place_forget(self):
        self.button.place_forget()