from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import QDate


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1192, 912)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(222, 221, 220);\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 24pt \'Century Gothic\';\n"
"    color: rgb(163, 72, 50)\n"
"}\n"
"QComboBox {\n"
"    padding: 8px 8px;\n"
"    font: 16pt \'Century Gothic\';\n"
"    height: 20px;\n"
"    width: 30px;\n"
"    background-color: rgba(223, 128, 112, 80);\n"
"    color: rgb(88, 87, 87, 201);\n"
"    combobox-popup: 0;\n"
"}\n"
"\n"
"QComboBox::focus {\n"
"    background-color: rgba(223, 128, 112, 80);\n"
"    border: 2px solid #A34832;\n"
"    color: rgb(88, 87, 87, 201);\n"
"}\n"
"\n"
"QDateEdit {\n"
"    font: 16pt \'Century Gothic\';\n"
"    padding: 2px 10px;\n"
"    color: rgb(88, 87, 87, 201);\n"
"    background-color: rgba(223, 128, 112, 80);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    min-width: 150px;\n"
"    height: 40px;\n"
"}\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #A34832;\n"
"}\n"
"QDateEdit::down-arrow {\n"
"    color: black;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"QDateEdit:focus {\n"
"    border: 2px solid #A34832;\n"
"}\n"
"QCalendarWidget QToolButton {\n"
"    height: 30px;\n"
"    width: 100px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    icon-size: 20px, 20px;\n"
"    background-color: #A34832;\n"
"}\n"
"QCalendarWidget QMenu {\n"
"    width: 150px;\n"
"    left: 20px;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    background-color: #A34832;\n"
"}\n"
"QCalendarWidget QSpinBox {\n"
"    width: 100px;\n"
"    font-size:14px;\n"
"    color: white;\n"
"    background-color: #A34832;\n"
"    selection-background-color: #A34832;\n"
"    selection-color: white;\n"
"}\n"
"QCalendarWidget QSpinBox::up-button { subcontrol-origin: border; subcontrol-position: top right; width:20px; }\n"
"QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right; width:20px;}\n"
"QCalendarWidget QSpinBox::up-arrow { width:20px; height:20px; }\n"
"QCalendarWidget QSpinBox::down-arrow { width:20px; height:20px; }\n"
"\n"
"QPushButton{\n"
"            background-color: #A34832;\n"
"            border: none;\n"
"            border-radius: 12px;\n"
"            color: white;\n"
"            padding: 12px 24px;\n"
"            font: 18px \"Century Gothic\";\n"
"            font-weight: bold;\n"
"        }\n"
"QPushButton:hover {\n"
"            background-color: #8B3A28;\n"
"        }\n"
"QPushButton:pressed {\n"
"            background-color: #732E22;\n"
"        }\n"
"\n"
"QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"    gridline-color: #E0E0E0;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #E0E0E0;\n"
"    color: #333333;\n"
"    font-family: 'Poppins', sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(223, 128, 112, 50);\n"
"    color: #333333;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(223, 128, 112, 20);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F5F5F5;\n"
"    color: #A6493A;\n"
"    font-family: 'Poppins', sans-serif;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-bottom: 2px solid #E0E0E0;\n"
"}\n"
"\n"
"QTableWidget QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #F0F0F0;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background: #CCCCCC;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
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
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(70, 70, 70, 70)
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem2, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        self.frame_bilgi = QtWidgets.QFrame(Form)
        self.frame_bilgi.setStyleSheet("#frame_bilgi{\n"
"    background-color: rgb(253, 255, 255);\n"
"}\n"
"QLabel{\n"
"    color: rgb(223, 128, 112);\n"
"    font: 24pt \"Baskerville\" bold;\n"
"}")
        self.frame_bilgi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bilgi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bilgi.setObjectName("frame_bilgi")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_bilgi)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_2 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_2.setStyleSheet("#label_2{\n"
"    color: rgb(163, 72, 50);\n"
"    font:500 26pt;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_14.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.comboBox = QtWidgets.QComboBox(self.frame_bilgi)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.horizontalLayout_13.addWidget(self.comboBox)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.horizontalLayout_13.setStretch(0, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_ad_soyad = QtWidgets.QLabel(self.frame_bilgi)
        self.label_ad_soyad.setStyleSheet("#label_ad_soyad{\n"
"color: rgb(88, 87, 87);\n"
"font: 700 26pt \"Century Gothic\";\n"
"}")
        self.label_ad_soyad.setObjectName("label_ad_soyad")
        self.horizontalLayout_11.addWidget(self.label_ad_soyad)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.line_2 = QtWidgets.QFrame(self.frame_bilgi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_12.addWidget(self.line_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_13.setStyleSheet("#label_13{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.label_ogr_sayi = QtWidgets.QLabel(self.frame_bilgi)
        self.label_ogr_sayi.setStyleSheet("#label_ogr_sayi{\n"
"font: 20pt;\n"
"}")
        self.label_ogr_sayi.setText("")
        self.label_ogr_sayi.setObjectName("label_ogr_sayi")
        self.horizontalLayout_8.addWidget(self.label_ogr_sayi)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_16.setStyleSheet("#label_16{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.label_saat = QtWidgets.QLabel(self.frame_bilgi)
        self.label_saat.setStyleSheet("#label_saat{\n"
"font: 20pt;\n"
"}")
        self.label_saat.setText("")
        self.label_saat.setObjectName("label_saat")
        self.horizontalLayout_15.addWidget(self.label_saat)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.horizontalLayout_15.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_14.setStyleSheet("#label_14{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.label_odeme = QtWidgets.QLabel(self.frame_bilgi)
        self.label_odeme.setStyleSheet("#label_odeme{\n"
"font: 20pt;\n"
"}")
        self.label_odeme.setText("")
        self.label_odeme.setObjectName("label_odeme")
        self.horizontalLayout_9.addWidget(self.label_odeme)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.horizontalLayout_9.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.frame_bilgi)
        self.label_15.setStyleSheet("#label_15{\n"
"    color: rgb(163, 72, 50);\n"
"}")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.label_brans = QtWidgets.QLabel(self.frame_bilgi)
        self.label_brans.setStyleSheet("#label_brans{\n"
"font: 20pt;\n"
"}")
        self.label_brans.setText("")
        self.label_brans.setObjectName("label_brans")
        self.horizontalLayout_10.addWidget(self.label_brans)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.horizontalLayout_10.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem15)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(10, 1)
        self.gridLayout.addWidget(self.frame_bilgi, 1, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 1, 0, 1, 1)
        self.frame_odeme = QtWidgets.QFrame(Form)
        self.frame_odeme.setStyleSheet("#frame_odeme{\n"
"    background-color: rgb(253, 255, 255);\n"
"}")
        self.frame_odeme.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_odeme.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_odeme.setObjectName("frame_odeme")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_odeme)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem17)
        self.pushButton = QtWidgets.QPushButton(self.frame_odeme)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem18)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_tutar = QtWidgets.QLineEdit(self.frame_odeme)
        self.line_tutar.setText("")
        self.line_tutar.setAlignment(QtCore.Qt.AlignCenter)
        self.line_tutar.setReadOnly(False)
        self.line_tutar.setObjectName("line_tutar")
        self.horizontalLayout_4.addWidget(self.line_tutar)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem19, 5, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem20, 0, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 3, 2, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem22, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_odeme, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem23)
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        self.horizontalLayout.addWidget(self.dateEdit)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem24)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setShowGrid(False)  # Hide grid lines
        self.tableWidget.setAlternatingRowColors(True)  # Alternate row colors
        self.tableWidget.verticalHeader().setVisible(False)  # Hide vertical header
        self.tableWidget.horizontalHeader().setStretchLastSection(True)  # Stretch last column
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)  # Adjust size to contents
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Make table read-only
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Stretch columns to fit content
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 2)  # Set stretch factor for frame_odeme
        self.horizontalLayout_2.setStretch(1, 1)  # Set stretch factor for tableWidget
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.label_tarih = QtWidgets.QLabel(Form)
        self.label_tarih.setStyleSheet("#label_tarih{\n"
"color: rgb(87, 103, 142);\n"
"font: 22pt \"Century Gothic\";\n"
"}")
        self.label_tarih.setObjectName("label_tarih")
        self.gridLayout_2.addWidget(self.label_tarih, 1, 0, 1, 1)
        
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
        self.label.setText(_translate("Form", "Eğitmen Bilgi Ekranı"))
        self.label_2.setText(_translate("Form", "Lütfen bir eğitmen seçiniz"))
        self.label_ad_soyad.setText(_translate("Form", "AD - SOYAD"))
        self.label_13.setText(_translate("Form", "Öğrenci Sayısı:"))
        self.label_16.setText(_translate("Form", "Toplam Saat:"))
        self.label_14.setText(_translate("Form", "Kalan Ödeme:"))
        self.label_15.setText(_translate("Form", "Branş:"))
        self.pushButton.setText(_translate("Form", "ÖDE"))
        self.line_tutar.setPlaceholderText(_translate("Form", "Tutar giriniz...."))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "02/12/2022"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ad"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Soyad"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Yoklama Durumu"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_tarih.setText(_translate("Form", "16/09/2024"))
