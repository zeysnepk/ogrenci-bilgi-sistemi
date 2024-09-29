from managers.admin_manager import Admin

class LoginService:
    def __init__(self):
        self.adminManager = Admin()
        
    def login(self, username, password):
        if self.adminManager.login(username, password):
            return True
        else:
            return False