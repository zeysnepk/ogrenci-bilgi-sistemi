import bcrypt
from .database import Database

class Admin:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.conn.cursor()
        self.conn = self.db.conn

    def adminEkle(self, kullanici_adi, sifre):
        sifre_hash = bcrypt.hashpw(sifre.encode('utf-8'), bcrypt.gensalt())
        self.db.adminEkle(kullanici_adi, sifre_hash)

    def adminDogrula(self, kullanici_adi, sifre):
        sifre_hash = self.db.adminDogrula(kullanici_adi)
        if sifre_hash is None:
            return False
        if isinstance(sifre_hash, str):
            sifre_hash = sifre_hash.encode('utf-8')
        elif isinstance(sifre_hash, int):
            sifre_hash = str(sifre_hash).encode('utf-8')
        return bcrypt.checkpw(sifre.encode('utf-8'), sifre_hash)
    
    def sifreDegistir(self, kullanici_adi, sifre):
        sifre_hash = bcrypt.hashpw(sifre.encode('utf-8'), bcrypt.gensalt())
        self.db.sifreDegistir(kullanici_adi, sifre_hash)

