from services.registration_service import RegistrationService
from services.combo_service import ComboService
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
import gui.registration_view as registration

class RegistrationController(QWidget):
    def __init__(self):
        super().__init__()
        self.registrationService = RegistrationService()
        self.comboService = ComboService()
        self.registration = registration.Ui_Form()
        self.registration_widget = QWidget()
        self.registration.setupUi(self.registration_widget)
        
        self.lectures = []
        self.teachers = []
        self.packets = []
        self.hours = []
        self.amounts = []
        
        self.registration.combo_brans1.currentTextChanged.connect(self.show_teachers)
        self.registration.combo_brans1.currentTextChanged.connect(self.show_packets)
        
        self.registration.pushButton_devam.clicked.connect(self.get_lectures)
        self.registration.pushButton.clicked.connect(self.complete_registration)
        
        self.show_lectures()
        
    def clear_lecture(self):
        self.registration.combo_egt1.clear()
        self.registration.combo_paket.clear()
        self.registration.spinBox.setValue(0)
        self.registration.line_tutar.clear()
        
    def clear_all(self):
        self.registration.line_ad.clear()
        self.registration.line_soyad.clear()
        self.registration.line_tel.clear()
        self.registration.line_adres.clear()
        
    def show_lectures(self):
        lectures = self.comboService.get_lectures()
        for lecture in lectures:
            self.registration.combo_brans1.addItem(str(lecture[1]))
            
    def show_teachers(self):
        self.registration.combo_egt1.clear()
        lecture_name = self.registration.combo_brans1.currentText()
        teachers = self.comboService.get_teachers_by_lecture(str(lecture_name))
        print(teachers)
        for teacher in teachers:
            self.registration.combo_egt1.addItem(str(teacher))
            
    def show_packets(self):
        self.registration.combo_paket.clear()
        lecture_name = self.registration.combo_brans1.currentText()
        packets = self.comboService.get_packets_by_lecture(lecture_name)
        for packet in packets:
            self.registration.combo_paket.addItem(str(packet))
            
    def get_lectures(self):
        self.lectures.append(self.registration.combo_brans1.currentText())
        self.teachers.append(self.registration.combo_egt1.currentText())
        self.packets.append(self.registration.combo_paket.currentText())
        self.hours.append(self.registration.spinBox.value())
        self.amounts.append(self.registration.line_tutar.text())
        self.clear_lecture()
        
    def register_student(self):
        self.registrationService.register_student(self.name, self.surname, self.phone, self.address)
        
    def register_lecture(self, lecture, teacher, packet, hour, amount):
        if ',' in amount:
            amount = amount.replace(',', '.')
        amount = float(amount)
        name = self.name + " " + self.surname
        self.registrationService.students_lectures_registration(name, teacher, lecture, packet, hour, amount)
    
    def complete_registration(self):
        self.get_lectures()
        self.name = self.registration.line_ad.text()
        self.surname = self.registration.line_soyad.text()
        self.phone = self.registration.line_no.text()
        self.address = self.registration.text_adres.toPlainText()
        self.register_student()
        for lecture, teacher, packet, hour, amount in zip(self.lectures, self.teachers, self.packets, self.hours, self.amounts):
            self.register_lecture(lecture, teacher, packet, hour, amount)
        self.registration.label_registration_confirm.setText("Kayıt başarılı")
        self.registration.label_registration_confirm.setStyleSheet("color: green; font: 16pt \"Century Gothic\";")
        QTimer.singleShot(2000, lambda: self.registration.label_registration_confirm.setText(""))
        self.clear_all()      