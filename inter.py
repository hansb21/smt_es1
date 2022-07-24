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
        #aLabel = Label(self.table_frame, bd = 0, image=self.an_image)

        self.logo_label = Label(self.table_frame, bd = 0, image=self.logo)
        self.logo_label.grid(row=0, column=3)
        self.message_label = Label(self.message_frame, bg="gray", text=' Shin Megami Tem 6 - Press Turn Battle', font="arial 15")
        self.message_label.grid(row=2, column=6)
        
        self.startb = Button(self.message_frame,
                           text="Começar",
                           command=self.fill_character)
        self.endb = Button(self.message_frame,
                            text="Sair",
                            command=lambda:self.main_window.destroy())
        self.startb.grid(row=3, column=6)
        self.endb.grid(row=4, column=6)
    def fill_character(self):
        self.clear_frame()
        
        p1 = Label(self.table_frame, text= "Player 1",  width=15, font=("Arial", 25))
        p2 = Label(self.table_frame, text= "Player 2", width=15, font=("Arial", 25))
        p1.grid(row = 0, column = 0)
        p2.grid(row = 0, column = 80)
        
        self.humano1 = PhotoImage(file='images/sprites/humanos/humano1.png')
        self.humano2 = PhotoImage(file='images/sprites/humanos/humano2.png')
        p1b = Button(self.message_frame, text="PLAYER 1", font=("Arial",25), height=150, width=58, image=self.humano1)
        p2b = Button(self.message_frame, text="PLAYER 2", font=("Arial",25), height=150, width=58, image=self.humano2)
        p1b.grid(row=1, column=0)
        p2b.grid(row=1, column=80)
        
        #self.liu_image = PhotoImage(file="images/liu.png")
        for y in range(2):
            a_column = [] # column
            for x in range(5):
                dliu = Label(self.message_frame, bd = 0, bg="gray")
                dliu.grid(row=x+1 , column=y+1)
        confirm_bp1 = Button(self.message_frame, font=("Arial", 10),  text="CONFIRM", bg="gray", height=2, width=15)
        confirm_bp2 = Button(self.message_frame, font=("Arial", 10),  text="CONFIRM", bg="gray", height=2, width=15)
        confirm_bp1.grid(row=2, column=0)
        confirm_bp2.grid(row=2, column=80)

    def print_hello(self):
        print("hello world")

    def clear_frame(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        for widget in self.message_frame.winfo_children():
             widget.destroy()
PlayerInterface()
