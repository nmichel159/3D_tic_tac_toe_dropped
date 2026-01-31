class GameLogic:
    def __init__(self, size):
        self.size = size
        # 0 - PLAYING, 1 - SOLVED, -1 - FAILED
        self.__state = 0
        self.__player2 = True  # Private attribute backing
        
        self.moves = []
        for z in range(self.size):
            layer = []
            for y in range(self.size):
                row = []
                for x in range(self.size):
                    row.append(0)
                layer.append(row)
            self.moves.append(layer)

    @property
    def player2(self):
        return self.__player2

    @player2.setter
    def player2(self, value):
        if value == 0 or value == 1 or value is True or value is False:
             self.__player2 = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, newState):
        if newState in [0, 1, -1]:
            self.__state = newState

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, newSize):
        if newSize > 2 and newSize < 6:
            self.__size = newSize
        else:
            self.__size = 4 # Default fallback

    def getMoveAtPosition(self,x,y,z):
        if x >= 0 and x < self.size and y >= 0 and y < self.size and z >= 0 and z < self.size:
            return self.moves[x][y][z]

    def setMoveAtPosition(self,x,y,z, value):
        if x >= 0 and x < self.size and y >= 0 and y < self.size and z >= 0 and z < self.size:
            if value == 0 or value == 1 or value == 2:
                self.moves[x][y][z] = value

    def checkSum(self):   
        vektory=[[0,0,1],[0,1,0],[1,0,0],
                 [0,1,1],[1,0,1],[1,1,0],
                 [0,1,-1],[1,0,-1],[1,-1,0],
                 [1,1,1],[-1,-1,1],[1,-1,-1],[-1,1,-1]]

        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    for vektor in vektory:
                        match = 0
                        xcord=vektor[0]
                        ycord=vektor[1]
                        zcord=vektor[2]
                        
                        if (self.size-1) < x+(self.size-1)*xcord or 0 > x+(self.size-1)*xcord:
                            continue
                        if (self.size-1) < y+(self.size-1)*ycord or 0 > y+(self.size-1)*ycord:
                            continue
                        if (self.size-1) < z+(self.size-1)*zcord or 0 > z+(self.size-1)*zcord:
                            continue
                        
                        for i in range((self.size-1)):
                            if self.moves[x][y][z]==self.moves[x+(i+1)*xcord][y+(i+1)*ycord][z+(i+1)*zcord] and self.moves[x][y][z]!=0:
                                match += 1
                        if match == (self.size-1):
                            return self.moves[x][y][z]

        GOver=-1
        for i in range(self.size):
            for o in range(self.size):
                if 0 in self.moves[i][o]:
                    GOver=0
        
        return GOver
