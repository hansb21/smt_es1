from tkinter import *

class DisplayCell:
    def __init__(self, parent, width, height, frameBorder, frameText, textOnly, interface):
        self.parent = parent
        self.width = width
        self.height = height
        self.frameBorder = frameBorder
        self.frameText = frameText
        self.textOnly = textOnly
        self.interface = interface
        self.entidade = None

        self.frame = LabelFrame(self.parent, bd=self.frameBorder, text=self.frameText)
        self.imagemLabel = Label(self.frame, text="Imagem")
        self.text = Text(self.frame, state='disabled')
        self.button = Button(self.frame, bg="grey99", text="Selecionar", command=self.buttonCommand)

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
        if self.entidade == None:
            self.imagemLabel.configure(image=None)
        else:
            self.imagemLabel.configure(image=self.entidade.getImagem())
        self.updateStats()

    def updateStats(self):
        if self.entidade == None:
            self.replaceText("1.0", "VAZIO")
            self.replaceText("2.0", "")
            self.replaceText("3.0", "")
            return

        self.replaceText("1.0", self.entidade.getNome())

        hpText = "HP = " + str(self.entidade.getHpAtual()) + " / " + str(self.entidade.getHpMax())
        self.replaceText("2.0", hpText)

        mpText = "MP = " + str(self.entidade.getMpAtual())
        self.replaceText("3.0", mpText)

    def getEntidade(self):
        return self.entidade

    def getEntidadeNome(self):
        if self.entidade == None:
            return "VAZIO"
        return self.entidade.getNome()

    def getLocal(self):
        if self.entidade == None:
            return "vazio"
        else:
            return self.entidade.getLocal()

    def changeLocal(self):
        if self.entidade == None:
            return
        if self.entidade.getLocal() == 0:
            self.entidade.setLocal(1)
        else:
            self.entidade.setLocal(0)

    def getEhHumano(self):
        if self.entidade == None:
            return False
        return self.entidade.getEhHumano()

    def getVazio(self):
        if self.entidade == None:
            return True
        else:
            return False

    def buttonCommand(self):
        self.interface.alvoSelecionado(self)
