from managers.students_manager import Students
from managers.student_payments_manager import StudentPayments
from managers.cash_manager import Cash

class StudentService:
    def __init__(self):
        self.studentManager = Students()
        self.studentPaymentsManager = StudentPayments()
        self.cashManager = Cash()
        
    def get_student_information(self, **kwargs):
        return self.studentManager.get_student(**kwargs)
    
    def pay_student_payment(self, student_name, amount):
        self.studentPaymentsManager.pay_student_payment(student_name, amount)
        self.cash_add(amount, student_name)
    
    def cash_add(self, amount, student_name):
        self.cashManager.add_income("Öğrenci Ödemesi", amount, f"{student_name} adlı öğrenci ödemesi")