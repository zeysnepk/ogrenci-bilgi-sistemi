import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database
from datetime import datetime
class StudentPayments:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("student_payments",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            teacher_id INTEGER,
            lecture_id INTEGER,
            packet_id INTEGER,
            amount REAL DEFAULT 0,
            paid BOOLEAN DEFAULT FALSE,
            paid_amount REAL DEFAULT 0,
            remaining_amount REAL DEFAULT 0,
            last_payment_amount REAL DEFAULT 0,
            last_payment_date DATETIME DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
            payment_date DATETIME DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
            FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE,
            FOREIGN KEY (lecture_id) REFERENCES lectures (id) ON DELETE CASCADE,
            FOREIGN KEY (packet_id) REFERENCES packets (id) ON DELETE CASCADE
        """)
    
    def add_student_payment(self, student_name, teacher_name, lecture_name, packet_name, amount):
        student_id = self.databaseManager.get_id_by_name("students", student_name)
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        lecture_id = self.databaseManager.get_id_by_name("lectures", lecture_name)
        packet_id = self.databaseManager.get_id_by_name("packets", packet_name)
        self.databaseManager.add("student_payments", student_id=student_id,
            teacher_id=teacher_id, lecture_id=lecture_id, packet_id=packet_id, amount=amount,
            payment_date=f"(strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))")
        
    def get_student_payments_by_key(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        return self.databaseManager.get_all("student_payments", **kwargs)
    
    def total_payments(self, student_name):
        student_id = self.databaseManager.get_id_by_name("students", student_name)
        payments = self.get_student_payments_by_key(student_id=student_id)
        total = 0
        for payment in payments:
            total += payment[6]
        return total
    
    def all_student_payments(self):
        return self.databaseManager.get_all("student_payments")
    
    def delete_student_payment(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.delete("student_payments", **kwargs)
        
    def update_student_payment(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.update("student_payments", **kwargs)
        
    def pay_student_payment(self, student_name, amount):
        student_id = self.databaseManager.get_id_by_name("students", student_name)
        selections = "paid_amount, remaining_amount"
        payments = self.databaseManager.get("student_payments", selections, student_id=student_id)
        paid_amount = payments[0] + amount
        remaining_amount = payments[1] - amount
        remaining_amount = max(0, remaining_amount)
        if remaining_amount != 0:
            self.update_student_payment(student_id=student_id, paid_amount=paid_amount,
                remaining_amount=remaining_amount, last_payment_amount=amount,
                last_payment_date=f"(strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))")
    
    
    
    
        
        