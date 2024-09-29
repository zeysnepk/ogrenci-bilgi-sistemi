import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class Teachers:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("teachers",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            address TEXT,
            registration_date DATETIME DEFAULT CURRENT_DATE
        """)
    
    def add_teacher(self, name, phone, address):
        self.databaseManager.add("teachers", name=name, phone=phone, address=address)
    
    def delete_teacher(self, **kwargs):
        self.databaseManager.delete("teachers", **kwargs)
        
    def get_teacher(self, **kwargs):
        return self.databaseManager.get("teachers", **kwargs)
    
    def get_all_teachers(self):
        return self.databaseManager.get_all("teachers")
    
    def update_teacher(self, name, **kwargs):
        self.databaseManager.update("teachers", name, **kwargs)
        
    def count_all_teachers(self):
        return self.databaseManager.count_all("teachers")
        
    def count_by_key(self, **kwargs):
        return self.databaseManager.count_by_key("teachers", **kwargs)
    