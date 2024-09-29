from managers.cash_manager import Cash

class ExpenseService:
    def __init__(self):
        self.cashManager = Cash()
        
    def add_expense(self, title, amount, description):
        if ',' in amount:
            amount = amount.replace(',', '.')
        self.cashManager.add_expense(title, amount, description)