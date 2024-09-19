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

  
   