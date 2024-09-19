from PyQt5.QtWidgets import QWidget, QTableWidgetItem
import gui.egitmen2 as egitmen
from core.database import Database
from datetime import datetime


class Egitmen(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.db = Database()
            self.egitmen = egitmen.Ui_Form()
            self.egitmen_widget = QWidget()
            self.egitmen.setupUi(self.egitmen_widget)
            
            self.egitmen.label_tarih.setText(datetime.now().strftime("%d/%m/%Y"))
            
            self.egitmenleri_goster()
            
            self.egitmen.comboBox.currentTextChanged.connect(self.ogretmen_bilgileri)
            self.egitmen.dateEdit.dateChanged.connect(self.yoklama_goster)
            self.egitmen.pushButton.clicked.connect(self.odeme_yap)
        except Exception as e:
            print(f"Egitmen Class hata: {e}")
            
    def sayfa_yenile(self):
        try:
            self.egitmenleri_goster()
        except Exception as e:
            print(f"sayfa_yenile hata: {e}")
    
    def egitmenleri_goster(self):
        try:
            self.egitmen.comboBox.clear()
            egitmenler = self.db.egitmenler()
            for egitmen in egitmenler:
                if egitmen[0] != "Koray Doğan":
                    self.egitmen.comboBox.addItem(egitmen[0])
        except Exception as e:
            print(f"egitmenleri_goster hata: {e}")
    
    def ogretmen_bilgileri(self):
        try:
            self.egitmen.line_tutar.setEnabled(True)
            self.egitmen.line_tutar.clear()
            egitmen_adi = self.egitmen.comboBox.currentText()
            egitmen_bilgileri = self.db.egitmenBilgi(egitmen_adi)
            branslar = [brans[0] for brans in egitmen_bilgileri['branslar']]
            if egitmen_bilgileri is not None:
                self.egitmen.label_ad_soyad.setText(egitmen_adi)
                self.egitmen.label_ogr_sayi.setText(str(egitmen_bilgileri['ogrenci_sayisi']))
                self.egitmen.label_brans.setText(", ".join(branslar))
                self.egitmen.label_saat.setText(str(egitmen_bilgileri['toplam_saat']))
                self.egitmen.label_odeme.setText(str(egitmen_bilgileri['kalan_tutar']))
                self.yoklama_goster()
            else:
                print(f"Eğitmen bilgileri alınamadı: {egitmen_adi}")
                self.egitmen.label_ad_soyad.setText(egitmen_adi)
                self.egitmen.label_ogr_sayi.setText("0")
                self.egitmen.label_brans.setText("")
                self.egitmen.label_saat.setText("0")
                self.egitmen.label_odeme.setText("0")
        except Exception as e:
            print(f"ogretmen_bilgileri hata: {e}")
    
    def yoklama_goster(self):
        try:
            egitmen_adi = self.egitmen.comboBox.currentText()
            self.egitmen.tableWidget.clearContents()
            self.egitmen.tableWidget.setRowCount(0)
            tarih = self.egitmen.dateEdit.date().toString("dd.MM.yyyy")
            try:
                tarih_obj = datetime.strptime(tarih, "%d.%m.%Y")
                tarih_formatted = tarih_obj.strftime("%Y-%m-%d")
                yoklama_bilgileri = self.db.yoklamaBilgi(egitmen_adi, tarih_formatted)
                
                for i, (ad, soyad, durum) in enumerate(zip(yoklama_bilgileri['ogrenci_ad'], 
                                                        yoklama_bilgileri['ogrenci_soyad'], 
                                                        yoklama_bilgileri['durum'])):
                    row_position = self.egitmen.tableWidget.rowCount()
                    self.egitmen.tableWidget.insertRow(row_position)
                    self.egitmen.tableWidget.setItem(row_position, 0, QTableWidgetItem(ad))
                    self.egitmen.tableWidget.setItem(row_position, 1, QTableWidgetItem(soyad))
                    self.egitmen.tableWidget.setItem(row_position, 2, QTableWidgetItem(durum))
                    self.egitmen.tableWidget.setVerticalHeaderItem(row_position, QTableWidgetItem(tarih))
            
            except Exception as e:
                print(f"Error in yoklama_goster: {e}")
        except Exception as e:
            print(f"yoklama_goster hata: {e}")
            
    def odeme_yap(self):
        try:
            egitmen_adi = self.egitmen.comboBox.currentText()
            if ',' in self.egitmen.line_tutar.text():
                tutar = float(self.egitmen.line_tutar.text().replace(',', '.'))
            else:
                tutar = float(self.egitmen.line_tutar.text())
            self.db.egitmenOdeme(egitmen_adi, tutar)
            self.ogretmen_bilgileri()
        except Exception as e:
            print(f"odeme_yap hata: {e}")
        
                