# Linux Temelleri
## Terminal Komutları(ls,cd,grep,mkdir,chmod,top)
Bu komutlar klasörler üzerinde farklı işlemler gerçekleştirmek için kullanılır.

**1. ls**
 
 İsmi "list" ifadesinin kısaltmasından gelir.

 Geçerli klasörün içeriğini (alt klasörler ve dosyalar) görüntülemek için kullanılır.

 Cihazdaki tüm klasörleri görüntülemek için tek başına kullanılabilir. 
 
 **2. cd**
 

 Farklı bir dizine geçiş yapmak için kullanılır.
 
 *Kullanım Kalıbı:* cd [gidilecek_klasör]

 **3. grep**
 
 İsmi "global regular expression print" (Küresel düzenli ifade yazdırma) ifadesinin kısaltmasından gelir.

 Bir dosyanın içinde belirli bir kelimeyi aramak için kullanılır.

*Kullanım Kalıbı:* grep [seçenekler] "aranacak_kelime" [dosya_yolu]

**4. mkdir**

İsmi "make directory" (klasör oluştur) kelimelerinin kısaltmasıdır.

Linux ve tüm komut satırı sistemlerinde yeni bir klasör oluşturmak için kullanılan komuttur.

*Kullanım Kalıbı:* mkdir [klasör_adı]

**5. chmod**

İsmi "change mod" (modu değiştir) ifadesinin kısaltmasıdır.

Bir dosya veya klasörün yetki ayarlarını değiştiren komuttur.

Özellikle yazdığın bir kodu bilgisayara "Bu sadece bir yazı değil, çalışan bir programdır" diye tanıtmak (+x yetkisi vermek) için kullanılır.

*Kullanım Kalıbı:* chmod   [işlem_yetkisi] [işlem] [izin] dosya_adı

**6. top**

Linux'un Görev yöneticisidir. Sistem kaynaklarını (CPU, RAM) kimin tükettiğini canlı(real-time) olarak izlemeni sağlar.

Bilgisayar yavaşladığında, bir program donduğunda ya da yazdığın kod döngüye girdiğinde kullanılır.

*Kullanım Kalıbı:* top

## Paket Yönetimi(apt/pacman/dnf)
Linux işletim sistemlerinde program yükleme, güncelleme ve silme işlerini yapan merkezi sistemin adıdır.

**1-apt**

apt(Advanced package tool),Ubuntu, Debian, Linux Mint, Kali Linux ve Pardus gibi farklı Linux dağıtımlarında program yüklemek, güncellemek ve kaldırmak için kullanılan komuttur. 

Linux'un "App Store" veya "Google Play"inin komut satırı hali olarak düşünülebilir.

**2. dnf**

dnf, (Dandified YUM), Fedora, Red Hat (RHEL), CentOS, AlmaLinux ve Rocky Linux gibi farklı Linux dağıtımlarında kullanılan modern paket yöneticisidir.

**3. pacman**

Pacman, oldukça hızlı işlemler yapılmasına olanak veren Arch Linux ve türevlerinin paket yöneticisidir.

İsmini tabiki çocukluğumuzun oyunu olan "Pac-Man" den değil, "PACacge MANager" kelimelerinin kısaltmasından alır.

## Dosya İzinleri

Linux dosya izinleri; çok kullanıcılı işletim sistemi mimarisinde, veri bütünlüğünü korumak ve yetkisiz erişimi engellemek amacıyla kullanılan, dosya bazlı temel erişim kontrol (Access Control) mekanizmasıdır.

Dosya izni için komut yazarken düzen ilk karakter dosya türü(d=dizin), sonraki üçlü sayı grubu ise sırayla Sahip, Grup ve Diğerlerini temsil eder.

1- Sayısal (octal) sistem mantığı

Her iznin (w, r gibi) bir sayısal değeri vardır. Okuma yani w=4, yazma yani r=2, çalıştırma yani r=1 e karşılık gelir.

Örneğin: Neden "chmod 777" yazıyoruz? Çünkü 4+2+1=7 tam yetki eder bu da tam yetki anlamına gelir.

Ancak herkese yazma ve çalıştırma izni vermek (777), sistemin kötü nietli yazılımlara karşı savunmasız bir hale getirir. Bu yüzden *İhtiyaç Duyulan En Az Yetki Prensibi (Principle of Least Privilege)* uygulanmalıdır.

## Servisler (systemctl)
Bilgisayarınızda arka planda sessizce çalışan programlara (örneğin web sunucusu, veritabanı, bluetooth, internet bağlantısı) *Servis(Daemon)* denir. *systemctl*, bu servisleri yönetmenizi sağlar.

Windows'taki "Görev Yöneticisi > Hizmetler" sekmesinin veya "Services.msc" ekranının Linux'taki karşılığıdır.

*Start* komutu bilgisayar her açılıp kapandığında duran motoru o an için çalıştırırken, *enable* komutu motoru sistem açıldığı her an için motoru otomatik çalıştır manasına gelir.

Ve bu komutların ardından kullanmak istediğin [servis_adı] ını yazmalısın.(apache2, mysql, ssh)

**Örnek Senaryo: Web Sunucusu Kurmak**

Diyelim ki C veya Python ile yazdığın bir web uygulamasını yayınlayacaksın.

1. Önce durumuna bakarsın: systemctl status nginx -> (Inactive/Dead yazar)

2. Başlatırsın: sudo systemctl start nginx

3. Tekrar bakarsın: systemctl status nginx -> (Active/Running yazar ve yeşil yanar)
