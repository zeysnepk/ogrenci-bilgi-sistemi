import sys
from controller import login_controller, registration_controller#, payment_controller, attendance_controller, teacher_controller, cash_box_controller
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
import gui.main_gui_view as main_gui_view


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_gui_view.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Okul Yönetim Sistemi")
        self.setGeometry(100, 100, 1750, 1000)
        
        self.login = login_controller.LoginController()
        self.register = registration_controller.RegistrationController()
        
        self.stacked_widget_setup()
        self.is_enable(False)
        self.login.login_successful.connect(self.is_enable)
        
        self.ui.action_kayit.triggered.connect(lambda: self.show_widgets(self.register.registration_widget))
        self.ui.action_cikis.triggered.connect(self.logout)
        self.ui.action_kapat.triggered.connect(self.exit)

        
    def stacked_widget_setup(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)
        self.stacked_widget.addWidget(self.login.login_widget)
        self.stacked_widget.addWidget(self.register.registration_widget)
        
    def show_widgets(self, widget):
        self.stacked_widget.setCurrentWidget(widget)
        
    def is_enable(self, key):
        self.ui.action_kayit.setEnabled(key)
        self.ui.action_yoklama.setEnabled(key)
        self.ui.action_odeme.setEnabled(key)
        self.ui.action_egitmen.setEnabled(key)
        self.ui.action_kasa.setEnabled(key)
        self.ui.action_cikis.setEnabled(key)
        self.ui.action_kapat.setEnabled(key)
        
    def toggle_toolbar_action(self, triggered_action):
        for action in self.ui.toolBar.actions():
            if action.isSeparator():
                continue
            if action == triggered_action:
                action.setChecked(True)
            else:
                action.setChecked(False)
                
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.ui.toolBar.underMouse():
            for action in self.ui.toolBar.actions():
                if action.isSeparator():
                    continue
                action.setChecked(False)
        super().mousePressEvent(event)
        
    def logout(self):
        self.stacked_widget.setCurrentWidget(self.login.login_widget)
        self.login.login.line_kullanici.clear()
        self.login.login.line_sifre.clear()
        self.login.login.label_login_error.setText("")
        self.login.login.line_kullanici.setFocus()
        self.is_enable(False)
        for action in self.ui.toolBar.actions():
            if action.isSeparator():
                continue
            action.setChecked(False)
            
    def exit(self):
        sys.exit()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
        
        