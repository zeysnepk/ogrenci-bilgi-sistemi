from services.login_service import LoginService
from services.counts_service import CountsService
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
import gui.login_view as login

class LoginController(QWidget):
    login_successful = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()
        self.loginService = LoginService()
        self.countsService = CountsService()
        
        self.login = login.Ui_Form()
        self.login_widget = QWidget()
        self.login.setupUi(self.login_widget)
        
        self.get_total_counts()
        
        self.login.button_giris.clicked.connect(self.login_app)
        
    def get_total_counts(self):
        total_counts = self.countsService.all_counts()
        self.login.label_ogr_sayi.setText(str(total_counts['ogrenci_sayisi']))
        self.login.label_egt_sayi.setText(str(total_counts['egitmen_sayisi']))
        self.login.label_brans_sayi.setText(str(total_counts['brans_sayisi']))
        
    def login_app(self):
        kullanici = self.login.line_kullanici.text()
        sifre = self.login.line_sifre.text()
        if kullanici == "" or sifre == "":
            self.login.label_login_error.setText("Kullanıcı adı veya şifre boş bırakılamaz")
            self.login.label_login_error.setStyleSheet("color: red; font: 14pt \"Century Gothic\";")
        else:
            if self.loginService.login(kullanici, sifre):
                self.login.label_login_error.setText("Giriş başarılı menüden işlemlerinizi gerçekleştirebilirsiniz")
                self.login.label_login_error.setStyleSheet("color: green; font: 14pt \"Century Gothic\";")
                self.login_successful.emit(True)
            else:
                self.login.label_login_error.setText("Kullanıcı adı veya şifre hatalı")
                self.login.label_login_error.setStyleSheet("color: red; font: 14pt \"Century Gothic\";")
                self.login.line_kullanici.clear()
                self.login.line_sifre.clear()
                self.login_successful.emit(False)