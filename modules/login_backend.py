from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from core.admin import Admin
import gui.login as login
from core.database import Database

class Login(QWidget):
    login_successful = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        try:
            self.admin = Admin()
            self.login = login.Ui_Form()
            self.login_widget = QWidget()
            self.login.setupUi(self.login_widget)
            
            self.db = Database()
            self.toplamSayilar = self.db.toplamSayilar()
            self.login.label_ogr_sayi.setText(str(self.toplamSayilar['ogrenci_sayisi']))
            self.login.label_egt_sayi.setText(str(self.toplamSayilar['egitmen_sayisi']))
            self.login.label_brans_sayi.setText(str(self.toplamSayilar['brans_sayisi']))
            
            self.login.button_giris.clicked.connect(self.giris_yap)
        except Exception as e:
            print(f"Login Class hata: {e}")
        
    def giris_yap(self):
        try:
            kullanici = self.login.line_kullanici.text()
            sifre = self.login.line_sifre.text()
            if kullanici == "" or sifre == "":
                self.login.label_login_error.setText("Kullanıcı adı veya şifre boş bırakılamaz")
                self.login.label_login_error.setStyleSheet("color: red; font: 14pt \"Century Gothic\";")
            elif self.admin.adminDogrula(kullanici, sifre):
                self.login.label_login_error.setText("Giriş başarılı menüden işlemlerinizi gerçekleştirebilirsiniz")
                self.login.label_login_error.setStyleSheet("color: green; font: 14pt \"Century Gothic\";")
                self.login_successful.emit(True)
            else:
                self.login.label_login_error.setText("Kullanıcı adı veya şifre hatalı")
                self.login.label_login_error.setStyleSheet("color: red; font: 14pt \"Century Gothic\";")
                self.login.line_kullanici.clear()
                self.login.line_sifre.clear()
                self.login_successful.emit(False)
        except Exception as e:
            print(f"giris_yap hata: {e}")
        
        
