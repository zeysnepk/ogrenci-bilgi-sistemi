from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1126)
        Form.setStyleSheet("""
#Form{
	background-color: rgb(222, 221, 220);
}
QLineEdit, QTextEdit {
background-color: rgb(255, 255, 255);
            padding: 2px 18px;
            font: 18pt "Century Gothic";
            color: rgb(88, 87, 87);
            border: 2px solid rgba(166, 73, 58, 225);
            border-radius: 5px;
            height: 40px;
}
QLineEdit:focus , QTextEdit:focus{
background-color: rgba(223, 128, 112, 80);
        }
QLabel{
	font: 24pt "Century Gothic";
	color: rgb(163, 72, 50);
}
QComboBox{
    padding: 8px 8px;
    font: 16pt "Century Gothic";
    height: 20px;
    width: 30px;
    background-color: rgba(223, 128, 112, 80);
	color: rgba(88, 87, 87, 201);
    combobox-popup: 0;
}
QComboBox::focus {
    background-color: rgba(223, 128, 112, 80);
    border: 2px solid #A34832;
    color: rgba(88, 87, 87, 201);
}
QPushButton{
	font: "Century Gothic";
	background-color: rgb(118, 187, 211);
	border: none;
	border-radius: 12px;
 	color: white;
     padding: 12px 24px;
     font-size: 18px;
     font-weight: bold;
        }
QPushButton:hover {
	background-color: rgb(79, 127, 144);
}
QPushButton:pressed {
	background-color: rgb(55, 88, 100);
}
QSpinBox {
                font-size: 20px;
                padding: 2px;
			background-color: rgba(223, 128, 112, 99);
                border: none;
                border-radius: 5px;
                width: 20px;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                width: 20px;
                height: 30px;
            }
            QSpinBox:focus {
                border: 2px solid #A34832;
           }
""")
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setContentsMargins(70, 70, 70, 70)
        self.gridLayout_5.setHorizontalSpacing(50)
        self.gridLayout_5.setVerticalSpacing(20)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setStyleSheet("#label_13{\n"
"font: 700 44pt \"Century Gothic\";\n"
"color: rgb(223, 128, 112);\n"
"}\n"
"")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.gridLayout_5.addLayout(self.verticalLayout_8, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.frame_ogr = QtWidgets.QFrame(Form)
        self.frame_ogr.setStyleSheet("#frame_ogr{\n"
"    background-color: rgb(253, 255, 255);\n"
"}")
        self.frame_ogr.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ogr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ogr.setObjectName("frame_ogr")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_ogr)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.frame_ogr)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.frame_ogr)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.frame_ogr)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.frame_ogr)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(7, 2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem9)
        self.line_ad = QtWidgets.QLineEdit(self.frame_ogr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_ad.sizePolicy().hasHeightForWidth())
        self.line_ad.setSizePolicy(sizePolicy)
        self.line_ad.setObjectName("line_ad")
        self.verticalLayout.addWidget(self.line_ad)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem10)
        self.line_soyad = QtWidgets.QLineEdit(self.frame_ogr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_soyad.sizePolicy().hasHeightForWidth())
        self.line_soyad.setSizePolicy(sizePolicy)
        self.line_soyad.setObjectName("line_soyad")
        self.verticalLayout.addWidget(self.line_soyad)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem11)
        self.line_no = QtWidgets.QLineEdit(self.frame_ogr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_no.sizePolicy().hasHeightForWidth())
        self.line_no.setSizePolicy(sizePolicy)
        self.line_no.setObjectName("line_no")
        self.verticalLayout.addWidget(self.line_no)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem12)
        self.text_adres = QtWidgets.QTextEdit(self.frame_ogr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_adres.sizePolicy().hasHeightForWidth())
        self.text_adres.setSizePolicy(sizePolicy)
        self.text_adres.setObjectName("text_adres")
        self.verticalLayout.addWidget(self.text_adres)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem13)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(7, 2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem14, 2, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 1, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem16, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 1, 2, 1, 1)
        self.horizontalLayout_6.addWidget(self.frame_ogr)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem18, 1, 0, 1, 1)

        self.frame_egt = QtWidgets.QFrame(Form)
        self.frame_egt.setStyleSheet("#frame_egt{\n"
"    background-color: rgb(253, 255, 255);\n"
"}")
        self.frame_egt.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_egt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_egt.setObjectName("frame_egt")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_egt)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem19, 1, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem20, 4, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem21, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem22)
        self.pushButton_devam = QtWidgets.QPushButton(self.frame_egt)
        self.pushButton_devam.setStyleSheet("""
            #pushButton_devam {
                background-color: #8EC758;
            }
            #pushButton_devam:hover {
                background-color: #7AB347;
            }
            #pushButton_devam:pressed {
                background-color: #6A9F3E;
            }
        """)
        self.pushButton_devam.setObjectName("pushButton_devam")
        self.horizontalLayout_4.addWidget(self.pushButton_devam)
        
        self.pushButton = QtWidgets.QPushButton(self.frame_egt)
        self.pushButton.setStyleSheet("""
            #pushButton {
                background-color: #3498db;
            }
            #pushButton:hover {
                background-color: #2980b9;
            }
            #pushButton:pressed {
                background-color: #2471a3;
            }
        """)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        
        self.pushButton_iptal = QtWidgets.QPushButton(self.frame_egt)
        self.pushButton_iptal.setStyleSheet("""
            #pushButton_iptal {
                background-color: rgb(118, 187, 211);
            }
            #pushButton_iptal:hover {
                background-color: rgb(79, 127, 144);
            }
            #pushButton_iptal:pressed {
                background-color: rgb(55, 88, 100);
            }
        """)
        self.pushButton_iptal.setObjectName("pushButton_iptal")
        self.pushButton_iptal.setText("İPTAL")
        self.horizontalLayout_4.addWidget(self.pushButton_iptal)
        
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem23)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)
        

        self.label_registration_confirm = QtWidgets.QLabel(self.frame_egt)
        self.label_registration_confirm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_registration_confirm.setObjectName("label_onayla_buton")
        self.label_registration_confirm.setStyleSheet("color: green; font-size: 18pt;")
        self.label_registration_confirm.setText("")
        self.gridLayout_2.addWidget(self.label_registration_confirm, 4, 2, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem24, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem25)
        self.label_5 = QtWidgets.QLabel(self.frame_egt)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem26)
        self.label_6 = QtWidgets.QLabel(self.frame_egt)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem27)
        self.label_7 = QtWidgets.QLabel(self.frame_egt)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem28)
        self.label_8 = QtWidgets.QLabel(self.frame_egt)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem29)
        self.label_9 = QtWidgets.QLabel(self.frame_egt)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem30)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem31)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem32)
        self.combo_brans1 = QtWidgets.QComboBox(self.frame_egt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_brans1.sizePolicy().hasHeightForWidth())
        self.combo_brans1.setSizePolicy(sizePolicy)
        self.combo_brans1.setObjectName("combo_brans1")
        self.verticalLayout_4.addWidget(self.combo_brans1)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem33)
        self.combo_egt1 = QtWidgets.QComboBox(self.frame_egt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_egt1.sizePolicy().hasHeightForWidth())
        self.combo_egt1.setSizePolicy(sizePolicy)
        self.combo_egt1.setObjectName("combo_egt1")
        self.verticalLayout_4.addWidget(self.combo_egt1)
        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem34)
        self.combo_paket = QtWidgets.QComboBox(self.frame_egt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_paket.sizePolicy().hasHeightForWidth())
        self.combo_paket.setSizePolicy(sizePolicy)
        self.combo_paket.setObjectName("combo_paket")
        self.verticalLayout_4.addWidget(self.combo_paket)
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem35)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem36)
        self.spinBox = QtWidgets.QSpinBox(self.frame_egt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMaximumSize(QtCore.QSize(190, 16777215))
        self.spinBox.setStyleSheet("")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_5.addWidget(self.spinBox)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem37)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem38)
        self.line_tutar = QtWidgets.QLineEdit(self.frame_egt)
        self.line_tutar.setText("")
        self.line_tutar.setAlignment(QtCore.Qt.AlignCenter)
        self.line_tutar.setReadOnly(False)
        self.line_tutar.setObjectName("line_tutar")
        self.verticalLayout_4.addWidget(self.line_tutar)
        spacerItem39 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem39)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 2, 1, 1)
        self.label_onayla = QtWidgets.QLabel(self.frame_egt)
        self.label_onayla.setStyleSheet("""
        #label_onayla {
            color: red;
            font-size: 14px;
            font-weight: bold;
        }
        """)
        self.label_onayla.setAlignment(QtCore.Qt.AlignCenter)
        self.label_onayla.setObjectName("label_onayla")
        self.gridLayout_2.addWidget(self.label_onayla, 2, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame_egt, 1, 1, 1, 1)
        spacerItem40 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem40, 0, 1, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem41, 1, 2, 1, 1)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem42, 2, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem43)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        spacerItem44 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_5.addItem(spacerItem44, 4, 0, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_5.addItem(spacerItem45, 2, 0, 1, 1)
        
        def add_shadow(widget):
            shadow = QGraphicsDropShadowEffect(Form)
            shadow.setBlurRadius(20)
            shadow.setXOffset(0)
            shadow.setYOffset(10)
            shadow.setColor(QtGui.QColor(0, 0, 0, 50))
            widget.setGraphicsEffect(shadow)


        self.frame_ogr.setStyleSheet("#frame_ogr{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        add_shadow(self.frame_ogr)

        self.frame_egt.setStyleSheet("#frame_egt{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        add_shadow(self.frame_egt)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_13.setText(_translate("Form", "Öğrenci Kayıt Ekranı"))
        self.label.setText(_translate("Form", "Öğrenci Ad:"))
        self.label_2.setText(_translate("Form", "Öğrenci Soyad:"))
        self.label_3.setText(_translate("Form", "İletişim No:"))
        self.label_4.setText(_translate("Form", "Adres:"))
        self.pushButton_devam.setText(_translate("Form", "DEVAM ET"))
        self.pushButton.setText(_translate("Form", "ONAYLA"))
        self.label_5.setText(_translate("Form", "Branş:"))
        self.label_6.setText(_translate("Form", "Eğitmen:"))
        self.label_7.setText(_translate("Form", "Paket Tipi:"))
        self.label_8.setText(_translate("Form", "Saat Sayısı:"))
        self.label_9.setText(_translate("Form", "Tutar:"))
        self.label_onayla.setText(_translate("Form", "Lütfen diğer branş ve eğitmen seçimleri için '<span style=\"color: rgba(76, 175, 80, 1);\">DEVAM ET</span>' seçeneğini seçiniz!"))
