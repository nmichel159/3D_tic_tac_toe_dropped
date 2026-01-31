from tkinter import *
from src.model.game_logic import GameLogic
from src.controller.persistence import GamePickleController
from src.view.game_plan import GamePlan
from src.view.statistics import WinnerPutInStatistics

class GameGraphics:        
    def __init__(self, master,size,fromFile):
        self.master = master
        for widget in self.master.winfo_children():
            widget.destroy()

        self.master.geometry("571x800")
        self.master.resizable(False, False)
        self.master.configure(background="black")

        self.background_image = PhotoImage(file = "resources/background.png")
        self.label_background = Label(self.master, image = self.background_image)
        self.label_background.place(x=0, y=0)
        self.label_background.image = self.background_image

        self.size = size
        self.fromFile = fromFile

        self.pickleController = GamePickleController()

        self.logic = None

        if self.fromFile == 1:
            self.logic = self.pickleController.load()
            if self.logic != None:
                self.size = self.logic.size

        ## CANVAS
        self.canvas = Canvas(self.master, bg = "black",bd=0, highlightthickness=0, relief='ridge', width=375, height=609)
        self.canvas.place(x = 100, y = 100)

        ## CANVAS FOR RECTANGLES OF PLAYERS
        self.canvas2 = Canvas(self.master, bg = "black",bd=0, highlightthickness=0, height = 95, width = int(self.canvas["width"]))
        self.canvas2.place(x = 100, y = 5)
        
        ## PLAYER LABELS
        self.font = "Courier 25"
        self.font_bold = "Courier 25 bold"

        self.image0 = PhotoImage(file = "resources/player_background.png")
        self.player_rect1 = self.canvas2.create_image(0,5,image=self.image0, anchor="nw", state = NORMAL)
        self.player_rect2 = self.canvas2.create_image(210,5,image=self.image0, anchor="nw", state = HIDDEN)
        self.canvas2.image0 = self.image0

        self.label1 = Label(self.master, text = "Hráč 1",  font = self.font_bold, bg = "black", fg = "#00FF00")
        self.label1.place(x = 120, y = 30)
        self.label2 = Label(self.master, text = "Hráč 2",  font = self.font, bg = "black", fg = "white")
        self.label2.place(x = 330, y = 30)

        ## BUTTONS
        self.menu_button_image = PhotoImage(file = "resources/menu_button.png")
        self.exit_button_image = PhotoImage(file = "resources/exit_button.png")
        self.save_button_image = PhotoImage(file = "resources/save_button.png")
        
        self.menu_button = Button(self.master, bd = 0, bg = "black", activebackground = "black", image = self.menu_button_image, command = self.openMenu)
        self.menu_button.place(x = 50, y = 718)
        self.menu_button.image = self.menu_button_image
        
        self.exit_button = Button(self.master, bd = 0, bg = "black", activebackground = "black", image = self.exit_button_image, command = self.quitGame)
        self.exit_button.place(x = 350, y = 718)
        self.exit_button.image = self.exit_button_image
        
        self.save_button = Button(self.master, bd = 0, bg = "black", activebackground = "black", image = self.save_button_image, command = self.saveGame)
        self.save_button.place(x = 200, y = 718)
        self.save_button.image = self.save_button_image

        ## vygenerovanie hracieho planu
        self.gamePlan = GamePlan(self.size, self.canvas)
        self.gamePlan.draw_squares()

        ## zaplnenie pola - LOPTICKY hracov
        self.balls = self.gamePlan.draw_balls()

        self.canvas.bind("<Button-1>", self.onClick)

        ## bool premenna, kym pada dole lopticka, nemoze nikto klikat
        self.is_falling = False

        if self.logic != None:
            self.prepareGameForSavedGame()
        if self.logic == None:
            self.logic = GameLogic(self.size)


    def saveGame(self):
        if self.logic.state == 0:
            self.pickleController.save(self.logic)

    def prepareGameForSavedGame(self):
        for layer in range(self.size):
            for row in range(self.size):
                for x in range(self.size):
                    if self.logic.getMoveAtPosition(layer,row,x) == 1:
                        self.canvas.itemconfig(self.balls[layer][row][x][0], state = NORMAL)
                    elif self.logic.getMoveAtPosition(layer,row,x) == 2:
                        self.canvas.itemconfig(self.balls[layer][row][x][1], state = NORMAL)

        if self.logic.player2:
            self.label1.configure(foreground = "#00FF00")
            self.label1.configure(font = self.font_bold)
            self.canvas2.itemconfig(self.player_rect1, state = NORMAL)
                        
            self.label2.configure(foreground = "white")
            self.label2.configure(font = self.font)
            self.canvas2.itemconfig(self.player_rect2, state = HIDDEN)
        else:
            self.label2.configure(foreground = "#00FF00")
            self.label2.configure(font = self.font_bold)
            self.canvas2.itemconfig(self.player_rect2, state = NORMAL)
                        
            self.label1.configure(foreground = "white")
            self.label1.configure(font = self.font)
            self.canvas2.itemconfig(self.player_rect1, state = HIDDEN)     

    def gameOver(self):
        self.canvas.after(100)
        self.canvas.unbind('<1>')
        self.canvas.delete("all")
        
        self.canvas2.delete("all")
        self.label1.destroy()
        self.label2.destroy()
        self.canvas2.create_text(185.5,50, text = "KONIEC HRY", font = self.font_bold, fill="red")

        self.image_go = PhotoImage(file = "resources/game_over.png")
        self.canvas.create_image(0,0,image=self.image_go, anchor="nw")
        self.canvas.image_go = self.image_go

    def congratulation(self, number):
        self.canvas.after(100)
        self.canvas.unbind('<1>')
        self.canvas.delete("all")
        
        self.canvas2.delete("all")
        self.label1.destroy()
        self.label2.destroy()
        self.canvas2.create_text(185.5,50, text = "KONIEC HRY", font = self.font_bold, fill="red")

        if number == 1:    
            self.image_cong = PhotoImage(file = "resources/congratulation_1.png")
        else:
            self.image_cong = PhotoImage(file = "resources/congratulation_2.png")
        
        self.canvas.create_image(0,0,image=self.image_cong, anchor="nw")
        self.canvas.image_cong = self.image_cong

        WinnerPutInStatistics(self.master)

    def onClick(self, event):
        if not self.is_falling:
            layer,row,column = self.gamePlan.calculate_position_square(event.x, event.y)
              
            if layer > -1 and self.logic.getMoveAtPosition(layer,row,column) == 0:
                    if self.logic.player2:
                        self.logic.player2 = False
                    else:
                        self.logic.player2 = True

                    self.canvas.itemconfig(self.balls[layer][row][column][self.logic.player2], state = NORMAL)
                    if self.logic.player2:
                        self.logic.setMoveAtPosition(layer,row,column,2)
                    else:
                        self.logic.setMoveAtPosition(layer,row,column,1)
                    self.canvas.update()
                    self.canvas.after(500)
                    self.moveDown(layer, row, column, self.logic.player2)
                    if self.logic.player2:
                        self.label1.configure(foreground = "#00FF00")
                        self.label1.configure(font = self.font_bold)
                        self.canvas2.itemconfig(self.player_rect1, state = NORMAL)
                        
                        self.label2.configure(foreground = "white")
                        self.label2.configure(font = self.font)
                        self.canvas2.itemconfig(self.player_rect2, state = HIDDEN)
                    else:
                        self.label2.configure(foreground = "#00FF00")
                        self.label2.configure(font = self.font_bold)
                        self.canvas2.itemconfig(self.player_rect2, state = NORMAL)
                        
                        self.label1.configure(foreground = "white")
                        self.label1.configure(font = self.font)
                        self.canvas2.itemconfig(self.player_rect1, state = HIDDEN)

            nextState = self.logic.checkSum()

            if nextState == -1:
                self.logic.state = -1
                self.gameOver()
            elif nextState > 0:
                self.logic.state = 1
                self.congratulation(nextState)

    def moveDown(self,layer, y, x, player):
        self.is_falling = True
        while layer < self.size - 1:
            if self.logic.getMoveAtPosition(layer+1,y,x) == 0:
                self.logic.setMoveAtPosition(layer+1,y,x, self.logic.getMoveAtPosition(layer,y,x))
                self.logic.setMoveAtPosition(layer,y,x,0)
                self.canvas.itemconfig(self.balls[layer][y][x][player], state = HIDDEN)
                self.canvas.itemconfig(self.balls[layer+1][y][x][player], state = NORMAL)
                self.canvas.update()
                self.canvas.after(500)
                layer = layer + 1
            else:
                self.is_falling = False
                return
        self.is_falling = False

    def openMenu(self):
        from src.view.menu import Menu
        self.myGUI = Menu(self.master)

    def quitGame(self):
        self.master.destroy()
