import database.connect_database as connect_database

class TableManager:
    def __init__(self, db_name):
        self.connectDatabase = connect_database.ConnectDatabase(db_name)
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()
        
    def delete_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(query)
        self.conn.commit()
        
        
        
        
        
        
        
        