from tkinter import *
# Importujeme len názvy, samotné moduly importujeme vo funkciách
# aby sme predišli circular importom

class Menu:
    def __init__(self, master):
        self.master = master
        # Čistenie predchádzajúcich widgetov (ak sa vraciame z iného okna)
        for widget in self.master.winfo_children():
            widget.destroy()

        self.master.geometry("380x600")
        self.master.resizable(False, False)
        self.master.title("Menu")
        self.master.configure(background="black")

        self.background_image = PhotoImage(file = "resources/menu_background_new.png")
        self.label_background = Label(self.master, image = self.background_image)
        self.label_background.place(x=0, y=0)
        # Keep reference to avoid garbage collection
        self.label_background.image = self.background_image

        self.photo1 = PhotoImage(file = "resources/play_button.png")
        self.photo2 = PhotoImage(file = "resources/paleta.png")
        self.photo3 = PhotoImage(file = "resources/statistics.png")
        self.photo4 = PhotoImage(file = "resources/exit.png")

        self.label1 = Label(self.master, text="3D padajúce piškvorky",  font = "Courier 20 bold", justify="center", fg="white",bg = "black", activebackground = "black", width=23).place(x=10,y=10)
        
        self.button1 = Button(self.master, text="", image = self.photo1, command=self.OpenWin2, borderwidth=0, bg = "black", activebackground = "black")
        self.button1.place(x = 40, y = 50)
        
        self.button2 = Button(self.master, text="", image = self.photo2, command= self.OpenWin3, borderwidth=0, bg = "black", activebackground = "black")
        self.button2.place(x = 40, y = 185)
        
        self.button3 = Button(self.master, text="", image = self.photo3, command= self.OpenWin4, borderwidth=0, bg = "black", activebackground = "black")
        self.button3.place(x = 40, y = 320)
        
        self.button4 = Button(self.master, text="", image = self.photo4, command= self.Exit, borderwidth=0,bg = "black", activebackground = "black")
        self.button4.place(x = 40, y = 455)
        
    def OpenWin2(self):
        from src.view.help import Help
        self.myGUI = Help(self.master)

    def OpenWin3(self):
        from src.view.settings import ChoiceColor
        self.myGUI = ChoiceColor(self.master)

    def OpenWin4(self):
        from src.view.statistics import Statistics
        self.myGUI = Statistics(self.master)

    def Exit(self):
        self.master.destroy()
