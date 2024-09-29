import sqlite3

class ConnectDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON;')

    def disconnect(self):
        self.conn.close()
        
        
