from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1665, 983)
        Form.setStyleSheet("""
#Form {
    background-color: rgb(222, 221, 220);
}

QLabel {
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
QTreeWidget {
    background-color: #FFFFFF;
    color: #A6493A;
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    border: none;
    outline: none;
}

QTreeWidget::item {
    padding: 10px;
    border-bottom: 1px solid #E0E0E0;
}

QTreeWidget::item:selected {
    background-color: #F0F0F0;
    color: #A6493A;
}

QTreeWidget::item:hover {
    background-color: #F5F5F5;
}

QHeaderView::section {
    background-color: rgb(87, 103, 142);
    color: #FFFFFF;
    padding: 5px;
    border: none;
}
""")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setContentsMargins(70, 70, 70, 70)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
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
        self.label_date = QtWidgets.QLabel(Form)
        self.label_date.setObjectName("label_date")
        self.label_date.setText("03/12/2002")
        self.label_date.setStyleSheet("font-size: 22pt; color: rgb(87, 103, 142);")
        self.verticalLayout_8.addWidget(self.label_date)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.comboBox_brans = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_brans.sizePolicy().hasHeightForWidth())
        self.comboBox_brans.setSizePolicy(sizePolicy)
        self.comboBox_brans.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBox_brans.setObjectName("comboBox_brans")
        self.verticalLayout_9.addWidget(self.comboBox_brans)
        self.comboBox_egitmen = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_egitmen.sizePolicy().hasHeightForWidth())
        self.comboBox_egitmen.setSizePolicy(sizePolicy)
        self.comboBox_egitmen.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_egitmen.setObjectName("comboBox_egitmen")
        self.verticalLayout_9.addWidget(self.comboBox_egitmen)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem5)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.headerItem().setFont(6, font)
        
        self.verticalLayout.addWidget(self.treeWidget)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("QPushButton{\n"
"            \n"
"    background-color: rgb(120, 141, 194);\n"
"        }\n"
"QPushButton:hover {\n"
"            \n"
"    \n"
"    background-color: rgb(87, 102, 142);\n"
"        }\n"
"QPushButton:pressed {\n"
"            \n"
"    background-color: rgb(62, 74, 102);\n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgb(253, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem8)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font: 20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setMinimumSize(QtCore.QSize(280, 280))
        self.widget.setMaximumSize(QtCore.QSize(280, 280))
        self.widget.setStyleSheet("#widget{\n"
"\n"
"border-radius: 140px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.0394089 rgba(93, 164, 44, 200), stop:0.187192 rgba(93, 164, 44, 200), stop:0.188 rgba(185, 51, 34, 208), stop:0.527094 rgba(185, 51, 34, 208), stop:0.528 rgba(239, 129, 61, 210), stop:0.753695 rgba(239, 129, 61, 210), stop:0.755 rgb(120, 141, 194));\n"
"}")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(50, 50, 180, 180))
        self.widget_2.setMinimumSize(QtCore.QSize(180, 180))
        self.widget_2.setMaximumSize(QtCore.QSize(180, 180))
        self.widget_2.setStyleSheet("#widget_2{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 90px\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ogr = QtWidgets.QLabel(self.widget_2)
        self.label_ogr.setMinimumSize(QtCore.QSize(0, 0))
        self.label_ogr.setMaximumSize(QtCore.QSize(3454, 343243))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        self.label_ogr.setFont(font)
        self.label_ogr.setStyleSheet("#label_ogr{\n"
"    color: rgb(166, 73, 58);\n"
"    font: 600 25pt \"Century Gothic\" ;\n"
"}\n"
"")
        self.label_ogr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ogr.setWordWrap(True)
        self.label_ogr.setObjectName("label_ogr")
        self.verticalLayout_3.addWidget(self.label_ogr)
        self.horizontalLayout_2.addWidget(self.widget)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem13)
        self.label_gelmedi = QtWidgets.QLabel(self.frame)
        self.label_gelmedi.setStyleSheet("#label_gelmedi{\n"
"    color: rgb(198, 89, 75);\n"
"    font: 26pt \"Century Gothic\";\n"
"}\n"
"")
        self.label_gelmedi.setObjectName("label_gelmedi")
        self.verticalLayout_2.addWidget(self.label_gelmedi)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_geldi = QtWidgets.QLabel(self.frame)
        self.label_geldi.setStyleSheet("#label_geldi{\n"
"    \n"
"    color: rgb(128, 184, 90);\n"
"    font: 26pt \"Century Gothic\";\n"
"}\n"
"")
        self.label_geldi.setObjectName("label_geldi")
        self.verticalLayout_2.addWidget(self.label_geldi)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_telafi = QtWidgets.QLabel(self.frame)
        self.label_telafi.setStyleSheet("#label_telafi{\n"
"    color: rgb(242, 151, 95);\n"
"    font: 26pt \"Century Gothic\";\n"
"}\n"
"")
        self.label_telafi.setObjectName("label_telafi")
        self.verticalLayout_2.addWidget(self.label_telafi)
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_iptal = QtWidgets.QLabel(self.frame)
        self.label_iptal.setStyleSheet("#label_iptal{\n"
"    color: rgb(120, 141, 194);\n"
"    font: 26pt \"Century Gothic\";\n"
"}\n"
"")
        self.label_iptal.setObjectName("label_iptal")
        self.verticalLayout_2.addWidget(self.label_iptal)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem14)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem16)
        self.verticalLayout_5.setStretch(4, 2)
        self.verticalLayout_4.addWidget(self.frame)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem17)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem18)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        
        def add_shadow(widget):
            shadow = QGraphicsDropShadowEffect(Form)
            shadow.setBlurRadius(20)
            shadow.setXOffset(0)
            shadow.setYOffset(10)
            shadow.setColor(QtGui.QColor(0, 0, 0, 50))
            widget.setGraphicsEffect(shadow)
        
        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgb(253, 255, 255);\n"
"    border-radius: 10px;\n"
"}")

        add_shadow(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Öğrenci Yoklama Ekranı"))
        self.label_3.setText(_translate("Form", "Branş:"))
        self.label_5.setText(_translate("Form", "Eğitmen:"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "No"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Ad"))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Soyad"))
        self.treeWidget.headerItem().setText(3, _translate("Form", "Geldi"))
        self.treeWidget.headerItem().setText(4, _translate("Form", "Gelmedi"))
        self.treeWidget.headerItem().setText(5, _translate("Form", "Telafi"))
        self.treeWidget.headerItem().setText(6, _translate("Form", "İptal Edildi"))

        self.pushButton.setText(_translate("Form", "KAYDET"))
        self.label_2.setText(_translate("Form", "Lütfen devamsızlık bilgisini görmek istediğiniz öğrenciyi seçiniz"))
        self.label_ogr.setText(_translate("Form", "AD\n"
"SOYAD"))
        self.label_gelmedi.setText(_translate("Form", "- 0 gün gelmedi"))
        self.label_geldi.setText(_translate("Form", "- 0 gün geldi"))
        self.label_telafi.setText(_translate("Form", "- 0 gün telafi"))
        self.label_iptal.setText(_translate("Form", "- 0 gün iptal"))
