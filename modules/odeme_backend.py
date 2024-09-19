from PyQt5.QtWidgets import QWidget
import gui.odeme as odeme
from core.database import Database
from datetime import datetime
from PyQt5 import QtPrintSupport
from PyQt5 import QtGui
from modules import kasa_backend


class Odeme(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.odeme = odeme.Ui_Form()
            self.odeme_widget = QWidget()
            self.odeme.setupUi(self.odeme_widget)
            
            self.db = Database()
            self.kasa_backend = kasa_backend.Kasa()
            
            self.odeme.label_tarih.setText(datetime.now().strftime('%d/%m/%Y'))
            self.odeme.comboBox_brans.setEnabled(False)
            self.odeme.comboBox_egt.setEnabled(False)
            self.odeme.line_tutar.setEnabled(False)
            self.odeme.comboBox_egt_2.setEnabled(False)
            self.ogrencileri_goster()
            self.odeme.comboBox_ogr.currentTextChanged.connect(self.ogrenci_bilgileri)
            self.odeme.comboBox_brans.currentTextChanged.connect(self.egitmen_goster)
            self.odeme.pushButton.clicked.connect(self.yazdir)
        except Exception as e:
            print(f"Odeme Class hata: {e}")
            
    def sayfa_yenile(self):
        self.odeme.comboBox_ogr.clear()
        self.ogrencileri_goster()
        
    def ogrencileri_goster(self):
        try:
            ogrenciler = self.db.ogrenciler()
            print("ogrenciler2", ogrenciler)
            for ogrenci in ogrenciler:
                self.odeme.comboBox_ogr.addItem(ogrenci[0] + " " + ogrenci[1])
        except Exception as e:
            print(f"ogrencileri_goster hata: {e}")
            
    def ogrenci_bilgileri(self):
        try:
            ogrenci = self.odeme.comboBox_ogr.currentText()
            bilgiler, branslar, egitmenler = self.db.ogrenciBilgi(ogrenci)
            self.odeme.label_ad_soyad.setText(bilgiler[0] + " " + bilgiler[1])
            self.odeme.label_no.setText(bilgiler[2])
            self.odeme.label_kayit_tarih.setText(bilgiler[3])
            
            self.odeme.label_brans1.setText("")
            self.odeme.label_brans2.setText("")
            self.odeme.label_brans3.setText("")
            self.odeme.label_egitmen1.setText("")
            self.odeme.label_egitmen2.setText("")
            self.odeme.label_egitmen3.setText("")
            
            for i, (brans, egitmen) in enumerate(zip(branslar, egitmenler), 1):
                if i <= 3:
                    getattr(self.odeme, f"label_brans{i}").setText(brans[0] if brans else "")
                    getattr(self.odeme, f"label_egitmen{i}").setText(egitmen if egitmen else "")
            
            self.odeme.comboBox_brans.setEnabled(True)
            self.odeme.comboBox_brans.clear()
            for brans in branslar:
                self.odeme.comboBox_brans.addItem(brans[0])
        except Exception as e:
            print(f"ogrenci_bilgileri hata: {e}")

            
    def egitmen_goster(self):
        try:
            self.odeme.comboBox_egt.setEnabled(True)
            self.odeme.comboBox_egt.clear()
            brans = self.odeme.comboBox_brans.currentText()
            ogrenci = self.odeme.comboBox_ogr.currentText()
            egitmenler = self.db.egitmen_brans_ogrenci(brans, ogrenci)
            for egitmen in egitmenler:
                self.odeme.comboBox_egt.addItem(egitmen[0])
            
            self.odeme.comboBox_egt_2.setEnabled(True)
            self.odeme.comboBox_egt_2.clear()
            egitmen = self.odeme.comboBox_egt.currentText()
            paketler = self.db.paketleriGetir(ogrenci, brans, egitmen)
            for paket in paketler:
                self.odeme.comboBox_egt_2.addItem(paket[0])
                
            self.odeme.line_tutar.setEnabled(True)
                
            self.odeme.comboBox_egt.currentTextChanged.connect(self.odeme_bilgileri)
        except Exception as e:
            print(f"egitmen_goster hata: {e}")
            
    def odeme_bilgileri(self):
        try:
            ogrenci = self.odeme.comboBox_ogr.currentText()
            brans = self.odeme.comboBox_brans.currentText()
            egitmen = self.odeme.comboBox_egt.currentText()
            print(ogrenci, brans, egitmen)
            bilgiler = self.db.ogrenciOdemeBilgiAl(ogrenci, brans, egitmen)
            self.odeme.label_gecen_saat.setText(str(bilgiler['gecen_saat']))
            self.odeme.label_kalan_saat.setText(str(bilgiler['kalan_saat']))
            self.odeme.label_paket.setText(bilgiler['paket'])
            self.odeme.label_toplam_odeme.setText(f"{bilgiler['odenen_tutar']:.2f}")
            self.odeme.label_kalan_odeme.setText(f"{bilgiler['kalan_odeme']:.2f}")
            self.odeme.label_son_tarih.setText(bilgiler['odeme_tarihi'])
        except Exception as e:
            print(f"odeme_bilgileri hata: {e}")
    def yazdir(self):
        try:
            ogrenci = self.odeme.comboBox_ogr.currentText()
            brans = self.odeme.comboBox_brans.currentText()
            egitmen = self.odeme.comboBox_egt.currentText()
            tutar = self.odeme.line_tutar.text()
            if ',' in tutar:
                tutar = tutar.replace(',' , '.')
            if tutar:
                if egitmen == "Koray Doğan":
                    self.kasa_backend.ana_kasa += float(tutar)
                self.db.ogrenciOdemeEkle(ogrenci, brans, egitmen, float(tutar))
                bilgiler = self.db.ogrenciOdemeBilgiAl(ogrenci, brans, egitmen)
                self.odeme_bilgileri()
                """html_content = f
                <html lang="tr>
                <head>
                    <style>
                        body {{ font-family: Arial, sans-serif; }}
                        h2 {{ color: #333; }}
                        span {{ color: #333; }}
                        p {{ color: #333; }}
                        .section {{ margin-bottom: 15px; }}
                        .label {{ font-weight: bold; }}
                    </style>
                </head>
                <body>
                    <h2>Ödeme Makbuzu</h2>
                    
                    <div class="section">
                        <h3>Öğrenci Bilgileri:</h3>
                        <p><span class="label">Ad Soyad:</span> {ogrenci}</p>
                        <p><span class="label">Branş:</span> {brans}</p>
                        <p><span class="label">Eğitmen:</span> {egitmen}</p>
                    </div>
                    
                    <div class="section">
                        <h3>Ödeme Bilgileri:</h3>
                        <p><span class="label">Ödeme Tutarı:</span> {tutar} TL</p>
                        <p><span class="label">Ödeme Tarihi:</span> {bilgiler['odeme_tarihi']}</p>
                    </div>
                    
                    <div class="section">
                        <h3>Paket Bilgileri:</h3>
                        <p><span class="label">Paket:</span> {bilgiler['paket']}</p>
                        <p><span class="label">Geçen Saat:</span> {bilgiler['gecen_saat']}</p>
                        <p><span class="label">Kalan Saat:</span> {bilgiler['kalan_saat']}</p>
                    </div>
                    
                    <div class="section">
                        <p><span class="label">Toplam Ödenen:</span> {bilgiler['odenen_tutar']} TL</p>
                        <p><span class="label">Kalan Ödeme:</span> {bilgiler['kalan_odeme']} TL</p>
                    </div>
                </body>
                </html>
                """
                with open('modules/fatura.html', 'r', encoding='utf-8') as file:
                    html_content = file.read()

                html_content = html_content.replace('id="currentDate">', f'id="currentDate">{bilgiler["odeme_tarihi"]}')
                html_content = html_content.replace('id="fullName">', f'id="fullName">{ogrenci}')
                html_content = html_content.replace('id="amountNumeric">', f'id="amountNumeric">{tutar}')
                html_content = html_content.replace('id="brans">', f'id="brans">{brans}')
                
                amount_text = tutar
                html_content = html_content.replace('id="amountText">', f'id="amountText">{amount_text}')
                
                self.invoice_content = html_content
                self.odeme.textEdit.setHtml(html_content)
                if not hasattr(self, 'yazdir_connected'):
                    self.odeme.pushButton_yazdir.clicked.connect(self.yazici)
                    self.yazdir_connected = True
        except Exception as e:
            print(f"yazdir hata: {e}")
        
    def yazici(self):
        try:
            printer = QtPrintSupport.QPrinter()
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
            
            doc = QtGui.QTextDocument()
            doc.setHtml(self.invoice_content)
            
            preview_dialog = QtPrintSupport.QPrintPreviewDialog(printer)
            preview_dialog.paintRequested.connect(lambda p: doc.print_(p))
            
            if preview_dialog.exec_() == QtPrintSupport.QPrintPreviewDialog.Accepted:
                doc.print_(printer)
                print("Yazdırma işlemi başarılı.")
            else:
                print("Yazdırma işlemi iptal edildi.")
                
        except Exception as e:
            print(f"yazici hata: {e}")
