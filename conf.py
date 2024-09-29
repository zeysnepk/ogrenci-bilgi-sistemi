from managers import admin_manager, lectures_manager, packets_manager, student_payments_manager, students_manager, teacher_payments_manager, teachers_manager, lectures_packets_manager, cash_manager, teachers_lectures_manager, student_lectures_manager, admin_manager, lectures_manager, packets_manager, student_payments_manager, students_manager, teacher_payments_manager, teachers_manager, lectures_packets_manager, cash_manager, teachers_lectures_manager, student_lectures_manager, attendance_manager


class Config:
    def __init__(self):
        self.school_db_name = 'okul.db'
        self.cash_db_name = 'cash.db'
        self.admin_manager = admin_manager.Admin()
        self.lectures_manager = lectures_manager.Lectures()
        self.packets_manager = packets_manager.Packets()
        self.student_payments_manager = student_payments_manager.StudentPayments()
        self.students_manager = students_manager.Students()
        self.teacher_payments_manager = teacher_payments_manager.TeacherPayments()
        self.teachers_manager = teachers_manager.Teachers()
        self.cash_manager = cash_manager.Cash()
        self.lectures_packets_manager = lectures_packets_manager.LecturesPackets()
        self.teachers_lectures_manager = teachers_lectures_manager.TeachersLectures()
        self.student_lectures_manager = student_lectures_manager.StudentLectures()
        self.attendance_manager = attendance_manager.Attendance()
        
    def start_up(self):
        print("="*50)
        print("💼 Welcome to the Management System 💼".center(50))
        print("="*50)
        
        print("""
                ZZZZZZZ     K    K
                      Z     K   K 
                     Z      K  K  
                  ZZZZZ     KKK   
                   Z        K  K  
                  Z         K   K 
                ZZZZZZZ     K     K
""")


        print("="*70)
        
        print("""
📋 Choose an option:
        
1. 👤 Add Admin                -> Add a new admin to the system
2. 🔑 Change Admin Password    -> Update the password for an existing admin
3. 🗑️ Delete Admin            -> Remove an admin from the system
4. 📚 Add Lecture              -> Add a new lecture to the course list
5. 🗑️ Delete Lecture          -> Delete a lecture from the course list
6. 📦 Add Packet               -> Add a packet with various courses
7. 🗑️ Delete Packet           -> Delete a packet from the system
8.  Add Lecture Packet     -> Assign lectures to a packet
9. 🎓 Add Student              -> Enroll a student to the system
10. 🗑️ Delete Student         -> Delete a student from the system
11. 👨 Add Teacher           -> Register a new teacher
12. 🗑️ Delete Teacher       -> Delete a teacher from the system
13. 🧑 Add Teacher Lecture -> Assign lectures to a teacher
14. ❌ Exit                    -> Exit the system

        """)

        print("="*50)
        print("👨‍💻 Developed by zeysnepk".center(50))
        print("="*50)
        
        choice = input("Please enter your choice (1-14): ")
        config.choice_control(choice)
        
    def choice_control(self, choice):
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            self.add_admin(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            self.change_admin_password(username, password)
        elif choice == '3':
            username = input("Enter username: ")
            self.delete_admin(username)
        elif choice == '4':
            name = input("Enter lecture name: ")
            self.add_lecture(name)
        elif choice == '5':
            name = input("Enter lecture name: ")
            self.delete_lecture(name)
        elif choice == '6':
            name = input("Enter packet name: ")
            price = input("Enter packet price: ")
            self.add_packet(name, price)
        elif choice == '7':
            name = input("Enter packet name: ")
            self.delete_packet(name)
        elif choice == '8':
            lecture_name = input("Enter lecture name: ")
            packet_name = input("Enter packet name: ")
            self.add_lecture_packet(lecture_name, packet_name)
        elif choice == '9':
            name = input("Enter student name: ")
            phone = input("Enter student phone: ")
            address = input("Enter student address: ")
            self.add_student(name, phone, address)
        elif choice == '10':
            name = input("Enter student name: ")
            self.delete_student(name)
        elif choice == '11':
            name = input("Enter teacher name: ")
            phone = input("Enter teacher phone: ")
            address = input("Enter teacher address: ")
            self.add_teacher(name, phone, address)
        elif choice == '12':
            name = input("Enter teacher name: ")
            self.delete_teacher(name)
        elif choice == '13':
            teacher_name = input("Enter teacher name: ")
            lectures = input("Enter lectures (comma-separated): ").split(',')
            self.add_teacher_lecture(teacher_name, lectures)
        elif choice == '14':
            print("Exiting the system...")
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.start_up()
        
    def create_tables(self):
        self.admin_manager.create_table()
        self.lectures_manager.create_table()
        self.packets_manager.create_table()
        self.student_payments_manager.create_table()
        self.students_manager.create_table()
        self.teacher_payments_manager.create_table()
        self.teachers_manager.create_table()
        self.cash_manager.create_table()
        self.lectures_packets_manager.create_table()
        self.teachers_lectures_manager.create_table()
        self.student_lectures_manager.create_table()
        self.attendance_manager.create_table()
        
    def add_admin(self, username, password):
        if self.admin_manager.add_admin(username, password):
            print("Admin added")
        else:
            print("Admin already exists")
        
    def change_admin_password(self, username, password):
        if self.admin_manager.update_admin_password(username, password):
            print("Admin password updated")
        else:
            print("Admin not found")
            
    def delete_admin(self, username):
        if self.admin_manager.delete_admin(username):
            print("Admin deleted")
        else:
            print("Admin not found")
        
    def add_lecture(self, name):
        self.lectures_manager.add_lecture(name)
        
    def add_packet(self, name, price):
        self.packets_manager.add_packet(name, price)
        
    def add_lecture_packet(self, lecture_name, packet_name):
        self.lectures_packets_manager.add_lecture_packet(lecture_name, packet_name)
        
    def add_student(self, name, phone, address):
        self.students_manager.add_student(name, phone, address)
        
    def add_teacher(self, name, phone, address):
        self.teachers_manager.add_teacher(name, phone, address)
        
    def add_teacher_lecture(self, teacher_name, lectures):
        lectures = [lecture.strip() for lecture in lectures]
        self.teachers_lectures_manager.add_lecture_teacher(teacher_name, lectures)
        
    def delete_lecture(self, lecture_name):
        self.lectures_manager.delete_lecture(name=lecture_name)
        
    def delete_teacher(self, teacher_name):
        self.teachers_manager.delete_teacher(name=teacher_name)
        
    def delete_packet(self, packet_name):
        self.packets_manager.delete_packet(name=packet_name)
        
    def delete_student(self, student_name):
        self.students_manager.delete_student(name=student_name)
        
        
if __name__ == "__main__":
    config = Config()
    config.create_tables()
    config.start_up()