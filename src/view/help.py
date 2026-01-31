from tkinter import *

class Help:
    def __init__(self,master):
        self.master = master
        for widget in self.master.winfo_children():
            widget.destroy()

        self.master.geometry("500x600")
        self.master.resizable(False, False)
        self.master.configure(background="black")

        self.background_image = PhotoImage(file = "resources/help_background.png")
        self.label_background = Label(self.master, image = self.background_image)
        self.label_background.place(x=0, y=0)
        self.label_background.image = self.background_image

        self.rules = self.readData()
        self.label2 = Label(self.master, text=self.rules,  font = "Courier 12", justify="center", fg="white",bg = "black", width=41, wraplength=420, anchor = "nw").place(x=45,y=5)

        self.play_image = PhotoImage(file = "resources/play_button.png")
        self.button1 = Button(self.master, text="", image = self.play_image, command=self.openGame, borderwidth=0, bg = "black", activebackground = "black")
        self.button1.place(x = 100, y = 280)
        self.button1.image = self.play_image

        self.load_image = PhotoImage(file = "resources/load_button.png")
        self.button3 = Button(self.master, text="", image = self.load_image, command=self.openGameFromFile, borderwidth=0, bg = "black", activebackground = "black")
        self.button3.place(x = 100, y = 401)
        self.button3.image = self.load_image

        self.menu_image = PhotoImage(file = "resources/menu_button.png")
        self.button2 = Button(self.master, bd = 0, bg = "black", activebackground = "black", image = self.menu_image, command = self.openMenu)
        self.button2.place(x = 180, y = 525)
        self.button2.image = self.menu_image

        self.choiceSize = IntVar(self.master, '4')

        valuesForRadioButtons = {'3x3x3' : 3,
                                 '4x4x4' : 4,
                                 '5x5x5' : 5}

        for(text, value) in valuesForRadioButtons.items():
            Radiobutton(self.master, text = text, variable = self.choiceSize, value = value, indicator = 0, background = 'black', selectcolor = 'gold', activebackground = 'black',borderwidth = 5, relief = SUNKEN,
                        foreground = 'white', activeforeground = 'white', font = 'Courier 20 bold').place(x = 80 + (value-3)*130, y = 220)

    def readData(self):
        try:
            with open("resources/rules.txt","r",encoding = "utf-8") as file:
                text = file.read()
            return text
        except FileNotFoundError:
            return "Pravidlá sa nenašli."

    def openGame(self):
        from src.view.game_graphics import GameGraphics
        self.myGUI = GameGraphics(self.master, self.choiceSize.get(), 0)

    def openGameFromFile(self):
        from src.view.game_graphics import GameGraphics
        self.myGUI = GameGraphics(self.master, self.choiceSize.get(), 1)

    def openMenu(self):
        from src.view.menu import Menu
        self.myGUI = Menu(self.master)
