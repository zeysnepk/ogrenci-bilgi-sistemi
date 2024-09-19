import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import gui.main_gui as main_gui
from modules import login_backend
from modules import kayit_backend
from modules import yoklama_backend
from modules import odeme_backend
from modules import egitmen_backend
from modules import kasa_backend
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Öğrenci Yönetim Sistemi")
        self.setGeometry(100, 100, 1750, 1000)
        
        self.login = login_backend.Login()
        self.login.login_successful.connect(self.giris_setup)
        
        self.kayit = kayit_backend.Kayit()
        self.yoklama = yoklama_backend.Yoklama()
        self.odeme = odeme_backend.Odeme()
        self.egitmen = egitmen_backend.Egitmen()
        self.kasa = kasa_backend.Kasa()
        self.ui.action_kayit.setEnabled(False)
        self.ui.action_yoklama.setEnabled(False)
        self.ui.action_odeme.setEnabled(False)
        self.ui.action_egitmen.setEnabled(False)
        self.ui.action_kasa.setEnabled(False)
        
        self.stacked_widget_setup()
        
        self.ui.action_kayit.triggered.connect(lambda: self.show_widgets(self.kayit.kayit_widget, self.kayit.sayfa_yenile))
        self.ui.action_yoklama.triggered.connect(lambda: self.show_widgets(self.yoklama.yoklama_widget, self.yoklama.sayfa_yenile))
        self.ui.action_odeme.triggered.connect(lambda: self.show_widgets(self.odeme.odeme_widget, self.odeme.sayfa_yenile))
        self.ui.action_egitmen.triggered.connect(lambda: self.show_widgets(self.egitmen.egitmen_widget, self.egitmen.sayfa_yenile))
        self.ui.action_kasa.triggered.connect(lambda: self.show_widgets(self.kasa.kasa_widget, self.kasa.sayfa_yenile))
        self.ui.action_cikis.triggered.connect(self.cikis)
        self.ui.action_kapat.triggered.connect(self.kapat)
        

        for action in self.ui.toolBar.actions():
            if action.isSeparator():
                continue
            action.setCheckable(True)
        

        self.ui.toolBar.actionTriggered.connect(self.toggle_toolbar_action)
        
    def toggle_toolbar_action(self, triggered_action):
        for action in self.ui.toolBar.actions():
            if action.isSeparator():
                continue
            if action == triggered_action:
                action.setChecked(True)
            else:
                action.setChecked(False)
        
    def giris_setup(self, login_successful):
        if login_successful:
            self.ui.action_kayit.setEnabled(True)
            self.ui.action_yoklama.setEnabled(True)
            self.ui.action_odeme.setEnabled(True)
            self.ui.action_egitmen.setEnabled(True)
            self.ui.action_kasa.setEnabled(True)
            self.ui.action_anasayfa.setEnabled(False)
        
    def stacked_widget_setup(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)
        self.stacked_widget.addWidget(self.login.login_widget)
        self.stacked_widget.addWidget(self.kayit.kayit_widget)
        self.stacked_widget.addWidget(self.yoklama.yoklama_widget)
        self.stacked_widget.addWidget(self.odeme.odeme_widget)
        self.stacked_widget.addWidget(self.egitmen.egitmen_widget)
        self.stacked_widget.addWidget(self.kasa.kasa_widget)
        
    def show_widgets(self, widget, yenile):
        self.stacked_widget.setCurrentWidget(widget)
        yenile()
        
    def cikis(self):
        self.stacked_widget.setCurrentWidget(self.login.login_widget)
        self.login.login.line_kullanici.clear()
        self.login.login.line_sifre.clear()
        self.login.login.label_login_error.setText("")
        self.login.login.line_kullanici.setFocus()
        self.ui.action_kayit.setEnabled(False)
        self.ui.action_yoklama.setEnabled(False)
        self.ui.action_odeme.setEnabled(False)
        self.ui.action_egitmen.setEnabled(False)
        self.ui.action_kasa.setEnabled(False)
        
        for action in self.ui.toolBar.actions():
            if action.isSeparator():
                continue
            action.setChecked(False)
        
    def kapat(self):
        self.close()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.ui.toolBar.underMouse():
            for action in self.ui.toolBar.actions():
                if action.isSeparator():
                    continue
                action.setChecked(False)
        super().mousePressEvent(event)
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())