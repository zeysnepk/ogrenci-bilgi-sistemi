from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QListWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QEvent
import gui.kasa as kasa
from core.database import Database
from datetime import datetime

class Kasa(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.kasa = kasa.Ui_Form()
            self.kasa_widget = QWidget()
            self.kasa.setupUi(self.kasa_widget)
            self.db = Database()
            self.kasa.label_tarih.setText(datetime.now().strftime("%d.%m.%Y"))
            
            self.odeme_grafikleri()
            self.odemeleri_al()
            
            self.original_texts = {
                self.kasa.label_kasa: "Ana Kasa",
                self.kasa.label_gider: "Gider Kasa",
                self.kasa.label_kayit_ucret: "Beklenen Tutar",
                self.kasa.label_kalan_odeme: "Kalan Ödeme",
                self.kasa.label_egt_odeme: "Eğitmen Ödemeleri"
            }
            
            for label, text in self.original_texts.items():
                label.setText(text)
            
            self.kasa.label_kasa.installEventFilter(self)
            self.kasa.label_gider.installEventFilter(self)
            self.kasa.label_kayit_ucret.installEventFilter(self)
            self.kasa.label_kalan_odeme.installEventFilter(self)
            self.kasa.label_egt_odeme.installEventFilter(self)
            
            self.odemeleri_al()
            self.ogrencileri_listele()
            self.egitmenleri_listele()
            
            self.kasa.comboBox_ogr.currentTextChanged.connect(self.ogrenci_secildi)
            self.kasa.comboBox_egt.currentTextChanged.connect(self.egitmen_secildi)
            
            self.kasa.pushButton_gider.clicked.connect(self.gider_ekle)
        except Exception as e:
            print(f"Kasa Class hata: {e}")
    
    def sayfa_yenile(self):
        try:
            self.odeme_grafikleri()
            self.odemeleri_al()
            self.ogrencileri_listele()
            self.egitmenleri_listele()
        except Exception as e:
            print(f"sayfa_yenile hata: {e}")
        
    def ogrenci_secildi(self):
        try:
            ogrenci = self.kasa.comboBox_ogr.currentText()
            bilgiler = self.db.ogrenciGenelOdeme(ogrenci)
            beklenen_tutar = bilgiler['toplam_odenen_tutar'] + bilgiler['kalan_tutar']
            self.kasa.label_beklenen_tutar.setText(f"{beklenen_tutar:.2f} TL")
            self.kasa.label_odenmis_tutar.setText(f"{bilgiler['toplam_odenen_tutar']:.2f} TL")
            self.kasa.label_kalan_tutar.setText(f"{bilgiler['kalan_tutar']:.2f} TL")
            if bilgiler["son_odeme"] > 0:
                if isinstance(bilgiler['odeme_tarihi'], str):
                    tarih, zaman = bilgiler['odeme_tarihi'].split(" ")
                else:
                    tarih = bilgiler['odeme_tarihi'].strftime("%Y-%m-%d")
                    zaman = bilgiler['odeme_tarihi'].strftime("%H:%M:%S")
                self.kasa.label_son_odeme.setText(f"{tarih}\n{zaman}\n{bilgiler['son_odeme']:.2f} TL")
            else:
                self.kasa.label_son_odeme.setText("")
        except Exception as e:
            print(f"ogrenci_secildi hata: {e}")
            
    def egitmen_secildi(self):
        try:
            egitmen = self.kasa.comboBox_egt.currentText()
            bilgiler = self.db.egitmenGenelOdeme(egitmen)
            self.kasa.label_yapilacak_odeme.setText(f"{bilgiler['kalan_odeme']:.2f} TL")
            self.kasa.label_yapilan_odeme.setText(f"{bilgiler['toplam_odenen']:.2f} TL")
            if bilgiler["son_odeme"] > 0:
                if isinstance(bilgiler['odeme_tarihi'], str):
                    tarih, zaman = bilgiler['odeme_tarihi'].split(" ")
                else:
                    tarih = bilgiler['odeme_tarihi'].strftime("%Y-%m-%d")
                    zaman = bilgiler['odeme_tarihi'].strftime("%H:%M:%S")
                self.kasa.label_son_odeme_egt.setText(f"{tarih}\n{zaman}\n{bilgiler['son_odeme']:.2f} TL")
            else:
                self.kasa.label_son_odeme_egt.setText("")
        except Exception as e:
            print(f"egitmen_secildi hata: {e}")
            
    def update_labels(self):
        try:
            self.kasa.label_kasa.setText(self.original_texts[self.kasa.label_kasa])
            self.kasa.label_gider.setText(self.original_texts[self.kasa.label_gider])
            self.kasa.label_kayit_ucret.setText(self.original_texts[self.kasa.label_kayit_ucret])
            self.kasa.label_kalan_odeme.setText(self.original_texts[self.kasa.label_kalan_odeme])
            self.kasa.label_egt_odeme.setText(self.original_texts[self.kasa.label_egt_odeme])
        except Exception as e:
            print(f"update_labels hata: {e}")
        
    def odeme_grafikleri(self):
        try:
            toplam_gider, toplam_kayit, toplam_odenen, toplan_kalan, egitmen_odemeleri, egitmen_odenen = self.db.genelKasa()
            self.ana_kasa = toplam_odenen - egitmen_odenen - toplam_gider
            self.gider_kasa = toplam_gider
            self.beklenen_tutar = toplam_kayit
            self.kalan_odeme = toplan_kalan
            self.egitmen_odemeleri = egitmen_odemeleri
        except Exception as e:
            print(f"odeme_grafikleri hata: {e}")
        
    def odemeleri_al(self):
        try:
            self.kasa.listWidget.clear()
            odemeler = self.db.sonOdemeler()
            for odeme in odemeler:
                print(odeme)
                self.odeme_listesi(odeme[0], odeme[1], odeme[2])
        except Exception as e:
            print(f"odemeleri_al hata: {e}")
        
    def odeme_listesi(self, tarih, miktar, odeme_turu):
        try:
            tarih_str = tarih.strftime('%d.%m.%Y %H:%M:%S')
            odeme_widget = QWidget()
            layout = QHBoxLayout(odeme_widget)
            
            circle_line_layout = QVBoxLayout()
            circle = QLabel("○")
            circle.setFont(QFont("Arial", 18))
            circle_line_layout.addWidget(circle, alignment=Qt.AlignHCenter)
            if odeme_turu != "son":
                line = QLabel("|")
                line.setStyleSheet("color: black; font-size: 14px;")
                line.setFixedHeight(30)
                circle_line_layout.addWidget(line, alignment=Qt.AlignHCenter)

            circle_line_layout.setSpacing(0)
            layout.addLayout(circle_line_layout)

            info_layout = QVBoxLayout()
            
            date_label = QLabel(tarih_str)
            date_label.setStyleSheet("color: gray; font-size: 14px;")
            info_layout.addWidget(date_label)

            if odeme_turu == "gider":
                amount_label = QLabel(f"Gider: -{miktar} TL")
                amount_label.setStyleSheet("color: red; font-weight: bold; font-size: 20px;")
            elif odeme_turu == "ogrenci":
                amount_label = QLabel(f"Öğrenci Ödemesi: +{miktar} TL")
                amount_label.setStyleSheet("color: green; font-weight: bold; font-size: 20px;")
            elif odeme_turu == "egitmen":
                amount_label = QLabel(f"Eğitmen Ödemesi: -{miktar} TL")
                amount_label.setStyleSheet("color: orange; font-weight: bold; font-size: 20px;")
            else:
                amount_label = QLabel(f"Tahsilat: {miktar} TL")
                amount_label.setStyleSheet("font-weight: bold; font-size: 18px;")
            
            info_layout.addWidget(amount_label)

            layout.addLayout(info_layout)
            layout.addStretch()

            list_item = QListWidgetItem(self.kasa.listWidget)
            list_item.setSizeHint(odeme_widget.sizeHint())
            
            self.kasa.listWidget.addItem(list_item)
            self.kasa.listWidget.setItemWidget(list_item, odeme_widget)
        except Exception as e:
            print(f"odeme_listesi hata: {e}")
            
    def eventFilter(self, obj, event):
        try:
            if obj in self.original_texts.keys():
                if event.type() == QEvent.Enter:
                    label_mapping = {
                        self.kasa.label_kasa: self.ana_kasa,
                        self.kasa.label_gider: self.gider_kasa,
                        self.kasa.label_kayit_ucret: self.beklenen_tutar,
                        self.kasa.label_kalan_odeme: self.kalan_odeme,
                        self.kasa.label_egt_odeme: self.egitmen_odemeleri
                    }
                    
                    if obj in label_mapping:
                        value = label_mapping[obj]
                        formatted_value = f"{value:.2f}".replace(".", ",")
                        obj.setText(f"{formatted_value} TL")
                elif event.type() == QEvent.Leave:
                    obj.setText(self.original_texts[obj])
            return super().eventFilter(obj, event)
        except Exception as e:
            print(f"eventFilter hata: {e}")
        
    def ogrencileri_listele(self):
        try:
            self.kasa.comboBox_ogr.clear()
            ogrenciler = self.db.ogrenciler()
            for ogrenci in ogrenciler:
                self.kasa.comboBox_ogr.addItem(f"{ogrenci[0]} {ogrenci[1]}")
        except Exception as e:
            print(f"ogrencileri_listele hata: {e}")
        
    def egitmenleri_listele(self):
        try:
            self.kasa.comboBox_egt.clear()
            egitmenler = self.db.egitmenler()
            for egitmen in egitmenler:
                if egitmen[0] != "Koray Doğan":
                    self.kasa.comboBox_egt.addItem(egitmen[0])
        except Exception as e:
            print(f"egitmenleri_listele hata: {e}")

    def gider_ekle(self):
        try:
            tutar = self.kasa.line_tutar.text()
            aciklama = self.kasa.line_aciklama.text()
            
            if not tutar or not aciklama:
                self.kasa.label_gider_error.setText("Lütfen tutar ve açıklama giriniz.")
                self.kasa.label_gider_error.setStyleSheet("color: red; font-size: 14px;")
                return
            
            if ',' in tutar:
                tutar = tutar.replace(',', '.')
            
            try:
                tutar = float(tutar)
                self.db.giderEkle(tutar, aciklama)
                self.kasa.label_gider_error.setText("Gider başarıyla eklendi")
                self.kasa.label_gider_error.setStyleSheet("color: green; font-size: 14px;")
                self.kasa.line_tutar.clear()
                self.kasa.line_aciklama.clear()
                self.odeme_grafikleri()
                self.odemeleri_al()
            except ValueError:
                self.kasa.label_gider_error.setText("Geçersiz tutar, lütfen sayısal bir değer giriniz")
                self.kasa.label_gider_error.setStyleSheet("color: red; font-size: 14px;")
        except Exception as e:
            print(f"gider_ekle hata: {e}")

