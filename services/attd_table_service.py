from managers.attendance_manager import Attendance
from managers.student_lectures_manager import StudentLectures

class AttdTableService:
    def __init__(self):
        self.attendanceManager = Attendance()
        self.studentLecturesManager = StudentLectures()
        
    def get_attendance_table(self, **kwargs):
        if self.attendanceManager.get_attendance_by_key(**kwargs):
            return self.attendanceManager.get_attendance_by_key(**kwargs)
        else:
            return self.studentLecturesManager.get_students_by_key(**kwargs)
        
    def add_attendance(self, student_name, lecture_name, teacher_name, status):
        self.attendanceManager.add_attendance(student_name=student_name, lecture_name=lecture_name, teacher_name=teacher_name, status=status)
        
    def update_attendance(self, student_name, lecture_name, teacher_name, status, attendance_date):
        self.attendanceManager.update_attendance(student_name=student_name, lecture_name=lecture_name, teacher_name=teacher_name, status=status, attendance_date=attendance_date)
        
    def get_attendance_all_counts(self, lecture_name, teacher_name, student_name):
        return self.attendanceManager.get_attendace_counts(lecture_name=lecture_name, teacher_name=teacher_name, student_name=student_name)