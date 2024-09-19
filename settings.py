import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'core'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'gui'))

def adminEkle():
    from core.admin import Admin
    admin = Admin()
    kullanici_adi = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    admin.adminEkle(kullanici_adi, sifre)

adminEkle()