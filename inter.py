from tkinter import *


class PlayerInterface:
    def __init__(self):
        self.main_window = Tk() # instanciar Tk (que implementa a janela)
        self.fill_main_window()
        # preenchimento da janela
        self.main_window.mainloop() # abrir a janela

    def fill_main_window(self):
        # Título, ícone, dimensionamento e fundo da janela
        self.main_window.title("Shin Megami Tem 6 - Press Turn Battle")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(True, True)
        self.main_window["bg"]="gray"
        # Criação de 2 frames e organização da janela em um grid de 2 linhas e 1 coluna,
        # sendo que table_frame ocupa a linha superior e message_frame, a inferior
        self.table_frame = Frame(self.main_window, padx=100, pady=25, bg="gray")
        self.table_frame.grid(row=0 , column=0)
        self.message_frame = Frame(self.main_window, padx=0, pady=10, bg="gray")
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
        self.logo_label = Label(self.table_frame, bd = 0, image=self.logo)
        self.logo_label.grid(row=0, column=3)
        self.message_label = Label(self.message_frame, bg="gray", text=' Shin Megami Tem 6 - Press Turn Battle', font="arial 15")
        self.message_label.grid(row=2, column=6)
        
        self.startb = Button(self.message_frame,
                           text="Começar",
                           command=self.clear_frame)
        self.endb = Button(self.message_frame,
                            text="Sair",
                            command=lambda:exit())
        self.startb.grid(row=3, column=6)
        self.endb.grid(row=4, column=6)

    def print_hello(self):
        print("hello world")

    def clear_frame(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        for widget in self.message_frame.winfo_children():
             widget.destroy()
PlayerInterface()
