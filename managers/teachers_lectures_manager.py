import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class TeachersLectures:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
    
    def create_table(self):
        self.tableManager.create_table("lecture_teachers",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lecture_id INTEGER,
            teacher_id INTEGER,
            FOREIGN KEY (lecture_id) REFERENCES lectures (id) ON DELETE CASCADE,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE
        """)
    
    def add_lecture_teacher(self, teacher_name, lectures):
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        print(lectures)
        for lecture in lectures:
            lecture_id = self.databaseManager.get_id_by_name("lectures", lecture)
            self.databaseManager.add("lecture_teachers", teacher_id=teacher_id, lecture_id=lecture_id)
    
    def delete_lecture_teacher(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.delete("lecture_teachers", **kwargs)
        
    def get_lectures_by_teacher(self, teacher_name):
        lecture_names = []
        teacher_id = self.databaseManager.get_id_by_name("teachers", teacher_name)
        lectures = self.databaseManager.get_all("lecture_teachers", teacher_id=teacher_id)
        for lecture in lectures:
            lecture_names.append(self.databaseManager.get_name_by_id("lectures", lecture[1]))
        return lecture_names
    
    def get_teachers_by_lecture(self, lecture_name):
        teacher_names = []
        lecture_id = self.databaseManager.get_id_by_name("lectures", lecture_name)
        teachers = self.databaseManager.get_all("lecture_teachers", lecture_id=lecture_id)
        for teacher in teachers:
            teacher_names.append(self.databaseManager.get_name_by_id("teachers", teacher[2]))
        return teacher_names
        
    def get_all_lecture_teachers(self):
        return self.databaseManager.get_all("lecture_teachers")
    
    
    

        