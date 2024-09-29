from database import connect_database, database_manager
from database import table_manager
import bcrypt

class Admin:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("admin",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            password BLOB NOT NULL
        """)
        
    def add_admin(self, username, password):
        if not self.get_admin(username):
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            self.databaseManager.add("admin", name=username, password=hashed_password)
            return True
        else:
            return False
        
    def delete_admin(self, username):
        if self.get_admin(username):
            self.databaseManager.delete("admin", name=username)
            return True
        else:
            return False
        
    def get_admin(self, username):
        return self.databaseManager.get_all("admin", name=username)[0]
    
    def get_all_admins(self):
        return self.databaseManager.get_all("admin")
    
    def update_admin_password(self, username, password):
        if self.get_admin(username):    
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) 
            self.databaseManager.update("admin", name=username, password=hashed_password)
            return True
        else:
            return False
        
    def login(self, username, password):
        admin = self.get_admin(username)
        if admin and bcrypt.checkpw(password.encode('utf-8'), admin[2]):
            return True
        else:
            return False
        
        
        