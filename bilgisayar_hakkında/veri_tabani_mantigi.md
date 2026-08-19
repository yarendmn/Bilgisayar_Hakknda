# VERİ TABANI MANTIĞI (SQL TEMELLERİ)
## Relational Database nedir?
* Verileri satırlar ve sütunlardan oluşan tablolar şeklinde depolayan ve bu tablolar arasında mantıksal ilişkiler kuran bir veri düzenleme sistemidir. 
* Düzenli veri gerektiren alanlarda sıklıkla kullanılır.
* Genelde kullanılan dil SQL'dir.
## Primary Key, Foreign Key
**Primary Key** her tablodaki kaydın benzersiz bir tanımlayıcıdır. Her tabloda sadece bir primary key olabilirken boş(null) değerler kabul edilmez.

*Örneğin* kullanıcı bilgilerini içeren bir tabloda kullanıcı kimlik bilgisi (UserID gibi) her kullanıcı için bir primary key olabilir.

**Forgein Key** ise tablodaki bir alanın başka bir tablodaki Primary Key e referans vermesidir. Veritabanı içindeki  referans bütünlüğünü koruyarak iki tablodaki kayıtlar arasında etkili bir bağlantı kurar.

**Örneğin** siparişlerin tutulduğu bir veritabanında müşterilerin bilgisinin bulunduğu tablodaki müşteri Id leri primary key iken müşteri bilgileri ise referans edilen foreign key dir.

## SELECT - JOIN - GROUP BY NEDİR ?

SELECT, JOIN ve GROUP BY, veritabanlarından veri çekmek ve raporlamak için kullanılan temel SQL komutlarıdır.

SELECT istenen sütunları seçer,

JOIN farklı tabloları birbirine bağlar,

GROUP BY ise aynı değerleri bir araya getirip özet hesaplar yapmayı sağlar

SELECT Nedir?
* Veritabanından veri almak için kullanılır.Hangi sütunları görmek istediğinizi söylersiniz
* Örnek: SELECT ad, soyad FROM ogrenci;

JOIN Nedir?
* Birden çok tabloyu ortak bir alana göre birleştirir.İlişkili tablolardan tek seferde veri almayı sağlar.
* Türleri: INNER JOIN, LEFT JOIN, RIGHT JOIN.Örnek: Öğrenci ve notlar tablosunu birleştirir.

GROUP BY Nedir?
* Verileri belirli bir sütuna göre gruplara ayırır.COUNT, SUM, AVG gibi toplama fonksiyonları ile kullanılır.
* Örnek: Her sınıfta kaç öğrenci olduğunu bulur

# Index ne işe yarar?

Index, büyük veri kümelerinde, veritabanlarında veya web sitelerinde aranan bilgiye çok daha hızlı ve kolay ulaşmayı sağlayan yardımcı liste veya veri yapısıdır.

Veritabanlarında ;
* Okuma hızını artırır: Tablodaki verileri tek tek aramak yerine (tablo taraması) doğrudan adrese gider ve SELECT sorgularını hızlandırır.
* Yeni veri eklendiğinde veya güncellendiğinde (INSERT, UPDATE) indeksin de güncellenmesi gerektiği için ek işlem yaratır.

Arama Motorlarında ve Web Sitelerinde;

* Siteleri kaydeder: Google gibi arama motorlarının web sitelerini tarayıp anlaması ve kendi kütüphanesine (dizinine) eklemesidir.
* Listelemede gösterir: Bir sayfa indexlenirse, kullanıcılar arama yaptığında o sonuçlar listede görünür.


Yazılım ve Programlamada;

Sıra numarası verir: Liste veya dizilerdeki (array) elemanların yerini belirtir. Örneğin ilk elemanın yerini bulmak için kullanılır (çoğu dilde 0'dan başlar).