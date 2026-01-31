import pickle
import os

class GamePickleController:
    def __init__(self):
        self.fileName = 'resources/game.pickle'

    def load(self):
        try:
            with open(self.fileName,'r+b') as file:
                obj = pickle.load(file)
                file.truncate(0)
                return obj
        except:
            return None

    def save(self, obj):
        with open(self.fileName, 'wb') as file:
            pickle.dump(obj, file)
