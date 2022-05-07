from tkinter import *
from turtle import width

class BattleInterface:
    def __init__(self):
        self.main_window = Tk()
        self.fill_main_window()
        self.main_window.mainloop()

    def fill_main_window(self):
        self.main_window.title("Press Turn Battle")
        #self.main_window.iconbitmap("images/icon.ico")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(FALSE,FALSE)
        #self.main_window["bg"]="gold3"

        #FRAMES
        self.menu_frame = Frame(self.main_window, bg="red", width=256, height=528)
        self.menu_frame.place(x=0, y=0)

        self.field_frame = Frame(self.main_window, bg="green", width=1024, height=528)
        self.field_frame.place(x=256, y=0)

        self.entity_frame = Frame(self.main_window, bg="blue", width=1280, height=192)
        self.entity_frame.place(x=0, y=528)

        #BOTOES
        self.ataque_button = Button(self.menu_frame ,bg="grey99", text="Ataque")
        self.magia_button = Button(self.menu_frame ,bg="grey99", text="Magias")
        self.item_button = Button(self.menu_frame ,bg="grey99", text="Itens")
        self.fundir_button = Button(self.menu_frame ,bg="grey99", text="Fusão")
        self.invocar_button = Button(self.menu_frame ,bg="grey99", text="Invocar")
        self.passar_button = Button(self.menu_frame ,bg="grey99", text="Passar Turno")

        self.lista_botoes = [self.ataque_button, self.magia_button, self.item_button, self.fundir_button, self.invocar_button,self.passar_button]
        for i, botao in enumerate(self.lista_botoes):
            calc_pos=70*i
            botao.place(x=0, y=calc_pos, width=256, height=70)

        #LABELFRAME DOS TURNOS
        self.turnos_frame = LabelFrame(self.menu_frame, bd=5, text="Turnos")
        self.turnos_frame.place(x=0,y=420, width=256,height=108)

        #LABEL DOS TURNOS
        #substituir por um sistema de imagens dps
        self.turnos_label = Label(self.turnos_frame, text="5")
        self.turnos_label.place(relheight=1, relwidth=1)

        #LABELFRAMES DOS INIMIGOS
        #Usar como pai dos labels dos inimigos (não implementar agora)
        self.inimigo1_frame = LabelFrame(self.field_frame, bd=5, text="Inimigo 1")
        self.inimigo2_frame = LabelFrame(self.field_frame, bd=5, text="Inimigo 2")
        self.inimigo3_frame = LabelFrame(self.field_frame, bd=5, text="Inimigo 3")
        self.inimigo4_frame = LabelFrame(self.field_frame, bd=5, text="Inimigo 4")

        self.lista_inimigo_frames = [self.inimigo1_frame, self.inimigo2_frame, self.inimigo3_frame, self.inimigo4_frame]
        for i, inimigoFrame in enumerate(self.lista_inimigo_frames):
            calc_pos=256*i
            inimigoFrame.place(x=calc_pos,y=0,width=256,height=528)

        #LABELS DOS INIMIGOS
        #Colocar imagens dps
        self.inimigo1_label = Label(self.inimigo1_frame, text="Imagem 1")
        self.inimigo2_label = Label(self.inimigo2_frame, text="Imagem 2")
        self.inimigo3_label = Label(self.inimigo3_frame, text="Imagem 3")
        self.inimigo4_label = Label(self.inimigo4_frame, text="Imagem 4")

        self.lista_inimigo_labels = [self.inimigo1_label, self.inimigo2_label, self.inimigo3_label, self.inimigo4_label]
        for inimigoLabel in self.lista_inimigo_labels:
            inimigoLabel.place(relheight=1, relwidth=1)


        #LABELFRAMES DO TIME
        #Usar como pai dos labels do time (não implementar agora)
        self.time1_frame = LabelFrame(self.entity_frame, bd=5, text="Entidade 1")
        self.time2_frame = LabelFrame(self.entity_frame, bd=5, text="Entidade 2")
        self.time3_frame = LabelFrame(self.entity_frame, bd=5, text="Entidade 3")
        self.time4_frame = LabelFrame(self.entity_frame, bd=5, text="Entidade 4")

        self.lista_time_frames = [self.time1_frame, self.time2_frame, self.time3_frame, self.time4_frame]
        for i, timeFrame in enumerate(self.lista_time_frames):
            calc_pos=320*i
            timeFrame.place(x=calc_pos,y=0,width=320,height=192)

        #LABELS DO TIME
        #Colocar imagens dps
        self.time1_label = Label(self.time1_frame, text="Imagem 1")
        self.time2_label = Label(self.time2_frame, text="Imagem 2")
        self.time3_label = Label(self.time3_frame, text="Imagem 3")
        self.time4_label = Label(self.time4_frame, text="Imagem 4")
        
        self.lista_time_labels = [self.time1_label,self.time2_label,self.time3_label,self.time4_label]
        for timeLabel in self.lista_time_labels:
            timeLabel.place(relheight=1, relwidth=1)

battle_interface = BattleInterface()