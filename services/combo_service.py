from managers import lectures_manager, teachers_lectures_manager, lectures_packets_manager

class ComboService:
    def __init__(self):
        self.lecturesManager = lectures_manager.Lectures()
        self.teachersLecturesManager = teachers_lectures_manager.TeachersLectures()
        self.lecturesPacketsManager = lectures_packets_manager.LecturesPackets()
        
    def get_lectures(self):
        return self.lecturesManager.get_all_lectures()
    
    def get_teachers_by_lecture(self, lecture_name):
        return self.teachersLecturesManager.get_teachers_by_lecture(lecture_name)
    
    def get_packets_by_lecture(self, lecture_name):
        return self.lecturesPacketsManager.get_packets_by_lecture(lecture_name)