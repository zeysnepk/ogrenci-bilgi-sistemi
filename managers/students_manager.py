import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class Students:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("students",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            address TEXT,
            registration_date DATETIME DEFAULT CURRENT_DATE
        """)
        
    def add_student(self, name, phone, address):
        self.databaseManager.add("students", name=name, phone=phone, address=address)
        
    def delete_student(self, **kwargs):
        self.databaseManager.delete("students", **kwargs)
        
    def get_student(self, **kwargs):
        return self.databaseManager.get_all("students", **kwargs)
    
    def get_all_students(self):
        return self.databaseManager.get_all("students")
    
    def update_student(self, name, **kwargs):
        self.databaseManager.update("students", name, **kwargs)
        
    def count_all_students(self):
        return self.databaseManager.count_all("students")
    
    def count_by_key(self, **kwargs):
        return self.databaseManager.count_by_key("students", **kwargs)
        
    