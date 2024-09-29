from managers.student_lectures_manager import StudentLectures
from managers.student_payments_manager import StudentPayments
from managers.teacher_payments_manager import TeacherPayments
from managers.students_manager import Students

class RegistrationService:
    def __init__(self):
        self.studentLecturesManager = StudentLectures()
        self.studentPaymentsManager = StudentPayments()
        self.teacherPaymentsManager = TeacherPayments()
        self.studentManager = Students()
    def register_student(self, name, surname, phone, address):
        name = name + " " + surname
        if self.studentManager.get_student(name=name, phone=phone, address=address):
            return "Öğrenci zaten mevcut"
        else:
            self.studentManager.add_student(name, phone, address)
            return "Öğrenci başarıyla eklendi"
        
    def students_lectures_registration(self, student_name, teachers_name, lecture_name, packet_name, hours, amount):
        self.studentLecturesManager.add_student_lecture(student_name, lecture_name, teachers_name, packet_name, hours)
        self.studentPaymentsManager.add_student_payment(student_name, lecture_name, teachers_name, packet_name, amount)
        self.teacherPaymentsManager.add_teacher_payment(teachers_name, amount)
        
        
