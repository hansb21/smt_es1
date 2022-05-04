from tkinter import *


class PlayerInterface:
    def __init__(self):
        self.main_window = Tk() # instanciar Tk (que implementa a janela)
        self.fill_main_window()
        # preenchimento da janela
        self.main_window.mainloop() # abrir a janela

    def fill_main_window(self):
        # Título, ícone, dimensionamento e fundo da janela
        self.main_window.title("Shin Megami Tem 6")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(False, False)
        self.main_window["bg"]="DarkOrchid2"
        # Criação de 2 frames e organização da janela em um grid de 2 linhas e 1 coluna,
        # sendo que table_frame ocupa a linha superior e message_frame, a inferior
        self.table_frame = Frame(self.main_window, padx=100, pady=25, bg="DarkOrchid2")
        self.table_frame.grid(row=0 , column=0)
        self.message_frame = Frame(self.main_window, padx=0, pady=10, bg="DarkOrchid2")
        self.message_frame.grid(row=1 , column=0)
        self.an_image = PhotoImage(file="images/battle_fill.png") #pyimage1
        self.logo = PhotoImage(file="images/smt_logo.png") #pyimage2
        self.board_view=[]
        #for y in range(2):
           # a_column = [] # column
            #for x in range(2):
        aLabel = Label(self.table_frame, bd = 0, image=self.an_image)
            #    aLabel.grid(row=x , column=y)
             #   a_column.append(aLabel)
        #self.board_view.append(a_column)
        self.logo_label = Label(self.message_frame, bd = 0, image=self.logo)
        self.logo_label.grid(row=0, column=0)
        self.message_label = Label(self.message_frame, bg="gold3", text=' Gobblet Gobblers', font="arial 30")
        self.message_label.grid(row=0, column=1)

PlayerInterface()
