import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class Attendance:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("attendance",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            lecture_id INTEGER,
            teacher_id INTEGER,
            attendance_date DATE DEFAULT CURRENT_DATE,
            status TEXT,
            FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
            FOREIGN KEY (lecture_id) REFERENCES lectures (id) ON DELETE CASCADE,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE
        """)
    
    def add_attendance(self, student_name, lecture_name, teacher_name, status):
        student_id = self.databaseManager.get_id_by_name("students", student_name)
        lecture_id = self.databaseManager.get_id_by_name("lectures", lecture_name)
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        self.databaseManager.add("attendance", student_id=student_id, lecture_id=lecture_id, teacher_id=teacher_id, status=status)
    
    def get_attendance_by_key(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        return self.databaseManager.get_all("attendance", **kwargs)
    
    def get_all_attendance(self):
        return self.databaseManager.get_all("attendance")
    
    def delete_attendance(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.delete("attendance", **kwargs)
    
    def update_attendance(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.update("attendance", **kwargs)
        
    def get_attendace_counts(self, **kwargs):
        status_dict = {"geldi": 0, "gelmedi": 0, "telafi": 0, "iptal": 0}
        kwargs = self.databaseManager.id_control(**kwargs)
        attendances = self.get_attendance_by_key(**kwargs)
        for attendance in attendances:
            status_dict[attendance[5]] += 1
        return status_dict
            
            
    
    