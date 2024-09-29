import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class Cash:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('cash.db')
        self.tableManager = table_manager.TableManager('cash.db')
        self.connectDatabase = connect_database.ConnectDatabase('cash.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("balance",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            balance REAL DEFAULT 0,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        """)
        
        self.tableManager.create_table("expenses",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            amount REAL DEFAULT 0,
            description TEXT,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        """)
        
        self.tableManager.create_table("incomes",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            amount REAL DEFAULT 0,
            description TEXT,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        """)
        
    def add_expense(self, title, amount, description):
        self.databaseManager.add("expenses", title=title, amount=amount, description=description)
        self.update_balance(-amount)
        
    def add_income(self, title, amount, description):
        self.databaseManager.add("incomes", title=title, amount=amount, description=description)
        self.update_balance(amount)
        
    def get_total_balance(self):
        self.cursor.execute("SELECT balance FROM balance WHERE id = 1")
        balance = self.cursor.fetchone()
        return balance[0] if balance else 0.0
    
    def get_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        expenses = self.cursor.fetchall()
        return expenses
    
    def get_incomes(self):
        self.cursor.execute("SELECT * FROM incomes")
        incomes = self.cursor.fetchall()
        return incomes
        
    def update_balance(self, amount):
        current_balance = self.get_total_balance()
        new_balance = current_balance + amount
        self.cursor.execute("UPDATE balance SET balance = ?", (new_balance,))
        self.conn.commit()
        
    def get_last_transactions(self, limit=5):
        transactions = self.cursor.execute("""
            SELECT amount, title, date FROM expenses
            UNION ALL
            SELECT amount, title, date FROM incomes
            ORDER BY date DESC LIMIT ?
        """, (limit,)).fetchall()
        return transactions
        
    
        
    