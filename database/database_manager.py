import database.connect_database as connect_database

class DatabaseManager:
    def __init__(self, db_name):
        self.connectDatabase = connect_database.ConnectDatabase(db_name)
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn
        
    def get_id_by_name(self, table_name, name):
        query = f"SELECT id FROM {table_name} WHERE name = ?"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()[0]
    
    def get_name_by_id(self, table_name, id):
        query = f"SELECT name FROM {table_name} WHERE id = ?"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()[0]
        
    def clause_builder(self, **kwargs):
        where_clause = ' AND '.join([f"{key} = ?" for key in kwargs.keys()])
        values = tuple(value for value in kwargs.values())
        return where_clause, values

    def add(self, table_name, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?' for _ in kwargs])
        values = tuple(kwargs.values())
        
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def delete(self, table_name, **kwargs):
        where_clause, values = self.clause_builder(**kwargs)
        query = f"DELETE FROM {table_name} WHERE {where_clause}"
        print(query)
        print(values)
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def update(self, table_name, name, **kwargs):
        if 'name' in kwargs:
            del kwargs['name']
        set_clause = ', '.join([f"{key} = ?" for key in kwargs.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE name = ?"
        values = tuple(kwargs.values()) + (name,)
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def get(self, table_name, selections, **kwargs):
        where_clause, values = self.clause_builder(**kwargs)
        query = f"SELECT {selections} FROM {table_name} WHERE {where_clause}"
        self.cursor.execute(query, values)
        return self.cursor.fetchone()
    
    def get_all(self, table_name, **kwargs):
        if kwargs:  
            where_clause, values = self.clause_builder(**kwargs)
            query = f"SELECT * FROM {table_name} WHERE {where_clause}"
            self.cursor.execute(query, values)
        else:
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def count_all(self, table_name):
        query = f"SELECT COUNT(*) FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
    
    def count_by_key(self, table_name, **kwargs):
        where_clause, values = self.clause_builder(**kwargs)
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {where_clause}"
        self.cursor.execute(query, values)
        return self.cursor.fetchone()[0]
    
    def id_control(self, **kwargs):
        if "student_name" in kwargs:
            student_id = self.get_id_by_name("students", kwargs["student_name"])
            kwargs["student_id"] = student_id
            del kwargs["student_name"]
        if "lecture_name" in kwargs:
            lecture_id = self.get_id_by_name("lectures", kwargs["lecture_name"])
            kwargs["lecture_id"] = lecture_id
            del kwargs["lecture_name"]
        if "teacher_name" in kwargs:
            teacher_id = self.get_id_by_name("teachers", kwargs["teacher_name"])
            kwargs["teacher_id"] = teacher_id
            del kwargs["teacher_name"]
        if "packet_name" in kwargs:
            packet_id = self.get_id_by_name("packets", kwargs["packet_name"])
            kwargs["packet_id"] = packet_id
            del kwargs["packet_name"]
        return kwargs