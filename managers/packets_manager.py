import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class Packets:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn  
    
    def create_table(self):
        self.tableManager.create_table("packets",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL DEFAULT 0
        """)
    
    def add_packet(self, name, price):
        self.databaseManager.add("packets", name=name, price=price)
    
    def delete_packet(self, **kwargs):
        self.databaseManager.delete("packets", **kwargs)
        
    def get_packet(self, **kwargs):
        return self.databaseManager.get("packets", **kwargs)
    
    def get_all_packets(self):
        return self.databaseManager.get_all("packets")
    
    def update_packet(self, name, **kwargs):
        self.databaseManager.update("packets", name, **kwargs)
        
    def count_all_packets(self):
        return self.databaseManager.count_all("packets")
    
    def count_by_key(self, **kwargs):
        return self.databaseManager.count_by_key("packets", **kwargs)
