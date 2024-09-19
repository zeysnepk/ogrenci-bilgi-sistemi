from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
import gui.kayit_2 as kayit_2
from core.database import Database

class Kayit(QWidget):

    def __init__(self):
        super().__init__()
        try:
            self.db = Database()
            self.kayit = kayit_2.Ui_Form()
            self.kayit_widget = QWidget()
            self.kayit.setupUi(self.kayit_widget)
            
            self.branslar = []
            self.egitmenler = []
            self.paketler = []
            self.tutarlar = []
            self.saatler = []
            
            self.secenekleri_goster()

            self.kayit.combo_brans1.currentTextChanged.connect(self.brans_degisti)
            
            self.kayit.pushButton_devam.clicked.connect(self.devam_et)
            self.kayit.pushButton.clicked.connect(self.kayit_tamamla)
            self.kayit.pushButton_iptal.clicked.connect(self.iptal)
            
            
        except Exception as e:
            print(f"Kayit Class hata: {e}")
    
    def sayfa_yenile(self):
        self.secenekleri_goster()
        
    def iptal(self):
        try:
            self.kayit.line_ad.clear()
            self.kayit.line_soyad.clear()
            self.kayit.line_no.clear()
            self.kayit.text_adres.clear()
            self.temizle()
            self.branslar.clear()
            self.egitmenler.clear()
            self.paketler.clear()
            self.saatler.clear()
            self.tutarlar.clear()
            self.kayit.label_registration_confirm.setText("Bilgiler sıfırlandı")
            self.kayit.label_registration_confirm.setStyleSheet("color: red; font: 16pt \"Century Gothic\";")
        except Exception as e:
            print(f"iptal hata: {e}")
        
    def secenekleri_goster(self):
        try:
            self.kayit.combo_brans1.clear()
            self.kayit.combo_egt1.clear()
        
            branslar = self.db.branslar()
            for brans in branslar:
                self.kayit.combo_brans1.addItem(brans[0])
            
            egitmenler = self.db.egitmenler()
            for egitmen in egitmenler:
                self.kayit.combo_egt1.addItem(egitmen[0])
            
            self.paketleri_guncelle()
        except Exception as e:
            print(f"secenekleri goster hata: {e}")

    def brans_degisti(self):
        self.paketleri_guncelle()

    def paketleri_guncelle(self):
        try:
            self.kayit.combo_paket.clear()
            paketler = self.db.brans_paketler(self.kayit.combo_brans1.currentText())
            print("paketler", paketler)
            for paket in paketler:
                self.kayit.combo_paket.addItem(paket)
        except Exception as e:
            print(f"paketleri guncelle hata: {e}")

    def giris_kontrol(self):
        try:
            brans = self.kayit.combo_brans1.currentText()
            egitmen = self.kayit.combo_egt1.currentText()
            paket = self.kayit.combo_paket.currentText()
            saat = self.kayit.spinBox.value()
            tutar = self.kayit.line_tutar.text()

            if not all([brans, egitmen, paket, tutar]) or saat < 0:
                self.kayit.label_registration_confirm.setText("Lütfen tüm alanları doldurunuz")
                self.kayit.label_registration_confirm.setStyleSheet("color: red; font: 16pt \"Century Gothic\";")
                return None

            if ',' in tutar:
                tutar = tutar.replace(',', '.')
            try:
                tutar = float(tutar)
                self.branslar.append(brans)
                self.egitmenler.append(egitmen)
                self.paketler.append(paket)
                self.saatler.append(saat)
                self.tutarlar.append(tutar)
                return True
            except ValueError:
                self.kayit.label_registration_confirm.setText("Lütfen tutarı doğru giriniz")
                self.kayit.label_registration_confirm.setStyleSheet("color: red;")
                return None
        except Exception as e:
            print(f"giris kontrol hata: {e}")
        
    def temizle(self):
        try:
            self.kayit.combo_brans1.setCurrentIndex(0)
            self.kayit.combo_egt1.setCurrentIndex(0)
            self.kayit.combo_paket.setCurrentIndex(0)
            self.kayit.spinBox.setValue(0)
            self.kayit.line_tutar.clear()
        except Exception as e:
            print(f"temizle hata: {e}")
        
    def devam_et(self):
        try:
            if self.giris_kontrol() is None:
                return
            self.temizle()
        except Exception as e:
            print(f"devam et hata: {e}")
        
    def kayit_tamamla(self):
        try:
            if self.giris_kontrol() is None:
                return
            self.ad = self.kayit.line_ad.text()
            self.soyad = self.kayit.line_soyad.text()
            self.no = self.kayit.line_no.text()
            self.adres = self.kayit.text_adres.toPlainText()   
            self.db.ogrenciEkle(self.ad, self.soyad, self.no, self.adres, self.egitmenler, self.branslar, self.paketler, self.tutarlar, self.saatler)
            
            self.kayit.line_ad.clear()
            self.kayit.line_soyad.clear()
            self.kayit.line_no.clear()
            self.kayit.text_adres.clear()
            self.temizle()
            
            self.branslar.clear()
            self.egitmenler.clear()
            self.paketler.clear()
            self.saatler.clear()
            self.tutarlar.clear()
            
            self.kayit.label_registration_confirm.setText("Kayıt başarılı")
            self.kayit.label_registration_confirm.setStyleSheet("color: green; font: 16pt \"Century Gothic\";")
            QTimer.singleShot(2000, lambda: self.kayit.label_registration_confirm.setText(""))
        except Exception as e:
            print(f"kayit tamamla hata: {e}")


