from managers.teachers_manager import Teachers
from managers.teacher_payments_manager import TeacherPayments
from managers.cash_manager import Cash

class TeacherService:
    def __init__(self):
        self.teacherManager = Teachers()
        self.teacherPaymentsManager = TeacherPayments()
        self.cashManager = Cash()
        
    def get_teacher_information(self, **kwargs):
        return self.teacherManager.get_teacher(**kwargs)
    
    def pay_teacher_payment(self, teacher_name, amount):
        self.teacherPaymentsManager.pay_teacher_payment(teacher_name, amount)
        self.cash_add(amount, teacher_name)
    
    def cash_add(self, amount, teacher_name):
        self.cashManager.add_income("Öğretmen Ödemesi", amount, f"{teacher_name} adlı öğretmen ödemesi")