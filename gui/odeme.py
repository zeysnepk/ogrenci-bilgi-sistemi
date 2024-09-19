from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1448, 1151)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(222, 221, 220);\n"
"}\n"
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
"QTextEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 2px 18px;\n"
"    border: 2px solid rgba(166, 73, 58, 225);\n"
"    font: 22pt \"Century Gothic\";\n"
"    color: rgb(88, 87, 87);\n"
"    height: 40px;\n"
"}\n"
"\n"
"")
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setContentsMargins(70, 70, 70, 70)
        self.gridLayout_4.setHorizontalSpacing(50)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_tarih = QtWidgets.QLabel(Form)
        self.label_tarih.setStyleSheet("#label_tarih{\n"
"color: rgb(87, 103, 142);\n"
"font: 22pt \"Century Gothic\";\n"
"}")
        self.label_tarih.setObjectName("label_tarih")
        self.gridLayout_4.addWidget(self.label_tarih, 1, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("#label{\n"
"font: 700 44pt \"Century Gothic\";\n"
"color: rgb(223, 128, 112);\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.gridLayout_4.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_ogr = QtWidgets.QComboBox(Form)
        self.comboBox_ogr.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_ogr.setStyleSheet("")
        self.comboBox_ogr.setObjectName("comboBox_ogr")
        self.comboBox_ogr.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_ogr)
        self.frame_bilgi = QtWidgets.QFrame(Form)
        self.frame_bilgi.setStyleSheet("#frame_bilgi{\n"
"    background-color: rgb(253, 255, 255);\n"
"}\n"
"")
        self.frame_bilgi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bilgi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bilgi.setObjectName("frame_bilgi")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_bilgi)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_12.setStyleSheet("#label_12{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.label_son_tarih = QtWidgets.QLabel(self.frame_bilgi)
        self.label_son_tarih.setStyleSheet("#label_son_tarih{\n"
"font: 20pt;\n"
"}")
        self.label_son_tarih.setText("")
        self.label_son_tarih.setObjectName("label_son_tarih")
        self.horizontalLayout_6.addWidget(self.label_son_tarih)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 16, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_17 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_17.setStyleSheet("#label_17{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_16.addWidget(self.label_17)
        self.label_toplam_odeme = QtWidgets.QLabel(self.frame_bilgi)
        self.label_toplam_odeme.setStyleSheet("#label_toplam_odeme{\n"
"font: 20pt;\n"
"}")
        self.label_toplam_odeme.setText("")
        self.label_toplam_odeme.setObjectName("label_toplam_odeme")
        self.horizontalLayout_16.addWidget(self.label_toplam_odeme)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.horizontalLayout_16.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_16, 14, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        self.label_7.setStyleSheet("#label_7{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.line_3 = QtWidgets.QFrame(self.frame_bilgi)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_brans1 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_brans1.setStyleSheet("#label_brans1{\n"
"font-size: 18pt;\n"
"}")
        self.label_brans1.setText("")
        self.label_brans1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_brans1.setObjectName("label_brans1")
        self.verticalLayout_2.addWidget(self.label_brans1)
        self.label_brans2 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_brans2.setStyleSheet("#label_brans2{\n"
"font-size: 18pt;\n"
"}")
        self.label_brans2.setText("")
        self.label_brans2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_brans2.setObjectName("label_brans2")
        self.verticalLayout_2.addWidget(self.label_brans2)
        self.label_brans3 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_brans3.setStyleSheet("#label_brans3{\n"
"font-size: 18pt;\n"
"}")
        self.label_brans3.setText("")
        self.label_brans3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_brans3.setObjectName("label_brans3")
        self.verticalLayout_2.addWidget(self.label_brans3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_11.setMinimumSize(QtCore.QSize(0, 30))
        self.label_11.setStyleSheet("#label_11{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.line_4 = QtWidgets.QFrame(self.frame_bilgi)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label_egitmen1 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_egitmen1.setStyleSheet("#label_egitmen1{\n"
"font-size: 18pt;\n"
"}")
        self.label_egitmen1.setText("")
        self.label_egitmen1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_egitmen1.setObjectName("label_egitmen1")
        self.verticalLayout.addWidget(self.label_egitmen1)
        self.label_egitmen2 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_egitmen2.setStyleSheet("#label_egitmen2{\n"
"font-size: 18pt;\n"
"}")
        self.label_egitmen2.setText("")
        self.label_egitmen2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_egitmen2.setObjectName("label_egitmen2")
        self.verticalLayout.addWidget(self.label_egitmen2)
        self.label_egitmen3 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_egitmen3.setStyleSheet("#label_egitmen3{\n"
"font-size: 18pt;\n"
"}")
        self.label_egitmen3.setText("")
        self.label_egitmen3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_egitmen3.setObjectName("label_egitmen3")
        self.verticalLayout.addWidget(self.label_egitmen3)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 7, 1, 1, 1)
        self.comboBox_egt = QtWidgets.QComboBox(self.frame_bilgi)
        self.comboBox_egt.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_egt.setObjectName("comboBox_egt")
        self.comboBox_egt.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_egt, 9, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem6, 3, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 5, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem8, 18, 1, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_14.setStyleSheet("#label_14{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.label_no = QtWidgets.QLabel(self.frame_bilgi)
        self.label_no.setStyleSheet("#label_no{\n"
"font: 20pt;\n"
"}")
        self.label_no.setText("")
        self.label_no.setObjectName("label_no")
        self.horizontalLayout_13.addWidget(self.label_no)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem9)
        self.horizontalLayout_13.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 6, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_13.setStyleSheet("#label_13{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.label_kalan_saat = QtWidgets.QLabel(self.frame_bilgi)
        self.label_kalan_saat.setStyleSheet("#label_kalan_saat{\n"
"font: 20pt;\n"
"}")
        self.label_kalan_saat.setText("")
        self.label_kalan_saat.setObjectName("label_kalan_saat")
        self.horizontalLayout_8.addWidget(self.label_kalan_saat)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.horizontalLayout_8.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 13, 1, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_15.setStyleSheet("#label_15{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.label_gecen_saat = QtWidgets.QLabel(self.frame_bilgi)
        self.label_gecen_saat.setStyleSheet("#label_gecen_saat{\n"
"font: 20pt;\n"
"}")
        self.label_gecen_saat.setText("")
        self.label_gecen_saat.setObjectName("label_gecen_saat")
        self.horizontalLayout_14.addWidget(self.label_gecen_saat)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem11)
        self.horizontalLayout_14.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 12, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_9.setStyleSheet("#label_9{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label_kayit_tarih = QtWidgets.QLabel(self.frame_bilgi)
        self.label_kayit_tarih.setStyleSheet("#label_kayit_tarih{\n"
"font: 20pt;\n"
"}")
        self.label_kayit_tarih.setText("")
        self.label_kayit_tarih.setObjectName("label_kayit_tarih")
        self.horizontalLayout_5.addWidget(self.label_kayit_tarih)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.horizontalLayout_5.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem13, 20, 1, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_18.setStyleSheet("#label_18{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.label_kalan_odeme = QtWidgets.QLabel(self.frame_bilgi)
        self.label_kalan_odeme.setStyleSheet("#label_kalan_odeme{\n"
"font: 20pt;\n"
"}")
        self.label_kalan_odeme.setText("")
        self.label_kalan_odeme.setObjectName("label_kalan_odeme")
        self.horizontalLayout_17.addWidget(self.label_kalan_odeme)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem14)
        self.horizontalLayout_17.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_17, 15, 1, 1, 1)
        self.comboBox_egt_2 = QtWidgets.QComboBox(self.frame_bilgi)
        self.comboBox_egt_2.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_egt_2.setObjectName("comboBox_egt_2")
        self.comboBox_egt_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_egt_2, 10, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_10.setStyleSheet("#label_10{\n"
"    color: rgb(163, 72, 50);\n"
"    font:600 28pt;\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem15)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_19 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_19.setStyleSheet("#label_19{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_18.addWidget(self.label_19)
        self.label_ad_soyad = QtWidgets.QLabel(self.frame_bilgi)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_ad_soyad.setFont(font)
        self.label_ad_soyad.setStyleSheet("#label_ad_soyad{\n"
"font: 20pt;\n"
"}")
        self.label_ad_soyad.setText("")
        self.label_ad_soyad.setObjectName("label_ad_soyad")
        self.horizontalLayout_18.addWidget(self.label_ad_soyad)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem16)
        self.horizontalLayout_18.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_18, 4, 1, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.line_2 = QtWidgets.QFrame(self.frame_bilgi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_11.addWidget(self.line_2)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem17)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 2, 1, 1, 1)
        self.comboBox_brans = QtWidgets.QComboBox(self.frame_bilgi)
        self.comboBox_brans.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_brans.setStyleSheet("")
        self.comboBox_brans.setObjectName("comboBox_brans")
        self.comboBox_brans.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_brans, 8, 1, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_16.setStyleSheet("#label_16{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.label_paket = QtWidgets.QLabel(self.frame_bilgi)
        self.label_paket.setStyleSheet("#label_paket{\n"
"font: 20pt;\n"
"}")
        self.label_paket.setText("")
        self.label_paket.setObjectName("label_paket")
        self.horizontalLayout_15.addWidget(self.label_paket)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem18)
        self.horizontalLayout_15.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 11, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_bilgi)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 3, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setAlignment(Qt.AlignCenter)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setStyleSheet("""
            QTextEdit {
                border: none;
                align: center;
                font-align: center;
            }
            QTextEdit::content {
                margin: 20px;
                padding: 20px;
            }
        """)
        self.gridLayout_3.addWidget(self.textEdit, 3, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem20, 5, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 3, 2, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem22, 0, 1, 1, 1)
        self.frame_odeme = QtWidgets.QFrame(Form)
        self.frame_odeme.setStyleSheet("#frame_odeme{\n"
"    background-color: rgb(253, 255, 255);\n"
"}")
        self.frame_odeme.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_odeme.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_odeme.setObjectName("frame_odeme")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_odeme)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem23)
        self.pushButton = QtWidgets.QPushButton(self.frame_odeme)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem24)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_tutar = QtWidgets.QLineEdit(self.frame_odeme)
        self.line_tutar.setStyleSheet("")
        self.line_tutar.setText("")
        self.line_tutar.setAlignment(QtCore.Qt.AlignCenter)
        self.line_tutar.setReadOnly(False)
        self.line_tutar.setObjectName("line_tutar")
        self.horizontalLayout_4.addWidget(self.line_tutar)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem25, 5, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem26, 0, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem27, 3, 2, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem28, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_odeme, 1, 1, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem29)
        self.pushButton_yazdir = QtWidgets.QPushButton(Form)
        self.pushButton_yazdir.setStyleSheet("#pushButton_yazdir{\n"
"background-color: rgb(120, 141, 194);\n"
"}\n"
"#pushButton_yazdir:hover {\n"
"   background-color: rgb(87, 102, 142);\n"
"}\n"
"#pushButton_yazdir:pressed {\n"
"    background-color: rgb(62, 74, 102);\n"
"}")
        self.pushButton_yazdir.setObjectName("pushButton_yazdir")
        self.horizontalLayout_19.addWidget(self.pushButton_yazdir)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem30)
        self.gridLayout_3.addLayout(self.horizontalLayout_19, 4, 1, 1, 1)
        self.horizontalLayout_12.addLayout(self.gridLayout_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)
        
        def add_shadow(widget):
            shadow = QGraphicsDropShadowEffect(Form)
            shadow.setBlurRadius(20)
            shadow.setXOffset(0)
            shadow.setYOffset(10)
            shadow.setColor(QtGui.QColor(0, 0, 0, 50))
            widget.setGraphicsEffect(shadow)


        self.frame_bilgi.setStyleSheet("#frame_bilgi{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_odeme.setStyleSheet("#frame_odeme{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        add_shadow(self.frame_bilgi)
        add_shadow(self.frame_odeme)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_tarih.setText(_translate("Form", "16/09/2024"))
        self.label.setText(_translate("Form", "Ödeme Ekranı"))
        self.comboBox_ogr.setItemText(0, _translate("Form", "Öğrenci Seçiniz"))
        self.label_12.setText(_translate("Form", "Son Ödeme Tarihi:"))
        self.label_17.setText(_translate("Form", "Toplam Ödeme:"))
        self.label_7.setText(_translate("Form", "Branşlar"))
        self.label_11.setText(_translate("Form", "Eğitmenler"))
        self.comboBox_egt.setItemText(0, _translate("Form", "Eğitmen Seçiniz"))
        self.label_14.setText(_translate("Form", "İletişim No:"))
        self.label_13.setText(_translate("Form", "Kalan Ders Saati:"))
        self.label_15.setText(_translate("Form", "Geçen Saat:"))
        self.label_9.setText(_translate("Form", "Kayıt Tarihi:"))
        self.label_18.setText(_translate("Form", "Kalan Ödeme:"))
        self.comboBox_egt_2.setItemText(0, _translate("Form", "Paket Seçiniz"))
        self.label_10.setText(_translate("Form", "ÖĞRENCİ ÖDEME BİLGİLERİ"))
        self.label_19.setText(_translate("Form", "Ad Soyad:"))
        self.comboBox_brans.setItemText(0, _translate("Form", "Branş Seçiniz"))
        self.label_16.setText(_translate("Form", "Paket:"))
        self.pushButton.setText(_translate("Form", "KAYDET"))
        self.line_tutar.setPlaceholderText(_translate("Form", "Tutar giriniz...."))
        self.pushButton_yazdir.setText(_translate("Form", "YAZDIR"))