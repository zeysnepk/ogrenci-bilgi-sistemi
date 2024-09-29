import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class StudentLectures:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def create_table(self):
        self.tableManager.create_table("student_lectures",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            lecture_id INTEGER,
            teacher_id INTEGER,
            packet_id INTEGER,
            total_hours INTEGER DEFAULT 0,
            remaining_hours INTEGER DEFAULT 0,
            elapsed_hours INTEGER DEFAULT 0,
            elapsed BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,
            FOREIGN KEY (lecture_id) REFERENCES lectures (id) ON DELETE CASCADE,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE,
            FOREIGN KEY (packet_id) REFERENCES packets (id) ON DELETE CASCADE
        """)
    
    def add_student_lecture(self, student_name, lecture_name, teacher_name, packet_name, hours):
        student_id = self.databaseManager.get_id_by_name("students", student_name)
        lecture_id = self.databaseManager.get_id_by_name("lectures", lecture_name)
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        packet_id = self.databaseManager.get_id_by_name("packets", packet_name)
        self.databaseManager.add("student_lectures", student_id=student_id, lecture_id=lecture_id, teacher_id=teacher_id, packet_id=packet_id, total_hours=hours, remaining_hours=hours)
    
    def delete_student_lecture(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.delete("student_lectures", **kwargs)
        
    def get_lectures_by_student(self, student_name):
        student_id = self.databaseManager.get_id_by_name("students", student_name)
        return self.databaseManager.get_all("student_lectures", student_id=student_id)
    
    def get_students_by_key(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        return self.databaseManager.get_all("student_lectures", **kwargs)
    
    def get_all_student_lectures(self):
        return self.databaseManager.get_all("student_lectures")
    
    def update_student_lecture(self, student_name, lecture_name, teacher_name, hours):
        student_id = self.databaseManager.get_id_by_name("students", student_name)
        lecture_id = self.databaseManager.get_id_by_name("lectures", lecture_name)
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        selections = "remaining_hours, elapsed_hours"
        student_lectures = self.databaseManager.get("student_lectures", selections, student_id=student_id, lecture_id=lecture_id, teacher_id=teacher_id)
        remaining_hours = student_lectures[0] - hours
        elapsed_hours = student_lectures[1] + hours
        if remaining_hours == 0:
            self.databaseManager.update("student_lectures", student_id=student_id, lecture_id=lecture_id,
                teacher_id=teacher_id, remaining_hours=remaining_hours, elapsed_hours=elapsed_hours, elapsed=True)
        else:
            self.databaseManager.update("student_lectures", student_id=student_id, lecture_id=lecture_id, 
                teacher_id=teacher_id, remaining_hours=remaining_hours, elapsed_hours=elapsed_hours)
        
        
