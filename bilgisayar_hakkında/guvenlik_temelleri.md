# Güvenlik Temelleri (Security Basics)

## Authentication vs Authorization

Authentication, bir kullanıcının veya sistemin gerçek kimlik doğrulama sürecidir. Bazı doğrulama yöntemleri şunlardır:
* Kullanıcı Adı ve Şifre
* Biyometrik Kimlik Doğrulama
* Tek Kullanımlık Kimlik Doğrulama Kodları (OTP)
* Çift Faktörlü Kimlik Doğrulama (2FA)


Authorization (Yetkilendirme) ise kimliği doğrulanmış bu kullanıcının nerelere erişebileceğini veya hangi işlemleri yapabileceğini belirlemesidir. 

Bu iki terimin birbiri yerine kullanılması yanlıştır. Yetkilendirme işlemi ve kimlik doğrulama birbiri ardına gerçekleşir. Doğrulama işlemi olmadan yetkilendirme yapılmaz.

Özetle: Sisteme giriş yapabilmeniz Authentication, giriş yaptıktan sonra başkasının profilini silememeniz Authorization ile ilgilidir.

## Modern Yetkilendirme ve Yönetim Standartları: JWT ve OAuth

Modern yetkilendirme mimarilerinde OAuth bir yetkilendirme çerçevesi (framework), JWT (JSON Web Token) ise bir belirteç (token) formatıdır; bu iki yapı sıklıkla birlikte çalışsa da farklı amaçlara hizmet eder.

**JWT (JSON Web Token)**
JWT, sunucu ile istemci arasında bilgileri güvenli bir şekilde JSON nesnesi olarak taşımak için kullanılan kompakt ve bağımsız bir standarttır.

* Mantığı: Kullanıcı başarılı bir şekilde giriş yaptığında, sunucu imzalı bir token üretir ve istemciye gönderir. İstemci, sonraki her istekte (HTTP Header içinde) bu token'ı sunucuya iletir.

* Avantajı: Sunucunun belleğinde oturum (session) tutmasına gerek kalmaz (Stateless). Ölçeklenebilir sistemler için idealdir.

* Yapısı: Üç parçadan oluşur: Header (Algoritma), Payload (Kullanıcı verileri/yetkileri), Signature (Doğrulama imzası).

**OAuth (Open Authorization)**
OAuth, şifre paylaşmadan bir uygulamanın başka bir uygulamadaki verilere erişmesi için kullanılan bir yetkilendirme (delegasyon) protokolüdür.

* Mantığı: "Google ile Giriş Yap" veya "GitHub ile Bağlan" butonlarının arkasındaki sistemdir.

* Avantajı: Kullanıcı, asıl şifresini üçüncü parti bir uygulamaya (örneğin sizin geliştirdiğiniz bir e-ticaret sitesine) vermek zorunda kalmaz. Sistemler arası güvenli bir erişim köprüsü kurulur.

## En Sık Karşılaşılan Web Zafiyetleri

Bir sistemi dışarıya açtığınızda, kullanıcıdan alınan girdiler (input) en büyük tehlike kaynağıdır.

**SQL Injection (SQLi)**
Kötü niyetli kişilerin, uygulamanın veritabanına gönderdiği SQL sorgularına manipülatif eklemeler yaparak veritabanını ele geçirmesi veya bozmasıdır.

* Nasıl Çalışır? Bir login ekranında kullanıcı adı kısmına ' OR 1=1 -- yazan bir saldırgan, arka plandaki sorguyu her zaman "Doğru" (True) dönecek şekilde kırarak şifre bilmeden sisteme girebilir.

* Nasıl Önlenir? Kullanıcı girdileri hiçbir zaman doğrudan SQL stringlerine eklenmemelidir. Bunun yerine Parametrik Sorgular (Parameterized Queries) veya Entity Framework gibi ORM araçları kullanılmalıdır.


**XSS (Cross-Site Scripting)**
Saldırganın, uygulamanız üzerinden diğer kullanıcıların tarayıcılarında çalışacak zararlı JavaScript kodları enjekte etmesidir.

* Nasıl Çalışır? Bir forum sitesindeki yorum alanına <script>alert(document.cookie)</script> yazıldığında, site bu yorumu filtrelemeden ekrana basarsa, o sayfayı ziyaret eden herkesin tarayıcısında bu kod çalışır ve oturum bilgileri (çerezler) çalınabilir.

* Nasıl Önlenir? Kullanıcıdan alınan tüm veriler ekrana basılmadan önce temizlenmeli (Input Validation) ve tehlikeli HTML karakterleri zararsız metin formatına dönüştürülmelidir (HTML Encoding).