import sqlite3
import os

class ScoreService:
    def __init__(self):
        # Cesta k DB relatívne k main.py
        self.db_path = 'resources/score.db'
        self.command_insert = "INSERT INTO score VALUES (?,?)"
        self.command_select_list = "SELECT * FROM score ORDER BY points desc LIMIT ?"
        self.command_select_one = "SELECT points FROM score WHERE player = ?"
        self.command_delete = "DELETE FROM score"
        self.command_update = "UPDATE score SET points = ? WHERE player = ?"
        
        # Vytvorenie DB ak neexistuje (voliteľné)
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS score (player TEXT, points INTEGER)")
        conn.commit()
        conn.close()

    def getTopScores(self, number):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(self.command_select_list,(number,))
        scores = cursor.fetchall()
        connection.close()
        return scores

    def reset(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(self.command_delete)
        connection.commit()
        connection.close()

    def addScore(self, player):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute(self.command_select_one,(player,))
        points = cursor.fetchone()

        if points == None:
            cursor.execute(self.command_insert,(player, 1))
        else:
            cursor.execute(self.command_update,(points[0]+1, player))
        connection.commit()
        connection.close()
