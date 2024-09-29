from managers.cash_manager import Cash
from managers.student_payments_manager import StudentPayments
from managers.teacher_payments_manager import TeachersPayments
class CashGraphService:
    def __init__(self):
        self.cashManager = Cash()
        self.studentPaymentsManager = StudentPayments()
        self.teacherPaymentsManager = TeachersPayments()
    def main_cash_graph(self):
        return self.cashManager.get_total_balance()
    
    def expense_cash_graph(self):
        return self.cashManager.get_expenses()
    
    def students_registration_cash_graph(self):
        amount = 0
        for payment in self.studentPaymentsManager.all_student_payments():
            amount += payment[5]
        return amount
    
    def students_remaining_cash_graph(self):
        amount = 0
        for payment in self.studentPaymentsManager.all_student_payments():
            amount += payment[8]
        return amount
    
    def teacher_remaining_cash_graph(self):
        amount = 0
        for payment in self.teacherPaymentsManager.all_teacher_payments():
            amount += payment[5]
        return amount
