from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1680, 1000)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(222, 221, 220);\n"
"}")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(450, 330))
        self.widget_2.setStyleSheet("#widget_2{\n"
"    image: url(:/anasayfa/png/logo.png);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(253, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("#label{\n"
"    font: 36pt \"Century Gothic\" bold;\n"
"    color: rgba(166, 73, 58, 225);\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("#label_2{\n"
"    font: 20pt \"Century Gothic\" bold;\n"
"    color: rgb(246, 134, 66);\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout.addWidget(self.frame_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem14)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem16, 1, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem17, 4, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem18, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 2, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 2, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem21, 3, 1, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem22)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setMinimumSize(QtCore.QSize(450, 180))
        self.widget.setStyleSheet("#widget{\n"
"    image: url(:/giris/png/login.png);\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem23)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem24)
        
        input_style = """
        QLineEdit {
            background-color: rgb(255, 255, 255);
            padding: 2px 18px;
            font: 18pt "Century Gothic";
            color: rgb(88, 87, 87);
            border: 2px solid rgba(166, 73, 58, 225);
            border-radius: 5px;
            height: 40px;
            
        }
        QLineEdit:focus {
            background-color: rgba(223, 128, 112, 80);
        }
        """
        
        self.line_kullanici = QtWidgets.QLineEdit(self.frame)
        self.line_kullanici.setMinimumSize(QtCore.QSize(350, 44))
        self.line_kullanici.setStyleSheet(input_style)
        self.line_kullanici.setObjectName("line_kullanici")
        self.horizontalLayout_3.addWidget(self.line_kullanici)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem25)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem26)
        self.line_sifre = QtWidgets.QLineEdit(self.frame)
        self.line_sifre.setMinimumSize(QtCore.QSize(350, 44))
        self.line_sifre.setStyleSheet(input_style)
        
        self.line_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_sifre.setObjectName("line_sifre")
        self.horizontalLayout_4.addWidget(self.line_sifre)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem27)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem28)
        self.button_giris = QtWidgets.QPushButton(self.frame)
        self.button_giris.setMinimumSize(QtCore.QSize(150, 45))
        self.button_giris.setStyleSheet("""
        #button_giris {
            font: \"Century Gothic\";
            background-color: #A34832;
            border: none;
            border-radius: 12px;
            color: white;
            padding: 12px 24px;
            font-size: 18px;
            font-weight: bold;
        }
        #button_giris:hover {
            background-color: #8B3A28;
        }
        #button_giris:pressed {
            background-color: #732E22;
        }
        """)
        self.button_giris.setAutoDefault(False)
        self.button_giris.setDefault(False)
        self.button_giris.setFlat(False)
        self.button_giris.setObjectName("button_giris")
        self.horizontalLayout_5.addWidget(self.button_giris)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem29)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        
        self.label_login_error = QtWidgets.QLabel(self.frame)
        self.label_login_error.setStyleSheet("""
        #label_login_error {
            color: red;
            font-size: 14px;
            font-weight: bold;
        }
        """)
        self.label_login_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login_error.setObjectName("label_login_error")
        self.verticalLayout_3.addWidget(self.label_login_error)
        
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem30)
        self.gridLayout.addWidget(self.frame, 2, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem31)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem32)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("#label_3{\n"
"    font: 16pt \"Baskerville\";\n"
"    color: rgb(99, 104, 110);\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem33)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem34)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem35)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("#label_4{\n"
"    font: 20pt \"Baskerville\";\n"
"    color: rgb(99, 104, 110);\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem36)
        self.frame_ogr_sayi = QtWidgets.QFrame(Form)
        self.frame_ogr_sayi.setMinimumSize(QtCore.QSize(400, 100))
        self.frame_ogr_sayi.setStyleSheet("#frame_ogr_sayi{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 60px\n"
"}")
        self.frame_ogr_sayi.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ogr_sayi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ogr_sayi.setObjectName("frame_ogr_sayi")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_ogr_sayi)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_ogr_sayi = QtWidgets.QLabel(self.frame_ogr_sayi)
        self.label_ogr_sayi.setStyleSheet("#label_ogr_sayi{\n"
"    font: 90pt \"Baskerville\";\n"
"    color: rgb(166, 73, 58);\n"
"}")
        self.label_ogr_sayi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ogr_sayi.setObjectName("label_ogr_sayi")
        self.verticalLayout_4.addWidget(self.label_ogr_sayi)
        self.horizontalLayout_8.addWidget(self.frame_ogr_sayi)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem37)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem38)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("#label_5{\n"
"    font: 20pt \"Baskerville\";\n"
"    color: rgb(99, 104, 110);\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem39)
        self.frame_egt_sayi = QtWidgets.QFrame(Form)
        self.frame_egt_sayi.setMinimumSize(QtCore.QSize(400, 100))
        self.frame_egt_sayi.setStyleSheet("#frame_egt_sayi{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 60px\n"
"}")
        self.frame_egt_sayi.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_egt_sayi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_egt_sayi.setObjectName("frame_egt_sayi")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_egt_sayi)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_egt_sayi = QtWidgets.QLabel(self.frame_egt_sayi)
        self.label_egt_sayi.setStyleSheet("#label_egt_sayi{\n"
"    font: 90pt \"Baskerville\";\n"
"    color: rgb(166, 73, 58);\n"
"}")
        self.label_egt_sayi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_egt_sayi.setObjectName("label_egt_sayi")
        self.verticalLayout_5.addWidget(self.label_egt_sayi)
        self.horizontalLayout_9.addWidget(self.frame_egt_sayi)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem40)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_7.addItem(spacerItem41)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("#label_6{\n"
"    font: 20pt \"Baskerville\";\n"
"    color: rgb(99, 104, 110);\n"
"}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem42)
        self.frame_brans_sayi = QtWidgets.QFrame(Form)
        self.frame_brans_sayi.setMinimumSize(QtCore.QSize(400, 100))
        self.frame_brans_sayi.setStyleSheet("#frame_brans_sayi{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 60px\n"
"}")
        self.frame_brans_sayi.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_brans_sayi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_brans_sayi.setObjectName("frame_brans_sayi")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_brans_sayi)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_brans_sayi = QtWidgets.QLabel(self.frame_brans_sayi)
        self.label_brans_sayi.setMinimumSize(QtCore.QSize(0, 0))
        self.label_brans_sayi.setStyleSheet("#label_brans_sayi{\n"
"    font: 90pt \"Baskerville\";\n"
"    color: rgb(166, 73, 58);\n"
"}")
        self.label_brans_sayi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_brans_sayi.setObjectName("label_brans_sayi")
        self.verticalLayout_6.addWidget(self.label_brans_sayi)
        self.horizontalLayout_10.addWidget(self.frame_brans_sayi)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem43)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        spacerItem44 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem44)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem45)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem46)
        

        def add_shadow(widget):
            shadow = QGraphicsDropShadowEffect(Form)
            shadow.setBlurRadius(20)
            shadow.setXOffset(0)
            shadow.setYOffset(10)
            shadow.setColor(QtGui.QColor(0, 0, 0, 50))
            widget.setGraphicsEffect(shadow)

        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(253, 255, 255);\n"
"}")
        add_shadow(self.frame_2)

        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        add_shadow(self.frame)

        self.frame_ogr_sayi.setStyleSheet("#frame_ogr_sayi{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 60px\n"
"}")
        add_shadow(self.frame_ogr_sayi)

        self.frame_egt_sayi.setStyleSheet("#frame_egt_sayi{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 60px\n"
"}")
        add_shadow(self.frame_egt_sayi)

        self.frame_brans_sayi.setStyleSheet("#frame_brans_sayi{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 60px\n"
"}")
        add_shadow(self.frame_brans_sayi)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Bugün\n"
"Günlerden\n"
"Ne?"))
        self.label_2.setText(_translate("Form", "\"Günden güne artar günler\n"
"ve azalır ömürler\""))
        self.line_kullanici.setPlaceholderText(_translate("Form", "Kullanıcı adınızı giriniz..."))
        self.line_sifre.setPlaceholderText(_translate("Form", "Şifrenizi giriniz..."))
        self.button_giris.setText(_translate("Form", "Giriş Yap"))
        self.label_4.setText(_translate("Form", "Toplam Öğrenci Sayısı"))
        self.label_ogr_sayi.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", "Toplam Eğitmen Sayısı"))
        self.label_egt_sayi.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "Branş Sayısı"))
        self.label_brans_sayi.setText(_translate("Form", "0"))
from . import pic_rc

