import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class TeacherPayments:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("teacher_payments",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            amount REAL DEFAULT 0,
            paid BOOLEAN DEFAULT FALSE,
            paid_amount REAL DEFAULT 0,
            remaining_amount REAL DEFAULT 0,
            last_payment_date DATETIME DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
            payment_date DATETIME DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
            FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE
        """)
        
    def add_teacher_payment(self, teacher_name, amount):
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        self.databaseManager.add("teacher_payments", teacher_id=teacher_id, amount=amount,
            payment_date=f"(strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))")
    
    def get_teacher_payments_by_key(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        return self.databaseManager.get_all("teacher_payments", **kwargs)
    
    def total_payments(self, teacher_name):
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        payments = self.get_teacher_payments_by_key(teacher_id=teacher_id)
        total = 0
        for payment in payments:
            total += payment[6]
        return total
    
    def all_teacher_payments(self):
        return self.databaseManager.get_all("teacher_payments")
    
    def pay_teacher_payment(self, teacher_name, amount):
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        selections = "paid_amount, remaining_amount"
        payments = self.databaseManager.get("teacher_payments", selections, teacher_id=teacher_id)
        paid_amount = payments[0] + amount
        remaining_amount = payments[1] - amount
        if remaining_amount == 0:
            self.update_teacher_payment(teacher_id=teacher_id, paid_amount=paid_amount,
                remaining_amount=remaining_amount, paid=True,
                last_payment_date=f"(strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))")
        else:
            self.update_teacher_payment(teacher_id=teacher_id, paid_amount=paid_amount,
                remaining_amount=remaining_amount)
    
    def delete_teacher_payment(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.delete("teacher_payments", **kwargs)
    
    def update_teacher_payment(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.update("teacher_payments", **kwargs)
    
    
    