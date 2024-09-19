from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1916, 1073)
        font = QtGui.QFont()
        Form.setFont(font)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(222, 221, 220);\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 24pt \"Century Gothic\";\n"
"    color: rgb(88, 87, 87);\n"
"}\n"
"QComboBox {\n"
"    padding: 8px 8px;\n"
"    font: 16pt \"Century Gothic\";\n"
"    height: 20px;\n"
"    width: 30px;\n"
"    background-color: rgba(223, 128, 112, 80);\n"
"    color: rgba(88, 87, 87, 201);\n"
"    combobox-popup: 0;\n"
"}\n"
"\n"
"QComboBox::focus {\n"
"    background-color: rgba(223, 128, 112, 80);\n"
"    border: 2px solid #A34832;\n"
"    color: rgba(88, 87, 87, 201);\n"
"}\n"
"\n"
"QListWidget {\n"
"     background-color: white;\n"
"     border: 1px solid #e0e0e0;\n"
"     border-radius: 5px;\n"
"}\n"
"QListWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"QPushButton{\n"
"    font: \"Century Gothic\";\n"
"    background-color: rgb(118, 187, 211);\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"     color: white;\n"
"     padding: 12px 24px;\n"
"     font-size: 18px;\n"
"     font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(79, 127, 144);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 88, 100);\n"
"}\n"
"QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 2px 18px;\n"
"    border: 2px solid rgba(166, 73, 58, 225);\n"
"    font: 22pt \"Century Gothic\";\n"
"    color: rgb(88, 87, 87);\n"
"    height: 40px;\n"
"}\n"
"")
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setContentsMargins(70, 70, 70, 70)
        self.gridLayout_6.setHorizontalSpacing(50)
        self.gridLayout_6.setVerticalSpacing(20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("#label{\n"
"font: 700 58pt \"Century Gothic\";\n"
"color: rgb(223, 128, 112);\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_8.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgb(253, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.widget_kasa = QtWidgets.QWidget(self.frame)
        self.widget_kasa.setMinimumSize(QtCore.QSize(360, 360))
        self.widget_kasa.setMaximumSize(QtCore.QSize(360, 360))
        self.widget_kasa.setStyleSheet("#widget_kasa{\n"
"border-radius: 180px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.005  rgb(120, 141, 194), stop:0.006  rgb(120, 141, 194), stop:0.995 rgb(120, 141, 194), stop:0.996 rgba(185, 51, 34, 0));\n"
"    color: rgb(120, 141, 194);\n"
"}")
        self.widget_kasa.setObjectName("widget_kasa")
        self.widget_2 = QtWidgets.QWidget(self.widget_kasa)
        self.widget_2.setGeometry(QtCore.QRect(20, 20, 320, 320))
        self.widget_2.setMinimumSize(QtCore.QSize(320, 320))
        self.widget_2.setMaximumSize(QtCore.QSize(320, 320))
        self.widget_2.setStyleSheet("#widget_2{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 160px\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_kasa = QtWidgets.QLabel(self.widget_2)
        self.label_kasa.setMinimumSize(QtCore.QSize(256, 256))
        self.label_kasa.setMaximumSize(QtCore.QSize(256, 256))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        self.label_kasa.setFont(font)
        self.label_kasa.setStyleSheet("#label_kasa{\n"
"font: 700 32pt \"Century Gothic\";\n"
"color: rgb(88, 87, 87);\n"
"}\n"
"")
        self.label_kasa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kasa.setWordWrap(True)
        self.label_kasa.setObjectName("label_kasa")
        self.horizontalLayout_2.addWidget(self.label_kasa)
        self.verticalLayout_11.addWidget(self.widget_kasa)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.widget_gider = QtWidgets.QWidget(self.frame)
        self.widget_gider.setMinimumSize(QtCore.QSize(260, 260))
        self.widget_gider.setMaximumSize(QtCore.QSize(260, 260))
        self.widget_gider.setStyleSheet("#widget_gider{\n"
"\n"
"border-radius: 130px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.005  rgba(207, 85, 73,214), stop:0.006  rgba(207, 85, 73,214), stop:0.995 rgba(207, 85, 73,214), stop:0.996 rgba(185, 51, 34, 0));\n"
"    color: rgba(207, 85, 73, 214);\n"
"}")
        self.widget_gider.setObjectName("widget_gider")
        self.widget_4 = QtWidgets.QWidget(self.widget_gider)
        self.widget_4.setGeometry(QtCore.QRect(20, 20, 220, 220))
        self.widget_4.setMinimumSize(QtCore.QSize(220, 220))
        self.widget_4.setMaximumSize(QtCore.QSize(220, 220))
        self.widget_4.setStyleSheet("#widget_4{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 110px\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_gider = QtWidgets.QLabel(self.widget_4)
        self.label_gider.setMinimumSize(QtCore.QSize(176, 176))
        self.label_gider.setMaximumSize(QtCore.QSize(176, 176))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label_gider.setFont(font)
        self.label_gider.setStyleSheet("#label_gider\n"
"{\n"
"font: 700 24pt \"Century Gothic\";\n"
"color: rgb(88, 87, 87);\n"
"}\n"
"")
        self.label_gider.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gider.setWordWrap(True)
        self.label_gider.setObjectName("label_gider")
        self.horizontalLayout_3.addWidget(self.label_gider)
        self.verticalLayout.addWidget(self.widget_gider)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.widget_kayit_ucret = QtWidgets.QWidget(self.frame)
        self.widget_kayit_ucret.setMinimumSize(QtCore.QSize(260, 260))
        self.widget_kayit_ucret.setMaximumSize(QtCore.QSize(260, 260))
        self.widget_kayit_ucret.setStyleSheet("#widget_kayit_ucret{\n"
"\n"
"border-radius: 130px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.005  rgb(227, 196, 86), stop:0.006  rgb(227, 196, 86), stop:0.995 rgb(227, 196, 86), stop:0.996 rgba(185, 51, 34, 0));\n"
"    \n"
"    color: rgb(227, 196, 86);\n"
"}")
        self.widget_kayit_ucret.setObjectName("widget_kayit_ucret")
        self.widget_5 = QtWidgets.QWidget(self.widget_kayit_ucret)
        self.widget_5.setGeometry(QtCore.QRect(20, 20, 220, 220))
        self.widget_5.setMinimumSize(QtCore.QSize(220, 220))
        self.widget_5.setMaximumSize(QtCore.QSize(220, 220))
        self.widget_5.setStyleSheet("#widget_5{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 110px\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_kayit_ucret = QtWidgets.QLabel(self.widget_5)
        self.label_kayit_ucret.setMinimumSize(QtCore.QSize(176, 176))
        self.label_kayit_ucret.setMaximumSize(QtCore.QSize(176, 176))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label_kayit_ucret.setFont(font)
        self.label_kayit_ucret.setStyleSheet("#label_kayit_ucret\n"
"{\n"
"font: 700 24pt \"Century Gothic\";\n"
"color: rgb(88, 87, 87);\n"
"}\n"
"")
        self.label_kayit_ucret.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kayit_ucret.setWordWrap(True)
        self.label_kayit_ucret.setObjectName("label_kayit_ucret")
        self.horizontalLayout_4.addWidget(self.label_kayit_ucret)
        self.verticalLayout_2.addWidget(self.widget_kayit_ucret)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.widget_kalan_odeme = QtWidgets.QWidget(self.frame)
        self.widget_kalan_odeme.setMinimumSize(QtCore.QSize(260, 260))
        self.widget_kalan_odeme.setMaximumSize(QtCore.QSize(260, 260))
        self.widget_kalan_odeme.setStyleSheet("#widget_kalan_odeme{\n"
"\n"
"border-radius: 130px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.005  rgba(56, 90, 213, 236), stop:0.006  rgba(56, 90, 213, 236), stop:0.995 rgba(56, 90, 213, 236), stop:0.996 rgba(185, 51, 34, 0));\n"
"    \n"
"    \n"
"    color: rgba(56, 90, 213, 236);\n"
"}")
        self.widget_kalan_odeme.setObjectName("widget_kalan_odeme")
        self.widget_7 = QtWidgets.QWidget(self.widget_kalan_odeme)
        self.widget_7.setGeometry(QtCore.QRect(20, 20, 220, 220))
        self.widget_7.setMinimumSize(QtCore.QSize(220, 220))
        self.widget_7.setMaximumSize(QtCore.QSize(220, 220))
        self.widget_7.setStyleSheet("#widget_7{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 110px\n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_kalan_odeme = QtWidgets.QLabel(self.widget_7)
        self.label_kalan_odeme.setMinimumSize(QtCore.QSize(176, 176))
        self.label_kalan_odeme.setMaximumSize(QtCore.QSize(176, 176))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label_kalan_odeme.setFont(font)
        self.label_kalan_odeme.setStyleSheet("#label_kalan_odeme\n"
"{\n"
"font: 700 24pt \"Century Gothic\";\n"
"color: rgb(88, 87, 87);\n"
"}\n"
"")
        self.label_kalan_odeme.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kalan_odeme.setWordWrap(True)
        self.label_kalan_odeme.setObjectName("label_kalan_odeme")
        self.horizontalLayout_5.addWidget(self.label_kalan_odeme)
        self.verticalLayout_9.addWidget(self.widget_kalan_odeme)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem10)
        self.widget_egt_odeme = QtWidgets.QWidget(self.frame)
        self.widget_egt_odeme.setMinimumSize(QtCore.QSize(260, 260))
        self.widget_egt_odeme.setMaximumSize(QtCore.QSize(260, 260))
        self.widget_egt_odeme.setStyleSheet("#widget_egt_odeme{\n"
"\n"
"border-radius: 130px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.005  rgba(104, 214, 120, 212), stop:0.006  rgba(104, 214, 120, 212), stop:0.995 rgba(104, 214, 120, 212), stop:0.996 rgba(185, 51, 34, 0));\n"
"    \n"
"    color: rgba(104, 214, 120, 212);\n"
"}")
        self.widget_egt_odeme.setObjectName("widget_egt_odeme")
        self.widget_6 = QtWidgets.QWidget(self.widget_egt_odeme)
        self.widget_6.setGeometry(QtCore.QRect(20, 20, 220, 220))
        self.widget_6.setMinimumSize(QtCore.QSize(220, 220))
        self.widget_6.setMaximumSize(QtCore.QSize(220, 220))
        self.widget_6.setStyleSheet("#widget_6{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 110px\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_egt_odeme = QtWidgets.QLabel(self.widget_6)
        self.label_egt_odeme.setMinimumSize(QtCore.QSize(176, 176))
        self.label_egt_odeme.setMaximumSize(QtCore.QSize(176, 176))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label_egt_odeme.setFont(font)
        self.label_egt_odeme.setStyleSheet("#label_egt_odeme\n"
"{\n"
"font: 700 24pt \"Century Gothic\";\n"
"color: rgb(88, 87, 87);\n"
"}\n"
"")
        self.label_egt_odeme.setAlignment(QtCore.Qt.AlignCenter)
        self.label_egt_odeme.setWordWrap(True)
        self.label_egt_odeme.setObjectName("label_egt_odeme")
        self.horizontalLayout_6.addWidget(self.label_egt_odeme)
        self.verticalLayout_10.addWidget(self.widget_egt_odeme)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem12, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 1, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem14, 1, 7, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setStyleSheet("#label_17{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_16.addWidget(self.label_17)
        self.label_odenmis_tutar = QtWidgets.QLabel(self.frame)
        self.label_odenmis_tutar.setStyleSheet("#label_odenmis_tutar{\n"
"font: 20pt;\n"
"}")
        self.label_odenmis_tutar.setText("")
        self.label_odenmis_tutar.setObjectName("label_odenmis_tutar")
        self.horizontalLayout_16.addWidget(self.label_odenmis_tutar)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem15)
        self.horizontalLayout_16.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_16, 5, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem16, 8, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem17, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setStyleSheet("#label_16{\n"
"color: rgb(163, 72, 50);\n"
"}")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.label_beklenen_tutar = QtWidgets.QLabel(self.frame)
        self.label_beklenen_tutar.setStyleSheet("#label_beklenen_tutar{\n"
"font: 20pt;\n"
"}")
        self.label_beklenen_tutar.setText("")
        self.label_beklenen_tutar.setObjectName("label_beklenen_tutar")
        self.horizontalLayout_15.addWidget(self.label_beklenen_tutar)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem18)
        self.horizontalLayout_15.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)
        self.comboBox_ogr = QtWidgets.QComboBox(self.frame)
        self.comboBox_ogr.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_ogr.setObjectName("comboBox_ogr")
        self.comboBox_ogr.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_ogr, 2, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setStyleSheet("#label_18{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.label_kalan_tutar = QtWidgets.QLabel(self.frame)
        self.label_kalan_tutar.setStyleSheet("#label_kalan_tutar{\n"
"font: 20pt;\n"
"}")
        self.label_kalan_tutar.setText("")
        self.label_kalan_tutar.setObjectName("label_kalan_tutar")
        self.horizontalLayout_17.addWidget(self.label_kalan_tutar)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem19)
        self.horizontalLayout_17.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_17, 6, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setStyleSheet("#label_19{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_18.addWidget(self.label_19)
        self.label_son_odeme = QtWidgets.QLabel(self.frame)
        self.label_son_odeme.setStyleSheet("#label_son_odeme{\n"
"font: 20pt;\n"
"}")
        self.label_son_odeme.setText("")
        self.label_son_odeme.setObjectName("label_son_odeme")
        self.horizontalLayout_18.addWidget(self.label_son_odeme)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem20)
        self.horizontalLayout_18.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_18, 7, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem21, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 3, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem22, 0, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_5.addWidget(self.listWidget, 0, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem23, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem24, 1, 5, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 1, 11, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem25)
        self.pushButton_gider = QtWidgets.QPushButton(self.frame)
        self.pushButton_gider.setObjectName("pushButton_gider")
        self.horizontalLayout_8.addWidget(self.pushButton_gider)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem26)
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem27, 0, 0, 1, 1)
        self.line_aciklama = QtWidgets.QLineEdit(self.frame)
        self.line_aciklama.setStyleSheet("")
        self.line_aciklama.setText("")
        self.line_aciklama.setAlignment(QtCore.Qt.AlignCenter)
        self.line_aciklama.setReadOnly(False)
        self.line_aciklama.setObjectName("line_aciklama")
        self.gridLayout_7.addWidget(self.line_aciklama, 4, 0, 1, 1)
        self.line_tutar = QtWidgets.QLineEdit(self.frame)
        self.line_tutar.setStyleSheet("")
        self.line_tutar.setText("")
        self.line_tutar.setAlignment(QtCore.Qt.AlignCenter)
        self.line_tutar.setReadOnly(False)
        self.line_tutar.setObjectName("line_tutar")
        self.gridLayout_7.addWidget(self.line_tutar, 3, 0, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem28, 7, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_7.addWidget(self.line_6, 2, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setStyleSheet("#label_26{\n"
"    font: 700 24pt \"Century Gothic\";\n"
"}")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 1, 0, 1, 1)
        self.label_gider_error = QtWidgets.QLabel(self.frame)
        self.label_gider_error.setStyleSheet("#label_gider_error{\n"
"    font:  16pt \"Century Gothic\";\n"
"}")
        self.label_gider_error.setText("")
        self.label_gider_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gider_error.setWordWrap(False)
        self.label_gider_error.setObjectName("label_gider_error")
        self.gridLayout_7.addWidget(self.label_gider_error, 6, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_7, 1, 13, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem29, 1, 9, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem30, 1, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setStyleSheet("#label_21{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_20.addWidget(self.label_21)
        self.label_son_odeme_egt = QtWidgets.QLabel(self.frame)
        self.label_son_odeme_egt.setStyleSheet("#label_son_odeme_egt{\n"
"font: 20pt;\n"
"}")
        self.label_son_odeme_egt.setText("")
        self.label_son_odeme_egt.setObjectName("label_son_odeme_egt")
        self.horizontalLayout_20.addWidget(self.label_son_odeme_egt)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem31)
        self.horizontalLayout_20.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_20, 5, 0, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setStyleSheet("#label_23{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_22.addWidget(self.label_23)
        self.label_yapilan_odeme = QtWidgets.QLabel(self.frame)
        self.label_yapilan_odeme.setStyleSheet("#label_yapilan_odeme{\n"
"font: 20pt;\n"
"}")
        self.label_yapilan_odeme.setText("")
        self.label_yapilan_odeme.setObjectName("label_yapilan_odeme")
        self.horizontalLayout_22.addWidget(self.label_yapilan_odeme)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem32)
        self.horizontalLayout_22.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_22, 4, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setStyleSheet("#label_20{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_19.addWidget(self.label_20)
        self.label_yapilacak_odeme = QtWidgets.QLabel(self.frame)
        self.label_yapilacak_odeme.setStyleSheet("#label_yapilacak_odeme{\n"
"font: 20pt;\n"
"}")
        self.label_yapilacak_odeme.setText("")
        self.label_yapilacak_odeme.setObjectName("label_yapilacak_odeme")
        self.horizontalLayout_19.addWidget(self.label_yapilacak_odeme)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem33)
        self.horizontalLayout_19.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_19, 3, 0, 1, 1)
        self.comboBox_egt = QtWidgets.QComboBox(self.frame)
        self.comboBox_egt.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_egt.setObjectName("comboBox_egt")
        self.comboBox_egt.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_egt, 1, 0, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem34, 0, 0, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem35, 6, 0, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem36, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 8, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 1, 6, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem37, 1, 12, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 4, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem38)
        self.gridLayout.addLayout(self.horizontalLayout_9, 5, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 2, 0, 1, 1)
        self.label_tarih = QtWidgets.QLabel(Form)
        self.label_tarih.setStyleSheet("#label_tarih{\n"
"color: rgb(87, 103, 142);\n"
"font: 22pt \"Century Gothic\";\n"
"}")
        self.label_tarih.setObjectName("label_tarih")
        self.gridLayout_6.addWidget(self.label_tarih, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "KASA"))
        self.label_kasa.setText(_translate("Form", "Ana\n"
"Kasa"))
        self.label_gider.setText(_translate("Form", "Gider"))
        self.label_kayit_ucret.setText(_translate("Form", "Beklenen\n"
"Tutar"))
        self.label_kalan_odeme.setText(_translate("Form", "Kalan\n"
"Ödeme"))
        self.label_egt_odeme.setText(_translate("Form", "Eğitmen\n"
"Ödemeleri"))
        self.label_17.setText(_translate("Form", "Ödenmiş Tutar:"))
        self.label_16.setText(_translate("Form", "Beklenen Tutar:"))
        self.comboBox_ogr.setItemText(0, _translate("Form", "Öğrenci Seçiniz"))
        self.label_18.setText(_translate("Form", "Kalan Tutar:"))
        self.label_19.setText(_translate("Form", "Son Ödeme:"))
        self.pushButton_gider.setText(_translate("Form", "KAYDET"))
        self.line_aciklama.setPlaceholderText(_translate("Form", "Açıklama giriniz..."))
        self.line_tutar.setPlaceholderText(_translate("Form", "Tutar giriniz...."))
        self.label_26.setText(_translate("Form", "Gider Ekle"))
        self.label_21.setText(_translate("Form", "Son Ödeme:"))
        self.label_23.setText(_translate("Form", "Yapılan Ödeme:"))
        self.label_20.setText(_translate("Form", "Yapılacak Ödeme:"))
        self.comboBox_egt.setItemText(0, _translate("Form", "Eğitmen Seçiniz"))
        self.label_tarih.setText(_translate("Form", "16/09/2024"))
