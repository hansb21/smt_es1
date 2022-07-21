from tkinter import *

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
        self.updateStats()

    def updateStats(self):
        self.replaceText("1.0", self.entidade.getNome())

        hpText = "HP = " + str(self.entidade.getHpAtual())
        self.replaceText("2.0", hpText)

        mpText = "MP = " + str(self.entidade.getMpAtual())
        self.replaceText("3.0", mpText)

    def getEntidade(self):
        return self.entidade
