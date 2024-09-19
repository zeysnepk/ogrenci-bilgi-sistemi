import sqlite3
from datetime import datetime
import pytz
import os

class Database:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, '..', 'databases', 'okul.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON;')
        
    def createTables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT UNIQUE,
            sifre TEXT
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS ogrenciler (
            ogrenci_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            soyad TEXT,
            no TEXT,
            adres TEXT,
            kayit_tarihi DATETIME DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS paketler (
            paket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            paket TEXT,
            fiyat REAL DEFAULT 0
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS branslar (
            brans_id INTEGER PRIMARY KEY AUTOINCREMENT,
            brans TEXT
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS egitmenler (
            egitmen_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            odeme REAL DEFAULT 0,
            toplam_odenen REAL DEFAULT 0,
            kalan_odeme REAL DEFAULT 0,
            son_odeme REAL DEFAULT 0,
            odeme_tarihi DATETIME DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS ogrenci_egitmen (
            ogrenci_id INTEGER,
            egitmen_id INTEGER,
            brans_id INTEGER,
            paket_id INTEGER,
            tutar REAL DEFAULT 0,
            toplam_odenen_tutar REAL DEFAULT 0,
            kalan_tutar REAL DEFAULT 0,
            son_odeme REAL DEFAULT 0,
            odeme_tarihi DATETIME DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
            toplam_saat INTEGER DEFAULT 0,
            kalan_saat INTEGER DEFAULT 0,
            gecen_saat INTEGER DEFAULT 0,
            FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(ogrenci_id),
            FOREIGN KEY (egitmen_id) REFERENCES egitmenler(egitmen_id),
            FOREIGN KEY (brans_id) REFERENCES branslar(brans_id),
            FOREIGN KEY (paket_id) REFERENCES paketler(paket_id)
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS brans_egitmen (
            brans_id INTEGER,
            egitmen_id INTEGER,
            FOREIGN KEY (brans_id) REFERENCES branslar(brans_id),
            FOREIGN KEY (egitmen_id) REFERENCES egitmenler(egitmen_id)
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS brans_paket (
            brans_id INTEGER,
            paket_id INTEGER,
            FOREIGN KEY (brans_id) REFERENCES branslar(brans_id),
            FOREIGN KEY (paket_id) REFERENCES paketler(paket_id)
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS yoklama (
            yoklama_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarih DATE DEFAULT CURRENT_DATE,
            durum TEXT,
            ogrenci_id INTEGER,
            egitmen_id INTEGER,
            brans_id INTEGER,
            FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(ogrenci_id),
            FOREIGN KEY (egitmen_id) REFERENCES egitmenler(egitmen_id),
            FOREIGN KEY (brans_id) REFERENCES branslar(brans_id)
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS giderler (
            gider_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarih DATETIME DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
            miktar REAL DEFAULT 0,
            aciklama TEXT
        )
        ''')
        self.conn.commit()
        
    def adminEkle(self, kullanici_adi, sifre):
        self.cursor.execute('''
        INSERT INTO admin (kullanici_adi, sifre)
        VALUES (?, ?)
        ''', (kullanici_adi, sifre))
        self.conn.commit()
    
    def adminDogrula(self, kullanici_adi):
        self.cursor.execute('''
        SELECT sifre FROM admin WHERE kullanici_adi = ?
        ''', (kullanici_adi,))
        result = self.cursor.fetchone()
        return result[0] if result else None


    def sifreDegistir(self, kullanici_adi, sifre):
        self.cursor.execute('''
        UPDATE admin SET sifre = ? WHERE kullanici_adi = ?
        ''', (sifre, kullanici_adi))
        self.conn.commit()

    def toplamSayilar(self):
        ogrenci_sayisi = self.cursor.execute('''
        SELECT COUNT(*) FROM ogrenciler
        ''').fetchone()[0]
        egitmen_sayisi = self.cursor.execute('''
        SELECT COUNT(*) FROM egitmenler
        ''').fetchone()[0]
        brans_sayisi = self.cursor.execute('''
        SELECT COUNT(DISTINCT brans) FROM branslar
        ''').fetchone()[0]
        return {'ogrenci_sayisi': ogrenci_sayisi, 'egitmen_sayisi': egitmen_sayisi, 'brans_sayisi': brans_sayisi}

        
    def ad_soyad_id_al(self, kisi, tablo, id_column):
        if tablo == "paketler":
            result = self.cursor.execute(f'''
            SELECT {id_column} FROM {tablo}
            WHERE paket = ?
            ''', (kisi,)).fetchone()
        elif tablo == "branslar":
            result = self.cursor.execute(f'''
            SELECT {id_column} FROM {tablo}
            WHERE brans = ?
            ''', (kisi,)).fetchone()
        elif tablo == "egitmenler":
            result = self.cursor.execute(f'''
            SELECT {id_column} FROM {tablo}
            WHERE ad = ?
            ''', (kisi,)).fetchone()
            
        elif len(kisi.split()) == 3:
            ad, ad2, soyad = kisi.split()
            ad = ad + " " + ad2
            result = self.cursor.execute(f'''
            SELECT {id_column} FROM {tablo}
            WHERE ad = ? AND soyad = ?
            ''', (ad, soyad)).fetchone()
        else:
            print("kisi", kisi)
            kisi = kisi.strip()
            ad, soyad = kisi.split()
            result = self.cursor.execute(f'''
            SELECT {id_column} FROM {tablo}
            WHERE ad = ? AND soyad = ?
            ''', (ad, soyad)).fetchone()
        
        if result is None:
            print(f"{tablo} tablosunda {kisi} bulunamadı")
            return None
        return result[0]

    def ogrenciEkle(self, ad, soyad, no, adres, egitmenler, branslar, paketler, tutarlar, saatler):
        self.cursor.execute('''
        INSERT INTO ogrenciler (ad, soyad, no, adres, kayit_tarihi)
        VALUES (?, ?, ?, ?, (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')))
        ''', (ad, soyad, no, adres))
        ogrenci_id = self.cursor.lastrowid
        
        for i in range(len(egitmenler)):
            egitmen_id = self.ad_soyad_id_al(egitmenler[i], "egitmenler", "egitmen_id")
            brans_id = self.ad_soyad_id_al(branslar[i], "branslar", "brans_id")
            paket_id = self.ad_soyad_id_al(paketler[i], "paketler", "paket_id")
            tutar = float(tutarlar[i])
            
            if egitmen_id is None or brans_id is None or paket_id is None:
                raise ValueError(f"Invalid foreign key for egitmen: {egitmenler[i]}, brans: {branslar[i]}, or paket: {paketler[i]}")
            
            self.cursor.execute('''
            INSERT INTO ogrenci_egitmen (ogrenci_id, egitmen_id, brans_id, paket_id, tutar, kalan_tutar, toplam_saat, kalan_saat)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (ogrenci_id, egitmen_id, brans_id, paket_id, tutar, tutar, saatler[i], saatler[i]))
            
            self.cursor.execute('''
            INSERT INTO brans_egitmen (brans_id, egitmen_id)
            VALUES (?, ?)
            ''', (brans_id, egitmen_id))
            
            self.cursor.execute('''
            INSERT INTO brans_paket (brans_id, paket_id)
            VALUES (?, ?)
            ''', (brans_id, paket_id))
            
            self.cursor.execute('''
            UPDATE egitmenler 
            SET odeme = odeme + ?, kalan_odeme = kalan_odeme + ?
            WHERE egitmen_id = ? AND ad != "Koray Doğan"
            ''', (tutar * 0.4, tutar * 0.4, egitmen_id))
            
        self.conn.commit()

    def branslar(self):
        self.cursor.execute('''
        SELECT brans FROM branslar
        ''')
        branslar = self.cursor.fetchall()
        print("branslar", branslar)
        return branslar
        
    def egitmenler(self):
        self.cursor.execute('''
        SELECT ad FROM egitmenler
        ''')
        egitmenler = self.cursor.fetchall()
        return egitmenler

    def brans_paketler(self, brans):
        self.cursor.execute('''
        SELECT DISTINCT p.paket
        FROM paketler p
        JOIN brans_paket bp ON p.paket_id = bp.paket_id
        JOIN branslar b ON bp.brans_id = b.brans_id
        WHERE b.brans = ?
        ''', (brans,))
        result = self.cursor.fetchall()
        return [paket[0] for paket in result]
    
    def egitmen_brans(self, brans):
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        self.cursor.execute('''
        SELECT DISTINCT e.ad FROM egitmenler e
        JOIN brans_egitmen be ON e.egitmen_id = be.egitmen_id
        WHERE be.brans_id = ?
        ''', (brans_id,))
        egitmenler = self.cursor.fetchall()
        return egitmenler
    
    def ogrenciler_egitmen_brans(self, egitmen, brans):
        print("egt", egitmen, brans)
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        print("ogr",egitmen_id, brans_id)
        self.cursor.execute('''
        SELECT o.ad, o.soyad FROM ogrenciler o 
        JOIN ogrenci_egitmen oe ON o.ogrenci_id = oe.ogrenci_id 
        WHERE oe.egitmen_id = ? AND oe.brans_id = ?
        ''', (egitmen_id, brans_id))
        ogrenciler = self.cursor.fetchall()
        return ogrenciler
    
    def devamsizlikBilgi(self, ogrenci, egitmen, brans):
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        devamsizlik_bilgileri = {'Gelmedi': 0, 'Geldi': 0, 'Telafi': 0, 'İptal': 0}
        yoklamalar = self.cursor.execute('''
        SELECT durum FROM yoklama WHERE ogrenci_id = ? AND egitmen_id = ? AND brans_id = ?
        ''', (ogrenci_id, egitmen_id, brans_id)).fetchall()
        for yoklama in yoklamalar:
            durum = yoklama[0]
            if durum in devamsizlik_bilgileri:
                devamsizlik_bilgileri[durum] += 1
        return devamsizlik_bilgileri
        
    def yoklamaEkle(self, ogrenci, egitmen, ogrenci_durum, brans):
        try:
            ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
            egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
            brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
            
            if ogrenci_id is None or egitmen_id is None or brans_id is None:
                print(f"Error: Invalid foreign key. Ogrenci: {ogrenci_id}, Egitmen: {egitmen_id}, Brans: {brans_id}")
                return False

            self.cursor.execute('''
            SELECT COUNT(*) FROM yoklama 
            WHERE ogrenci_id = ? AND egitmen_id = ? AND brans_id = ? AND tarih = CURRENT_DATE
            ''', (ogrenci_id, egitmen_id, brans_id))
            
            if self.cursor.fetchone()[0] == 0:
                self.cursor.execute('''
                INSERT INTO yoklama (ogrenci_id, egitmen_id, brans_id, durum, tarih)
                VALUES (?, ?, ?, ?, CURRENT_DATE)
                ''', (ogrenci_id, egitmen_id, brans_id, ogrenci_durum))
                if ogrenci_durum == "Geldi":
                    self.cursor.execute('''
                    UPDATE ogrenci_egitmen 
                    SET kalan_saat = kalan_saat - 1, 
                        gecen_saat = gecen_saat + 1
                    WHERE ogrenci_id = ? AND egitmen_id = ? AND brans_id = ?
                    ''', (ogrenci_id, egitmen_id, brans_id))
            else:
                self.cursor.execute('''
                UPDATE yoklama 
                SET durum = ?
                WHERE ogrenci_id = ? AND egitmen_id = ? AND brans_id = ? AND tarih = CURRENT_DATE
                ''', (ogrenci_durum, ogrenci_id, egitmen_id, brans_id))
            
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"SQLite Integrity Error: {e}")
            self.conn.rollback()
            return False
        except Exception as e:
            print(f"Error in yoklamaEkle: {e}")
            self.conn.rollback()
            return False
            
    def ogrenciler(self):
        self.cursor.execute('''
        SELECT ad, soyad FROM ogrenciler
        ''')
        ogrenciler = self.cursor.fetchall()
        return ogrenciler
        
    def ogrenciBilgi(self, ogrenci):
        print("ogrenci", ogrenci)
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        bilgiler = self.cursor.execute('''
        SELECT ad, soyad, no, kayit_tarihi FROM ogrenciler WHERE ogrenci_id = ?
        ''', (ogrenci_id,)).fetchone()
        print(bilgiler)
        branslar = self.cursor.execute('''
        SELECT b.brans FROM ogrenci_egitmen oe
        JOIN branslar b ON oe.brans_id = b.brans_id
        WHERE oe.ogrenci_id = ?
        ''', (ogrenci_id,)).fetchall()
        print(branslar)
        egitmenler = []
        for brans in branslar:
            brans_id = self.ad_soyad_id_al(brans[0], "branslar", "brans_id")
            egitmen = self.cursor.execute('''
            SELECT e.ad
            FROM egitmenler e
            JOIN ogrenci_egitmen oe ON e.egitmen_id = oe.egitmen_id
            WHERE oe.ogrenci_id = ? AND oe.brans_id = ?
            ''', (ogrenci_id, brans_id)).fetchone()
            egitmenler.append(egitmen[0] if egitmen else None)
        print(egitmenler)
        return bilgiler, branslar, egitmenler
        
    def egitmen_brans_ogrenci(self, brans, ogrenci):
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        self.cursor.execute('''
        SELECT e.ad FROM egitmenler e 
        JOIN ogrenci_egitmen oe ON e.egitmen_id = oe.egitmen_id
        WHERE oe.brans_id = ? AND oe.ogrenci_id = ?
        ''', (brans_id, ogrenci_id))
        egitmenler = self.cursor.fetchall()
        return egitmenler
    
    def paketleriGetir(self, ogrenci, brans, egitmen):
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        self.cursor.execute('''
        SELECT DISTINCT p.paket 
        FROM ogrenci_egitmen oe
        JOIN paketler p ON oe.paket_id = p.paket_id
        WHERE oe.ogrenci_id = ? AND oe.egitmen_id = ? AND oe.brans_id = ?
        ''', (ogrenci_id, egitmen_id, brans_id))
        paketler = self.cursor.fetchall()
        return paketler
        
    def ogrenciOdemeBilgiAl(self, ogrenci, brans, egitmen):
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        
        odeme_bilgileri = self.cursor.execute('''
        SELECT toplam_odenen_tutar, kalan_tutar, gecen_saat, kalan_saat, paket_id
        FROM ogrenci_egitmen
        WHERE ogrenci_id = ? AND egitmen_id = ? AND brans_id = ?
        ''', (ogrenci_id, egitmen_id, brans_id)).fetchone()
        
        paket = self.cursor.execute('''
        SELECT paket FROM paketler WHERE paket_id = ?
        ''', (odeme_bilgileri[4],)).fetchone()
        
        odeme_tarihi = self.cursor.execute('''
        SELECT odeme_tarihi FROM ogrenci_egitmen
        WHERE ogrenci_id = ? AND egitmen_id = ? AND brans_id = ? AND son_odeme > 0 
        ''', (ogrenci_id, egitmen_id, brans_id)).fetchone()
        odeme_tarihi = odeme_tarihi[0] if odeme_tarihi else None
        return {
            'odenen_tutar': odeme_bilgileri[0],
            'kalan_odeme': odeme_bilgileri[1],
            'gecen_saat': odeme_bilgileri[2],
            'kalan_saat': odeme_bilgileri[3],
            'paket': paket[0],
            'odeme_tarihi': odeme_tarihi
        }

    def ogrenciOdemeEkle(self, ogrenci, brans, egitmen, tutar):
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        self.cursor.execute('''
        UPDATE ogrenci_egitmen
        SET toplam_odenen_tutar = toplam_odenen_tutar + ?,
            kalan_tutar = kalan_tutar - ?,
            son_odeme = ?,
            odeme_tarihi = (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
        WHERE ogrenci_id = ? AND egitmen_id = ? AND brans_id = ?
        ''', (tutar, tutar, tutar, ogrenci_id, egitmen_id, brans_id))
        self.conn.commit()
            
    def egitmenler(self):
        self.cursor.execute('''
        SELECT ad FROM egitmenler
        ''')
        egitmenler = self.cursor.fetchall()
        return egitmenler
            
    def egitmenBilgi(self, egitmen_adi):
        egitmen_id = self.ad_soyad_id_al(egitmen_adi, "egitmenler", "egitmen_id")
        branslar = self.cursor.execute('''
        SELECT b.brans FROM branslar b
        JOIN brans_egitmen be ON b.brans_id = be.brans_id
        WHERE be.egitmen_id = ?
        ''', (egitmen_id,)).fetchall()
        print("branslar", branslar)
        result = self.cursor.execute('''
        SELECT COUNT(DISTINCT o.ogrenci_id) AS ogrenci_sayisi, 
        SUM(oe.toplam_saat) AS toplam_saat, 
        e.kalan_odeme FROM 
        ogrenciler o
        JOIN ogrenci_egitmen oe ON o.ogrenci_id = oe.ogrenci_id
        JOIN egitmenler e ON e.egitmen_id = oe.egitmen_id
        WHERE e.egitmen_id = ?
        ''', (egitmen_id,)).fetchone()
        print("kalan_odeme", result[2])
        if result:
            return {
                'ogrenci_sayisi': result[0],
                'branslar': branslar,
                'toplam_saat': result[1] or 0,
                'kalan_tutar': result[2] or 0
            }
        else:
            return {
                'ogrenci_sayisi': 0,
                'brans': '',
                'toplam_saat': 0,
                'kalan_tutar': 0
            }
        
    def yoklamaBilgi(self, egitmen, tarih):
        yoklama_bilgileri = {'ogrenci_ad':[], 'ogrenci_soyad':[], 'durum':[]}
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        
        yoklamalar = self.cursor.execute('''
        SELECT o.ad, o.soyad, y.durum
        FROM yoklama y
        JOIN ogrenciler o ON y.ogrenci_id = o.ogrenci_id
        WHERE y.egitmen_id = ? AND y.tarih = ?
        ''', (egitmen_id, tarih)).fetchall()
        
        for yoklama in yoklamalar:
            ad, soyad, durum = yoklama
            yoklama_bilgileri['ogrenci_ad'].append(ad)
            yoklama_bilgileri['ogrenci_soyad'].append(soyad)
            yoklama_bilgileri['durum'].append(durum)
        
        return yoklama_bilgileri
     
    def gunluk_yoklama_kontrol(self, tarih, egitmen, brans):
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        self.cursor.execute('''
        SELECT COUNT(*) FROM yoklama 
        WHERE tarih = ? AND egitmen_id = ? AND brans_id = ?
        ''', (tarih, egitmen_id, brans_id))
        result = self.cursor.fetchone()
        print(result)
        if result:
            mevcut_yoklama = self.cursor.execute('''
            SELECT o.ogrenci_id, o.ad, o.soyad, y.durum FROM yoklama y
            JOIN ogrenciler o ON y.ogrenci_id = o.ogrenci_id
            WHERE y.tarih = ? AND y.egitmen_id = ? AND y.brans_id = ?
            ''', (tarih, egitmen_id, brans_id)).fetchall()
            print(mevcut_yoklama)
            return mevcut_yoklama
        else:
            return False
    
    def egitmenOdeme(self, egitmen_adi, tutar):
        egitmen_id = self.ad_soyad_id_al(egitmen_adi, "egitmenler", "egitmen_id")
        
        self.cursor.execute('''
        UPDATE egitmenler 
        SET toplam_odenen = toplam_odenen + ?,
            kalan_odeme = kalan_odeme - ?,
            son_odeme = ?,
            odeme_tarihi = (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
        WHERE egitmen_id = ?
        ''', (tutar, tutar, tutar, egitmen_id))
        
        self.conn.commit()
            
    def genelKasa(self):
        giderler = self.cursor.execute('''
        SELECT SUM(miktar) FROM giderler
        ''').fetchone()[0] or 0

        odemeler = self.cursor.execute('''
        SELECT SUM(tutar), SUM(toplam_odenen_tutar), SUM(kalan_tutar)
        FROM ogrenci_egitmen
        ''').fetchone() or 0
        toplam_kayit, toplam_odenen, toplam_kalan = odemeler
        toplam_kayit = toplam_kayit or 0
        toplam_odenen = toplam_odenen or 0
        toplam_kalan = toplam_kalan or 0

        egitmen_odeme = self.cursor.execute('''
        SELECT SUM(kalan_odeme), SUM(toplam_odenen) FROM egitmenler
        ''').fetchone() or 0
        egitmen_odemeler = egitmen_odeme[0] or 0
        egitmen_odenen = egitmen_odeme[1] or 0
        return giderler, toplam_kayit, toplam_odenen, toplam_kalan, egitmen_odemeler, egitmen_odenen

    def sonOdemeler(self):
        all_payments = []
        local_tz = pytz.timezone('Europe/Istanbul') 

        gider_odemeleri = self.cursor.execute('''
        SELECT tarih, miktar FROM giderler WHERE miktar > 0
        ORDER BY tarih DESC 
        LIMIT 10
        ''').fetchall()
        all_payments.extend([(self.utc_to_local(date, local_tz), amount, 'gider') for date, amount in gider_odemeleri])
        
        ogrenci_odemeleri = self.cursor.execute('''
        SELECT odeme_tarihi, son_odeme FROM ogrenci_egitmen WHERE son_odeme > 0
        ORDER BY odeme_tarihi DESC
        LIMIT 10
        ''').fetchall()
        all_payments.extend([(self.utc_to_local(date, local_tz), amount, 'ogrenci') for date, amount in ogrenci_odemeleri])
        
        egitmen_odemeleri = self.cursor.execute('''
        SELECT odeme_tarihi, son_odeme FROM egitmenler WHERE son_odeme > 0
        ORDER BY odeme_tarihi DESC
        LIMIT 10
        ''').fetchall()
        all_payments.extend([(self.utc_to_local(date, local_tz), amount, 'egitmen') for date, amount in egitmen_odemeleri])
    
        sorted_payments = sorted(all_payments, key=lambda x: x[0], reverse=True)
        
        return sorted_payments[:10] 

    def utc_to_local(self, utc_dt, local_tz):
        if utc_dt is None:
            return None
        utc_dt = datetime.strptime(utc_dt, '%Y-%m-%d %H:%M:%S')
        utc_dt = pytz.utc.localize(utc_dt)
        return utc_dt.astimezone(local_tz)
        
    def ogrenciGenelOdeme(self, ogrenci):
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        self.cursor.execute('''
        SELECT SUM(toplam_odenen_tutar) as toplam_odenen_tutar,
                SUM(kalan_tutar) as kalan_tutar,
                MAX(son_odeme) as son_odeme,
                MAX(odeme_tarihi) as odeme_tarihi
        FROM ogrenci_egitmen
        WHERE ogrenci_id = ?
        ''', (ogrenci_id,))
        result = self.cursor.fetchone()
        return {
            'toplam_odenen_tutar': result[0] or 0,
            'kalan_tutar': result[1] or 0,
            'son_odeme': result[2] or 0,
            'odeme_tarihi': datetime.strptime(result[3], '%Y-%m-%d %H:%M:%S') if result[3] else None
        }

    def egitmenGenelOdeme(self, egitmen):
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        self.cursor.execute('''
        SELECT odeme,
                toplam_odenen,
                kalan_odeme,
                son_odeme,
                odeme_tarihi
        FROM egitmenler
        WHERE egitmen_id = ?
        ''', (egitmen_id,))
        result = self.cursor.fetchone()
        
        return {
            'odeme': result[0] or 0,
            'toplam_odenen': result[1] or 0,
            'kalan_odeme': result[2] or 0,
            'son_odeme': result[3] or 0,
            'odeme_tarihi': result[4]
        }


    def giderEkle(self, miktar, aciklama):
        self.cursor.execute('''
        INSERT INTO giderler (miktar, aciklama)
        VALUES (?, ?)
        ''', (miktar, aciklama))
        self.conn.commit()
 
    def bransEkle(self, brans):
        self.cursor.execute('''
        INSERT INTO branslar (brans)
        VALUES (?)
        ''', (brans,))
        
        self.conn.commit()
        
    def egitmenEkle(self, ad):
        self.cursor.execute('''
        INSERT INTO egitmenler (ad)
        VALUES (?)
        ''', (ad,))
        self.conn.commit()
        
    def paketEkle(self, paket, fiyat):
        self.cursor.execute('''
        INSERT INTO paketler (paket, fiyat)
        VALUES (?, ?)
        ''', (paket, fiyat))
        self.conn.commit()
        
    def bransPaketEkle(self, brans, paket):
        brans_id = self.ad_soyad_id_al(brans, "branslar", "brans_id")
        paket_id = self.ad_soyad_id_al(paket[0], "paketler", "paket_id")
        self.cursor.execute('''
        INSERT INTO brans_paket (brans_id, paket_id)
        VALUES (?, ?)
        ''', (brans_id, paket_id))
        self.conn.commit()
            
    def ogrenciGuncelle(self, ogrenci, ad, soyad, no, adres, egitmenler, branslar, paketler, tutarlar, saatler):
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        self.cursor.execute('''
        UPDATE ogrenciler 
        SET ad = ?, soyad = ?, no = ?, adres = ?
        WHERE ogrenci_id = ?
        ''', (ad, soyad, no, adres, ogrenci_id))
        self.cursor.execute('DELETE FROM ogrenci_egitmen WHERE ogrenci_id = ?', (ogrenci_id,))
        for i in range(len(egitmenler)):
            egitmen_id = self.ad_soyad_id_al(egitmenler[i], "egitmenler", "egitmen_id")
            self.cursor.execute('''
            INSERT INTO ogrenci_egitmen (ogrenci_id, egitmen_id, paket, tutar, saat, kalan_saat, gecen_saat, kalan_odeme, odenen_tutar)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (ogrenci_id, egitmen_id, paketler[i], tutarlar[i], saatler[i], saatler[i], 0, tutarlar[i], 0))
            self.cursor.execute('''
            UPDATE egitmenler 
            SET odeme = odeme + ?
            WHERE egitmen_id = ?
            ''', (tutarlar[i] * 0.4, egitmen_id))
        self.cursor.execute('DELETE FROM ogrenci_brans WHERE ogrenci_id = ?', (ogrenci_id,))
        for brans in branslar:
            self.cursor.execute('''
            INSERT INTO ogrenci_brans (ogrenci_id, brans)
            VALUES (?, ?)
            ''', (ogrenci_id, brans))
        self.conn.commit()
        
    def yoklamaGuncelle(self, ogrenci, egitmen, ogrenci_durum, tarih):
        ogrenci_id = self.ad_soyad_id_al(ogrenci, "ogrenciler", "ogrenci_id")
        egitmen_id = self.ad_soyad_id_al(egitmen, "egitmenler", "egitmen_id")
        self.cursor.execute('''
        UPDATE yoklama SET durum = ? 
        WHERE ogrenci_id = ? AND egitmen_id = ? AND tarih = ?
        ''', (ogrenci_durum, ogrenci_id, egitmen_id, tarih))
        self.conn.commit()
        
    def ogrencileriGetir(self):
        self.cursor.execute('''
        SELECT ad, soyad FROM ogrenciler
        ''')
        ogrenciler = self.cursor.fetchall()
        return ogrenciler

    def drop_tables(self):
        tables = ['admin', 'ogrenciler', 'paketler', 'branslar', 'egitmenler', 'ogrenci_egitmen', 'yoklama', 'giderler']
        for table in tables:
            self.cursor.execute(f'DROP TABLE IF EXISTS {table}')
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
        
if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.createTables()
   
    branslar = []
    
    muzik_branslar = ["Piyano", "Keman", "Çello", "Yan Flüt", "Gitar", "Bateri", "Bağlama", "Şan", "Konservatuar Hazırlık", "Klarnet", "Saksafon", "Ud", "Kanun"]
    muzik_paketler = [["Grup Dersi: 2500 TL", 2500], ["Özel Ders: 1500 TL", 1500], ["Zeynep Kaplan: 5000 TL", 5000], ["Yoğun Program: 3500 TL", 3500]]
    dans_branslar = ["BALE", "MODERN DANS", "LATİN DANSLARI", "DÜĞÜN DANSI", "ORYANTAL", "HIP HOP", "ZUMBA"]
    yaratici_branslar = ["RESİM", "YARATICI DRAMA", "HEYKEL"]
    dans_yaratici_paketler = [
        ["Dans Paketi: 1500 TL", 1500],
        ["Resim Paketi: 1200 TL", 1200],
        ["Yaratıcı Drama Paketi: 1300 TL", 1300]
    ]
    
    branslar.extend(muzik_branslar)
    branslar.extend(dans_branslar)
    branslar.extend(yaratici_branslar)
    
    for brans in branslar:
        db.bransEkle(brans)
    
    egitmenler = [
        ("Ahmet Yılmaz"),
        ("Mehmet Kaya"),
        ("Ayşe Demir"),
        ("Fatma Çelik"),
        ("Mustafa Öztürk"),
        ("Zeynep Kaplan"),
        ("Ali Şahin"),
        ("Hüseyin Arslan"),
        ("Emine Yıldız"),
        ("Hatice Özdemir"),
        ("Hasan Koç"),
        ("Merve Aksoy"),
        ("Emre Güneş"),
        ("Selin Yılmaz"),
    ]
    
    for egitmen in egitmenler:
        db.egitmenEkle(egitmen)
        
    paketler = []
    
    for paket in muzik_paketler:
        db.paketEkle(paket[0], paket[1])
    
    for paket in dans_yaratici_paketler:
        db.paketEkle(paket[0], paket[1])
    
    for muzik in muzik_branslar:
        for paket in muzik_paketler:
            db.bransPaketEkle(muzik, paket)
    
    for dans in dans_branslar:
        for paket in dans_yaratici_paketler:
            db.bransPaketEkle(dans, paket)
    
    for resim in yaratici_branslar:
        for paket in dans_yaratici_paketler:
            db.bransPaketEkle(resim, paket)

    db.close_connection()
    
            
        
            
        
    
        
        
        
        
        
        
        