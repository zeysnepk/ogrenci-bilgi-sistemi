import database.database_manager as database_manager, database.table_manager as table_manager, database.connect_database as connect_database

class LecturesPackets:
    def __init__(self):
        self.databaseManager = database_manager.DatabaseManager('okul.db')
        self.tableManager = table_manager.TableManager('okul.db')
        self.connectDatabase = connect_database.ConnectDatabase('okul.db')
        self.connectDatabase.connect()
        self.cursor = self.connectDatabase.cursor
        self.conn = self.connectDatabase.conn

    def create_table(self):
        self.tableManager.create_table("lectures_packets",
        """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lecture_id INTEGER,
            packet_id INTEGER,
            FOREIGN KEY (lecture_id) REFERENCES lectures (id) ON DELETE CASCADE,
            FOREIGN KEY (packet_id) REFERENCES packets (id) ON DELETE CASCADE
        """)
    
    def add_lecture_packet(self, lecture_name, packet_name):
        lecture_id = self.databaseManager.get_id_by_name("lectures", lecture_name)
        packet_id = self.databaseManager.get_id_by_name("packets", packet_name)
        self.databaseManager.add("lectures_packets", lecture_id=lecture_id, packet_id=packet_id)
    
    def delete_lecture_packet(self, **kwargs):
        kwargs = self.databaseManager.id_control(**kwargs)
        self.databaseManager.delete("lectures_packets", **kwargs)
        
    def get_lectures_by_packet(self, packet_name):
        packet_id = self.databaseManager.get_id_by_name("packets", packet_name)
        return self.databaseManager.get_all("lectures_packets", packet_id=packet_id)
    
    def get_packets_by_lecture(self, lecture_name):
        packet_names = []
        lecture_id = self.databaseManager.get_id_by_name("lectures", lecture_name)
        packets = self.databaseManager.get_all("lectures_packets", lecture_id=lecture_id)
        for packet in packets:
            packet_names.append(self.databaseManager.get_name_by_id("packets", packet[2]))
        return packet_names
        