from tkinter import *
from src.model.types import Types

class GamePlan:
    def __init__(self, size, canvas):
        self.canvas = canvas
        self.size = size
        self.widthCanvas = int(self.canvas['width'])-6
        self.heightCanvas = int(self.canvas['height'])-4

        self.heightSpace = 21.25

        if self.size < 4:
            self.heightSpace += 50

        self.heightLayer = (self.heightCanvas - self.size*self.heightSpace)/self.size
        self.widthSquare = self.widthCanvas/self.size
        self.heightSquare = self.heightLayer/self.size         

    def draw_squares(self):
        # vykreslenie vodorovnych ciar
        for layer in range(self.size+1):
            for i in range(self.size+1):
                y = layer*self.heightLayer + (layer+1)*self.heightSpace + i*self.heightSquare
                x1 = self.convert_function(2,y)
                x2 = self.convert_function(self.widthCanvas,y)
                self.canvas.create_line(x1,y,x2,y, fill='magenta', width=4, capstyle=ROUND, joinstyle=ROUND)

        # vykreslenie zvislych ciar
        for layer in range(self.size+1):
            for i in range(self.size+1):
                y1 = (layer+1)*self.heightSpace + layer*self.heightLayer
                y2 = (layer+1)*(self.heightLayer+self.heightSpace)
                x1 = self.convert_function(i*self.widthSquare, y1)
                x2 = self.convert_function(i*self.widthSquare, y2)
                self.canvas.create_line(x1,y1,x2,y2, fill='magenta', width=4, capstyle=ROUND, joinstyle=ROUND)

    def draw_balls(self):
        balls = []

        if self.size == 3:
            self.image1 = PhotoImage(file = "resources/type"+str(Types.player1_type)+"_3.png")
            self.image2 = PhotoImage(file = "resources/type"+str(Types.player2_type)+"_3.png")
        elif self.size == 4:
            self.image1 = PhotoImage(file = "resources/type"+str(Types.player1_type)+"_2.png")
            self.image2 = PhotoImage(file = "resources/type"+str(Types.player2_type)+"_2.png")
        else:
            self.image1 = PhotoImage(file = "resources/type"+str(Types.player1_type)+"_1.png")
            self.image2 = PhotoImage(file = "resources/type"+str(Types.player2_type)+"_1.png")            
        
        # Keep refs
        self.canvas.image1_ref = self.image1
        self.canvas.image2_ref = self.image2

        for z in range(self.size):
            layer = []
            for y in range(self.size):
                row = []
                for x in range(self.size):
                    pair = []
                    position = self.calculate_position_ball(z, y, x)
                    
                    pair.append(self.canvas.create_image(position[0],position[1],image=self.image1, anchor="s", state =  HIDDEN))
                    pair.append(self.canvas.create_image(position[0],position[1],image=self.image2, anchor="s", state = HIDDEN))

                    row.append(pair)
                layer.append(row)
            balls.append(layer)

        return balls

    def calculate_position_square(self, x, y):
        x = self.reverse_convert_function(x,y)
        
        x_cord = x // self.widthSquare
        layer = y // (self.heightLayer + self.heightSpace)
        y_cord = y - layer*self.heightLayer - (layer+1)*self.heightSpace

        if y_cord < 0:
            y_cord = -1
            return (-1,-1,-1)
        else:
            y_cord = y_cord//self.heightSquare

        return (int(layer), int(y_cord), int(x_cord))

    def calculate_position_ball(self, layer, row, column):
        if row < 0 or column < 0 or layer < 0 or row >= self.size or column >= self.size or layer >= self.size:
            return

        y_start = (layer+1)* self.heightSpace + layer* self.heightLayer + row* self.heightSquare
        x_start = self.convert_function(column* self.widthSquare + self.widthSquare/2, y_start)

        return (x_start , y_start + 5*self.heightSquare/6)

    def convert_function(self,x,y):
        width = self.size * self.widthSquare
        y = y % (self.heightLayer + self.heightSpace)
        if y < 0.1:
            y += self.heightLayer + self.heightSpace
        y = y - self.heightLayer - self.heightSpace
        
        #miera splostenia
        b = -400
        tmp = width/2 - x
        tmp2 = b - y
        tmp3 = (tmp/b) * tmp2
        x = width/2 - tmp3

        return x

    def reverse_convert_function(self,x,y):
        width = self.size * self.widthSquare
        y = y % (self.heightLayer + self.heightSpace)
        if y < 0.1:
            y += self.heightLayer + self.heightSpace
        y = y - self.heightLayer - self.heightSpace

        b = -400
        tmp3 = width/2 - x
        tmp2 = b - y
        tmp = (tmp3/tmp2) * b
        x = width/2 - tmp

        return x
