from tkinter import *
from turtle import width

class BattleInterface:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Press Turn Battle")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(FALSE,FALSE)

        #Definindo elementos
        self.defineFrames()
        self.defineButtons()
        self.defineLabelFrames()
        self.defineLabels()

        self.fill_main_window()
        self.main_window.mainloop()

    def defineFrames(self):
        self.menu_frame = Frame(self.main_window, bg="red", width=128, height=528)
        self.field_frame = Frame(self.main_window, bg="green", width=1152, height=528)
        self.entity_frame = Frame(self.main_window, bg="blue", width=1280, height=192)

    def defineButtons(self):
        self.ataque_button = Button(self.menu_frame ,bg="grey99", text="Ataque", command=lambda:self.unplaceAll())
        self.item_button = Button(self.menu_frame ,bg="grey99", text="Itens", command=lambda:self.debug_button("Uso de item"))
        self.fundir_button = Button(self.menu_frame ,bg="grey99", text="Fusão", command=lambda:self.debug_button("Ritual de fusão") )
        self.invocar_button = Button(self.menu_frame ,bg="grey99", text="Invocar", command=lambda:self.debug_button("Ritual de invocação"))
        self.passar_button = Button(self.menu_frame ,bg="grey99", text="Passar Turno", command=lambda:self.debug_button("Passagem de turno"))

        self.lista_botoes = [   self.ataque_button, 
                                self.item_button, 
                                self.fundir_button, 
                                self.invocar_button,
                                self.passar_button]

    def defineLabelFrames(self):
        #LABELFRAME DOS TURNOS
        self.turnos_frame = LabelFrame(self.menu_frame, bd=5, text="Turnos")

        #LABELFRAME DA ENTIDADE ATUAL
        self.entidade_atual_frame = LabelFrame(self.field_frame, bd=5, text="Entidade atual")

        #LABELFRAMES DOS INIMIGOS
        #Usar como pai dos labels dos inimigos
        self.inimigo1_frame = LabelFrame(self.field_frame, bd=5, text="Inimigo 1")
        self.inimigo2_frame = LabelFrame(self.field_frame, bd=5, text="Inimigo 2")
        self.inimigo3_frame = LabelFrame(self.field_frame, bd=5, text="Inimigo 3")
        self.inimigo4_frame = LabelFrame(self.field_frame, bd=5, text="Inimigo 4")
        self.lista_inimigo_frames = [   self.inimigo1_frame, 
                                        self.inimigo2_frame, 
                                        self.inimigo3_frame, 
                                        self.inimigo4_frame]

        #LABELFRAMES DO TIME
        #Usar como pai dos labels do time
        #Campo
        self.campo1_frame = LabelFrame(self.entity_frame, bd=5, text="Campo 1")
        self.campo2_frame = LabelFrame(self.entity_frame, bd=5, text="Campo 2")
        self.campo3_frame = LabelFrame(self.entity_frame, bd=5, text="Campo 3")
        self.campo4_frame = LabelFrame(self.entity_frame, bd=5, text="Campo 4")
        self.lista_time_frames = [  self.campo1_frame, 
                                    self.campo2_frame, 
                                    self.campo3_frame, 
                                    self.campo4_frame]
        #Reserva
        self.reserva1_frame = LabelFrame(self.entity_frame, bd=5, text="Reserva 1")
        self.reserva2_frame = LabelFrame(self.entity_frame, bd=5, text="Reserva 2")
        self.reserva3_frame = LabelFrame(self.entity_frame, bd=5, text="Reserva 3")
        self.reserva4_frame = LabelFrame(self.entity_frame, bd=5, text="Reserva 4")
        self.reserva5_frame = LabelFrame(self.entity_frame, bd=5, text="Reserva 5")
        self.reserva6_frame = LabelFrame(self.entity_frame, bd=5, text="Reserva 6")
        self.reserva7_frame = LabelFrame(self.entity_frame, bd=5, text="Reserva 7")
        self.reserva8_frame = LabelFrame(self.entity_frame, bd=5, text="Reserva 8")
        self.lista_reserva_frames = [   self.reserva1_frame, 
                                        self.reserva2_frame, 
                                        self.reserva3_frame, 
                                        self.reserva4_frame, 
                                        self.reserva5_frame, 
                                        self.reserva6_frame, 
                                        self.reserva7_frame, 
                                        self.reserva8_frame]

    def defineLabels(self):
        #LABEL DOS TURNOS
        self.turnos_label = Label(self.turnos_frame, text="5")
        self.turnos_label.place(relheight=1, relwidth=1)

        #LABELS DOS INIMIGOS
        self.inimigo1_label = Label(self.inimigo1_frame, text="Imagem 1")
        self.inimigo2_label = Label(self.inimigo2_frame, text="Imagem 2")
        self.inimigo3_label = Label(self.inimigo3_frame, text="Imagem 3")
        self.inimigo4_label = Label(self.inimigo4_frame, text="Imagem 4")
        self.lista_inimigo_labels = [   self.inimigo1_label, 
                                        self.inimigo2_label, 
                                        self.inimigo3_label, 
                                        self.inimigo4_label]

        #LABELS DO TIME
        #Campo
        self.campo1_label = Label(self.campo1_frame, text="Imagem 1")
        self.campo2_label = Label(self.campo2_frame, text="Imagem 2")
        self.campo3_label = Label(self.campo3_frame, text="Imagem 3")
        self.campo4_label = Label(self.campo4_frame, text="Imagem 4")
        self.lista_campo_labels = [  self.campo1_label,
                                    self.campo2_label,
                                    self.campo3_label,
                                    self.campo4_label]
        #Reserva
        self.reserva1_label = Label(self.reserva1_frame, text="Imagem 1")
        self.reserva2_label = Label(self.reserva2_frame, text="Imagem 2")
        self.reserva3_label = Label(self.reserva3_frame, text="Imagem 3")
        self.reserva4_label = Label(self.reserva4_frame, text="Imagem 4")
        self.reserva5_label = Label(self.reserva5_frame, text="Imagem 1")
        self.reserva6_label = Label(self.reserva6_frame, text="Imagem 2")
        self.reserva7_label = Label(self.reserva7_frame, text="Imagem 3")
        self.reserva8_label = Label(self.reserva8_frame, text="Imagem 4")
        self.lista_reserva_labels = [  self.reserva1_label,
                                    self.reserva2_label,
                                    self.reserva3_label,
                                    self.reserva4_label,
                                    self.reserva5_label,
                                    self.reserva6_label,
                                    self.reserva7_label,
                                    self.reserva8_label]


    def fill_main_window(self):

        self.menu_frame.place(x=0, y=0)

        self.field_frame.place(x=128, y=0)

        self.entity_frame.place(x=0, y=528)

        for i, botao in enumerate(self.lista_botoes):
            calc_pos=55*i
            botao.place(x=0, y=calc_pos, width=128, height=55)

        self.turnos_frame.place(x=0,y=275, width=128,height=55)

        self.entidade_atual_frame.place(x=0, y=0,width=230, height=528)

        for i, inimigoFrame in enumerate(self.lista_inimigo_frames):
            calc_pos=230*i+230
            inimigoFrame.place(x=calc_pos,y=0,width=230,height=528)

        for inimigoLabel in self.lista_inimigo_labels:
            inimigoLabel.place(relheight=1, relwidth=1)

        for i, campoFrame in enumerate(self.lista_time_frames):
            calc_pos=320*i
            campoFrame.place(x=calc_pos,y=0,width=320,height=96)
       
        for i, reservaFrame in enumerate(self.lista_reserva_frames):
            calc_pos=160*i
            reservaFrame.place(x=calc_pos,y=96,width=160,height=96)

        for campoLabel in self.lista_campo_labels:
            campoLabel.place(relheight=1, relwidth=1)

        for reservaLabel in self.lista_reserva_labels:
            reservaLabel.place(relheight=1, relwidth=1)
        

    def debug_button(self, escolha):
        print(f"{escolha} realizado sucesso")

    def unplaceAll(self):
        for widget in self.main_window.place_slaves():
            widget.place_forget()

battle_interface = BattleInterface()
