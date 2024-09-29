from managers.students_manager import Students
from managers.teachers_manager import Teachers
from managers.lectures_manager import Lectures


class CountsService:
    def __init__(self):
        self.studentManager = Students()
        self.teacherManager = Teachers()
        self.lectureManager = Lectures()
        
    def all_counts(self):
        counts_dict = {}
        students_count = self.studentManager.count_all_students()
        teachers_count = self.teacherManager.count_all_teachers()
        lectures_count = self.lectureManager.count_all_lectures()
        counts_dict = {
            "ogrenci_sayisi": students_count,
            "egitmen_sayisi": teachers_count,
            "brans_sayisi": lectures_count
        }
        return counts_dict
        
        