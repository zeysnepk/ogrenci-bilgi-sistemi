# Sanat Okulu Projesi

Sanat Okulu Projesi, sanat eğitimi alanında veya isterseniz kodu düzenleyerek kendi alanınızdaki branşlarla öğrencilere ve öğretmenlere çeşitli araçlar ve kaynaklar sunmayı amaçlayan bir uygulamadır. Proje, eğitimi desteklemek için geliştirilmiş bir dizi özellik sunar ve branşlar, eğitmenler, öğrenciler, ödemeler, giderler vs konusunda kolay bir kullanım sağlar. Böylelikle çok rahat bir şekilde işlerinizi gerçekleştirebilirsiniz.

## Özellikler

- **Giriş Ekranı**: Veritabanında sadece sizin girebileceğiniz şifrelenmiş bir şekilde tutulur ve ayrıca birden fazla giriş ekleyebilirsiniz.
- **Kayıt Ekranı**: Öğrencileri ilgili branş, eğitmen ve branşlara özel paket tipleri ve saat ile kaydetmenizi sağlar ve ayrıca öğrenci birden fazla branş veya eğitmen seçebilir.
- **Yoklama Ekranı**: Kaydedilen öğrencileri seçilen branş ve eğitmenle birlikte günlük olarak listeler ve eğer gün içinde yoklama alınmışsa bunu gösterir. Yan bölümde öğrenci seçilerek öğrenci hakkında devamsızlık bilgilerini grafiksel olarak gösterir.
- **Ödeme Ekranı**: İlgili öğrencinin ödeme bilgilerini ayrıntılı bir şekilde gösterip ödeme yapıldığında makbuzu istenilen formatla kaydedebilir veya bir yazıcıyla çıkarabilir.
- **Eğitmen Bilgi Ekranı**: İlgili eğitmenin okul tarafından yapılacak ödemelerini görebilir ve ayrıca öğrencilerinin yoklama bilgilerinin aşağıya açılır bir tarihle listeler.
- **Kasa Ekranı**: Ana Kasa(öğrenci ödemeleri - giderler), Gider Kasa, Beklenen Tutar(kayıt sırasında talep edilen tutar), Kalan Ödeme(öğrencilerin toplam ödemesi gereken tutar), Eğitmen Ödemeleri(eğitmenlere yapılacak toplam ödeme) şeklinde grafikle yansıtılır ve son tahsilatları gösterir.

## Ekran Görüntüleri

![Screenshot 2024-09-19 at 23 12 47](https://github.com/user-attachments/assets/9900ec45-47f6-4476-a3fe-1fd2a2d3ea7b)
![Screenshot 2024-09-19 at 21 51 33](https://github.com/user-attachments/assets/c30fe45d-d77c-45fe-a6d1-0cbab85dee88)
![Screenshot 2024-09-19 at 21 51 56](https://github.com/user-attachments/assets/ae067343-b15c-4122-98bb-c2718d437e49)
![Screenshot 2024-09-19 at 21 52 08](https://github.com/user-attachments/assets/c70f96d0-4062-43c2-9178-841fc23ab998)
![Screenshot 2024-09-19 at 21 52 15](https://github.com/user-attachments/assets/44c1c56d-3fb0-4011-9dfc-ab00bc4f80cf)
![Screenshot 2024-09-19 at 21 52 34](https://github.com/user-attachments/assets/67f53148-a23d-4047-8c4e-0b1497cb0b4f)
![Screenshot 2024-09-19 at 22 06 27](https://github.com/user-attachments/assets/45397610-f2f0-4fd2-b64a-2446fde79fb4)


## Kurulum

1. **Depoyu Klonlayın**:

      ```zsh
   git clone https://github.com/zeysnepk/ogrenci-bilgi-sistemi.git

2. **Sanal Bağımlılıkları Listeleyin**:

      ```zsh
   pip freeze > requirements.txt

3. **Gerekli Paketleri Yükleyin**:

      ```zsh
   pip install -r requirements.txt

4. **Veritabanını Yapılandırın**:

      ```zsh
   python3 core/database.py

5. **Kullanıcı Adı ve Şifre Oluşturun**:

      ```zsh
   python3 settings.py

6. **Çalıştırın**:

      ```zsh
   python3 main.py

  
## Özelleştirme

Kodlarla değişiklik yaparak renk, veriler, veritabanı işlemleri, görseller vs özelleştirebilirsiniz.

  
   
