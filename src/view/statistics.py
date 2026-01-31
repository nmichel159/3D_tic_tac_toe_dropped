from tkinter import *
from src.model.score_service import ScoreService

class Statistics:
    def __init__(self,master):
        self.master = master
        for widget in self.master.winfo_children():
            widget.destroy()

        self.master.geometry("380x500")
        self.master.resizable(False, False)
        self.master.configure(background="black")

        self.scoreService = ScoreService()

        self.background_image = PhotoImage(file = "resources/menu_background.png")
        self.label_background = Label(self.master, image = self.background_image)
        self.label_background.place(x=0, y=0)
        self.label_background.image = self.background_image

        self.label1 = Label(self.master, text="Rebríček najlepších\nhráčov",  font = "Courier 20 bold", justify="center", fg="white",bg = "black", activebackground = "black", width=23).place(x=10,y=10)

        self.menu_button_image = PhotoImage(file = "resources/menu_button.png")
        self.button2 = Button(self.master, bd = 0, bg = "black", activebackground = "black", image = self.menu_button_image, command = self.openMenu)
        self.button2.place(x = 120, y = 420)
        self.button2.image = self.menu_button_image

        self.label_stats = Label(self.master, text=self.printStatistics(),  font = "Courier 14 bold", justify="left", fg="white",bg = "black", activebackground = "black", width=23).place(x=60,y=100)

    def openMenu(self):
        from src.view.menu import Menu
        self.myGUI = Menu(self.master)

    def printStatistics(self):
        players = self.scoreService.getTopScores(12)
        stringForLabel = ""
        order = 1

        for i in range(len(players)):
            if i > 0:
                if players[i-1][1] != players[i][1]:
                    order += 1
                stringForLabel += "{}.\t{}\t{}\n".format(order,players[i][0],players[i][1])
            else:
                stringForLabel += "{}.\t{}\t{}\n".format(order,players[i][0],players[i][1])

        return stringForLabel   

class WinnerPutInStatistics(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        self.geometry("380x425")
        self.resizable(False, False)
        self.title("Výhra")
        self.configure(background="black")

        self.background_image = PhotoImage(file = "resources/menu_background.png")
        self.label_background = Label(self, image = self.background_image)
        self.label_background.place(x=0, y=0)
        self.label_background.image = self.background_image

        self.photo1 = PhotoImage(file = "resources/ok_button.png")
        self.photo2 = PhotoImage(file = "resources/menu_button.png")

        Label(self, text="GRATULUJEME",  font = "Courier 30 bold", justify="center", fg="white",bg = "black", activebackground = "black", width=11).place(x=60,y=10)
        Label(self, text="Zadaj svoje meno\na budeš pridaný\ndo rebríčka\nnajlepších hráčov,\n\nalebo klikni na Menu.",  font = "Courier 15 bold", justify="center", fg="white",bg = "black", activebackground = "black", width=23).place(x=60,y=70)
        Label(self, text="max. 6 znakov, klikni OK",  font = "Courier 12 italic", justify="center", fg="white",bg = "black", activebackground = "black", width=26).place(x=55,y=240)

        self.btn_ok = Button(self, text="", image = self.photo1, command= self.entryHandler, borderwidth=0,bg = "black", activebackground = "black")
        self.btn_ok.place(x = 70, y = 330)
        self.btn_ok.image = self.photo1
        
        self.btn_menu = Button(self, text="", image = self.photo2, command= self.Menu, borderwidth=0,bg = "black", activebackground = "black")
        self.btn_menu.place(x = 190, y = 330)
        self.btn_menu.image = self.photo2

        self.entryName = StringVar()        
        self.entry = Entry(self, font = "Courier 25 bold", justify = "center", textvariable= self.entryName, width=14).place(x = 50, y = 270)

        self.scoreService = ScoreService()

    def entryHandler(self):
        inputString = self.entryName.get()

        if len(inputString) > 6 or len(inputString) < 1:
            self.entryName.set("")
        else:
            self.scoreService.addScore(inputString)
            self.entryName.set("")
            self.Menu()

    def Menu(self):
        from src.view.menu import Menu
        self.destroy()
        # Vrátime sa na hlavné menu v rámci rodičovského okna
        self.parent_menu = Menu(self.master)
