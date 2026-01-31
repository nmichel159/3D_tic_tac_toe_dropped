from tkinter import *
from src.model.types import Types

class ChoiceColor:
    def __init__(self,master):
        self.master = master
        for widget in self.master.winfo_children():
            widget.destroy()

        self.master.geometry("380x500")
        self.master.resizable(False, False)
        self.master.configure(background="black")

        self.background_image = PhotoImage(file = "resources/menu_background.png")
        self.label_background = Label(self.master, image = self.background_image)
        self.label_background.place(x=0, y=0)
        self.label_background.image = self.background_image

        self.label1 = Label(self.master, text = "Hráč 1",  font = "Courier 25 bold", bg = "black", fg = "yellow")
        self.label1.place(x = 50, y = 20)
        self.label2 = Label(self.master, text = "Hráč 2",  font = "Courier 25 bold", bg = "black", fg = "red")
        self.label2.place(x = 200, y = 20)
        
        self.image1 = PhotoImage(file = "resources/type1_5.png")
        self.image2 = PhotoImage(file = "resources/type2_5.png")
        self.image3 = PhotoImage(file = "resources/type3_5.png")
        self.image4 = PhotoImage(file = "resources/type4_5.png")
        self.image5 = PhotoImage(file = "resources/type5_5.png")
        self.image6 = PhotoImage(file = "resources/type6_5.png")

        self.canvas = Canvas(self.master, bg = "black",bd=0, highlightthickness=0, width = 230, height = 350)
        self.canvas.place(x = 75, y = 60)

        # Uložíme referencie na obrázky do zoznamu, aby ich garbage collector nezmazal
        self.images = [self.image1, self.image2, self.image3, self.image4, self.image5, self.image6]
        
        self.canvas.create_image(60,60,image=self.image1, anchor="center")
        self.canvas.create_image(170,60,image=self.image2, anchor="center")
        self.canvas.create_image(60,170,image=self.image3, anchor="center")
        self.canvas.create_image(170,170,image=self.image4, anchor="center")
        self.canvas.create_image(60,280,image=self.image5, anchor="center")
        self.canvas.create_image(170,280,image=self.image6, anchor="center")

        self.rectangle1 = self.canvas.create_rectangle(0,0,110,110,outline = "yellow", width=3, state = HIDDEN)
        self.rectangle2 = self.canvas.create_rectangle(0,0,110,110,outline = "red", width=3, state = HIDDEN)

        self.menu_button_image = PhotoImage(file = "resources/menu_button.png")
        self.menu_button = Button(self.master, bd = 0, bg = "black", activebackground = "black", image = self.menu_button_image, command = self.openMenu)
        self.menu_button.place(x = 120, y = 400)
        self.menu_button.image = self.menu_button_image

        self.player2 = True
        self.position1 = 0
        self.position2 = 0
       
        self.canvas.bind("<Button-1>", self.onClick)

    def openMenu(self):
        from src.view.menu import Menu
        self.myGUI = Menu(self.master)

    def onClick(self, event):
        x = event.x
        y = event.y
        row, column = 0,0

        if self.player2:
            self.player2 = False
        else:
            self.player2 = True
        
        row = y//110 + 1
        if 10 < x < 110:
            column = 1
        elif 120 < x < 220:
            column = 2
        elif 230 < x < 330:
            column = 3

        position = row*2 - (2-column)

        if row > 0 and column > 0:
            if self.player2 and self.position1 != position:
                self.canvas.itemconfig(self.rectangle2, state = NORMAL)
                self.canvas.coords(self.rectangle2, 10+(column-1)*110, 10+(row-1)*110, column*110, row*110)
                Types.Set2(position)
                self.position2 = position
            elif not self.player2 and self.position2 != position:
                self.canvas.itemconfig(self.rectangle1, state = NORMAL)
                self.canvas.coords(self.rectangle1, 10+(column-1)*110, 10+(row-1)*110, column*110, row*110)
                Types.Set1(position)
                self.position1 = position
