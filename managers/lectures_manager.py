import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class Lectures:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("lectures",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        """)
    
    def add_lecture(self, name):
        self.databaseManager.add("lectures", name=name)
    
    def delete_lecture(self, **kwargs):
        self.databaseManager.delete("lectures", **kwargs)
        
    def get_lecture(self, **kwargs):
        return self.databaseManager.get("lectures", **kwargs)
    
    def get_all_lectures(self):
        return self.databaseManager.get_all("lectures")
    
    def update_lecture(self, name, **kwargs):
        self.databaseManager.update("lectures", name, **kwargs)
        
    def count_all_lectures(self):
        return self.databaseManager.count_all("lectures")
    
    def count_by_key(self, **kwargs):
        return self.databaseManager.count_by_key("lectures", **kwargs)