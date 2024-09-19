from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from core.admin import Admin
import gui.yoklama2 as yoklama
from core.database import Database
from datetime import datetime

class Yoklama(QWidget):
    def __init__(self):
        super().__init__()
        self.admin = Admin()
        self.yoklama = yoklama.Ui_Form()
        self.yoklama_widget = QWidget()
        self.yoklama.setupUi(self.yoklama_widget)
    
        self.db = Database()
        
        self.yoklama.label_date.setText(datetime.now().strftime('%d/%m/%Y'))
        self.yoklama.comboBox_brans.addItem("Branş seçiniz") 
        self.yoklama.comboBox_brans.setCurrentIndex(0)
        self.secenek_goster()
        self.ogrencileri_goster()
        self.yoklama.comboBox_brans.currentTextChanged.connect(self.egitmen_goster)
        self.yoklama.comboBox_egitmen.currentTextChanged.connect(self.yoklama_kontrol)
        self.yoklama.comboBox.currentTextChanged.connect(self.devamsizlik_bilgi)
        self.yoklama.pushButton.clicked.connect(self.kaydet)
        
    def sayfa_yenile(self):
        self.yoklama_kontrol
        self.yoklama.comboBox.clear()
        
    def secenek_goster(self):
        try:
            branslar = self.db.branslar()
            for brans in branslar:
                self.yoklama.comboBox_brans.addItem(brans[0])
        except Exception as e:
            print(f"secenek_goster hata: {e}")

            
    def egitmen_goster(self, brans):
        try:
            self.yoklama.comboBox.clear()
            self.yoklama.comboBox_egitmen.clear()
            self.yoklama.treeWidget.clear()
            brans = self.yoklama.comboBox_brans.currentText()
            egitmenler = self.db.egitmen_brans(brans)
            for egitmen in egitmenler:
                self.yoklama.comboBox_egitmen.addItem(egitmen[0])
        except Exception as e:
            print(f"egitmen_goster hata: {e}")

    def ogrencileri_goster(self):
        try:
            self.yoklama.comboBox.clear() 
            self.yoklama.treeWidget.clear()  
            egitmen = self.yoklama.comboBox_egitmen.currentText()
            brans = self.yoklama.comboBox_brans.currentText()
            tarih = datetime.now().strftime('%Y-%m-%d')
            print("ggt",egitmen, brans)
            ogrenciler = self.db.ogrenciler_egitmen_brans(egitmen, brans)
            print(ogrenciler)
            for i, ogrenci in enumerate(ogrenciler, start=1):
                self.yoklama.comboBox.addItem(f"{ogrenci[0]} {ogrenci[1]}")
                
                item = QtWidgets.QTreeWidgetItem(self.yoklama.treeWidget)
                item.setText(0, str(i))  
                ad_soyad = ogrenci
                item.setText(1, ad_soyad[0])  
                item.setText(2, ad_soyad[1] if len(ad_soyad) > 1 else "") 
                
                for i in range(self.yoklama.treeWidget.topLevelItemCount()):
                    button_group = QtWidgets.QButtonGroup(self.yoklama.treeWidget)  
                    button_group.setExclusive(True)  
                    
                    for j in range(3, 7):  
                            checkbox = QtWidgets.QCheckBox()
                            self.yoklama.treeWidget.setItemWidget(self.yoklama.treeWidget.topLevelItem(i), j, checkbox)
                            button_group.addButton(checkbox) 
            
            for i in range(self.yoklama.treeWidget.columnCount()):
                self.yoklama.treeWidget.resizeColumnToContents(i)
        except Exception as e:
            print(f"ogrencileri_goster hata: {e}")
            
    def devamsizlik_bilgi(self, ogrenci):
        try:
            print("devamsizlik_bilgi", ogrenci, self.yoklama.comboBox_egitmen.currentText())
            devamsizlik_bilgileri = self.db.devamsizlikBilgi(ogrenci, self.yoklama.comboBox_egitmen.currentText(), self.yoklama.comboBox_brans.currentText())
            print("devamsizlik_bilgileri", devamsizlik_bilgileri)
            self.yoklama.label_gelmedi.setText(f"- {devamsizlik_bilgileri.get('Gelmedi', 0)} gün gelmedi")
            self.yoklama.label_geldi.setText(f"- {devamsizlik_bilgileri.get('Geldi', 0)} gün geldi")
            self.yoklama.label_telafi.setText(f"- {devamsizlik_bilgileri.get('Telafi', 0)} gün telafi")
            self.yoklama.label_iptal.setText(f"- {devamsizlik_bilgileri.get('İptal', 0)} gün iptal")
        
            self.grafik_guncelle(devamsizlik_bilgileri)
        except Exception as e:
            print("Hata:", e)

    def grafik_guncelle(self, devamsizlik_bilgileri):
        try:
            toplam_gun = devamsizlik_bilgileri.get('Geldi', 0) + devamsizlik_bilgileri.get('Gelmedi', 0) + devamsizlik_bilgileri.get('Telafi', 0) + devamsizlik_bilgileri.get('İptal', 0)
            if toplam_gun > 0:
                geldi_yuzde = devamsizlik_bilgileri.get('Geldi', 0) / toplam_gun
                gelmedi_yuzde = devamsizlik_bilgileri.get('Gelmedi', 0) / toplam_gun
                telafi_yuzde = devamsizlik_bilgileri.get('Telafi', 0) / toplam_gun
                iptal_yuzde = devamsizlik_bilgileri.get('İptal', 0) / toplam_gun

                geldi_stop = geldi_yuzde
                gelmedi_stop = geldi_stop + gelmedi_yuzde
                telafi_stop = gelmedi_stop + telafi_yuzde
                iptal_stop = 1.0 
                if (gelmedi_yuzde == 0): gelmedi_stop = geldi_stop + 0.0002
                if (telafi_yuzde == 0): telafi_stop = gelmedi_stop + 0.0002
                if (iptal_yuzde == 0): iptal_stop = telafi_stop + 0.0002
                
                print(geldi_yuzde, gelmedi_yuzde, telafi_yuzde, iptal_yuzde)
                print(geldi_stop, gelmedi_stop, telafi_stop, iptal_stop)

                gradient_style = f"""
                #widget {{
                    border-radius: 140px;
                    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0,
                    stop:0 rgba(93, 164, 44, 200),
                    stop:{geldi_stop - 0.0001} rgba(93, 164, 44, 200),
                    stop:{geldi_stop} rgba(185, 51, 34, 208),
                    stop:{gelmedi_stop - 0.0001} rgba(185, 51, 34, 208),
                    stop:{gelmedi_stop} rgba(239, 129, 61, 210),
                    stop:{telafi_stop - 0.0001} rgba(239, 129, 61, 210),
                    stop:{telafi_stop } rgb(120, 141, 194),
                    stop:1 rgb(120, 141, 194));
                }}
                """
                self.yoklama.widget.setStyleSheet(gradient_style)
        except Exception as e:
            print(f"grafik_guncelle hata: {e}")

            
    def kaydet(self):
        try:
            tarih = datetime.now().strftime('%Y-%m-%d')
            egitmen = self.yoklama.comboBox_egitmen.currentText()
            brans = self.yoklama.comboBox_brans.currentText()
            for i in range(self.yoklama.treeWidget.topLevelItemCount()):
                item = self.yoklama.treeWidget.topLevelItem(i)
                ogrenci_adi = item.text(1) + " " + item.text(2)
                ogrenci_id = self.db.ad_soyad_id_al(ogrenci_adi, "ogrenciler", "ogrenci_id")
                ogrenci_durum = "Bilinmiyor"
                for j in range(3, 7):
                    checkbox = self.yoklama.treeWidget.itemWidget(item, j)
                    if isinstance(checkbox, QtWidgets.QCheckBox) and checkbox.isChecked():
                        if j == 3:
                            ogrenci_durum = "Geldi"
                        elif j == 4:
                            ogrenci_durum = "Gelmedi"
                        elif j == 5:
                            ogrenci_durum = "Telafi"
                        elif j == 6:
                            ogrenci_durum = "İptal"
                        break
                self.db.yoklamaEkle(ogrenci_adi, egitmen, ogrenci_durum, brans)
            ogrenci = self.yoklama.comboBox.currentText()
            self.devamsizlik_bilgi(ogrenci)
            self.yoklama_kontrol() 
        except Exception as e:
            print(f"kaydet hata: {e}")

        
    def yoklama_kontrol(self):
        try:
            self.yoklama.comboBox.clear()
            self.yoklama.treeWidget.clear()
            tarih = datetime.now().strftime('%Y-%m-%d')
            egitmen = self.yoklama.comboBox_egitmen.currentText()
            brans = self.yoklama.comboBox_brans.currentText()
            mevcut_yoklama = self.db.gunluk_yoklama_kontrol(tarih, egitmen, brans)
            if mevcut_yoklama:
                print("mevcut_yoklama:", mevcut_yoklama)
                print(len(mevcut_yoklama))
                self.yoklama.treeWidget.clear() 
                for ogrenci in mevcut_yoklama:
                    item = QtWidgets.QTreeWidgetItem(self.yoklama.treeWidget)
                    item.setText(0, str(ogrenci[0]))
                    item.setText(1, ogrenci[1])
                    item.setText(2, ogrenci[2])
                    
                    button_group = QtWidgets.QButtonGroup(self.yoklama.treeWidget)
                    button_group.setExclusive(True)
                    
                    for j in range(3, 7):
                        checkbox = QtWidgets.QCheckBox()
                        self.yoklama.treeWidget.setItemWidget(item, j, checkbox)
                        button_group.addButton(checkbox)
                        
                        durum_map = {3: "Geldi", 4: "Gelmedi", 5: "Telafi", 6: "İptal"}
                        if j in durum_map and ogrenci[3] == durum_map[j]:
                            checkbox.setChecked(True)
                print("ogr_yok")
                ogrenciler = self.db.ogrenciler_egitmen_brans(egitmen, self.yoklama.comboBox_brans.currentText())
                print("ogr_yok2", ogrenciler)
                for i, ogrenci in enumerate(ogrenciler, start=1):
                    self.yoklama.comboBox.addItem(f"{ogrenci[0]} {ogrenci[1]}")
                self.yoklama.treeWidget.resizeColumnToContents(0)
                self.yoklama.treeWidget.resizeColumnToContents(1)
                self.yoklama.treeWidget.resizeColumnToContents(2)
                return True
            else:
                print("mevcut_yoklamal  yok")
                self.ogrencileri_goster()
        except Exception as e:
            print(f"yoklama_kontrol hata: {e}")
            
            
            
            
            
            
            
            
