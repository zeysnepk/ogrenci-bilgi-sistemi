from managers.cash_manager import Cash

class TransactionsService:
    def __init__(self):
        self.cashManager = Cash()
        
    def get_transactions(self):
        return self.cashManager.get_last_transactions()