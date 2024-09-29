from PyQt5 import QtPrintSupport, QtGui
from managers.student_payments_manager import StudentPayments
from database.database_manager import DatabaseManager

class PaymentService:
    def __init__(self):
        self.printer = QtPrintSupport.QPrinter()
        self.painter = QtGui.QPainter()
        self.studentPaymentsManager = StudentPayments()
        self.databaseManager = DatabaseManager("database.db")
        
    def invoice_info(self, student_name):
        info_dict = {}
        info = self.studentPaymentsManager.get_student_payments_by_key(student_name=student_name)
        lecture_name = self.databaseManager.get_name_by_id("lectures", info[3])
        for i in info:
            info_dict = {
                "name": student_name,
                "amount": i[9],
                "lecture": lecture_name,
                "payment_date": i[10]
            }
        self.show_invoice(info_dict)
        
        
    def show_invoice(self, info_dict):
        with open('modules/fatura.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
            
        html_content = html_content.replace('id="currentDate">', f'id="currentDate">{info_dict["payment_date"]}')
        html_content = html_content.replace('id="fullName">', f'id="fullName">{info_dict["name"]}')
        html_content = html_content.replace('id="amountNumeric">', f'id="amountNumeric">{info_dict["amount"]}')
        html_content = html_content.replace('id="brans">', f'id="brans">{info_dict["lecture"]}')
        
        amount_text = info_dict["amount"]
        html_content = html_content.replace('id="amountText">', f'id="amountText">{amount_text}')
        
        self.invoice_content = html_content
        self.odeme.textEdit.setHtml(html_content)
        if not hasattr(self, 'printer_connected'):
            self.odeme.pushButton_yazdir.clicked.connect(self.print_invoice)
            self.printer_connected = True
        
    def print_invoice(self):
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