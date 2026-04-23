# Ağ Temelleri (Networking)
## IP – Port – DNS – TCP – UDP nedir?
Bu terimler, internetin ve ağ iletişiminin temel yapı taşlarıdır. Bilgisayarların birbirini bulması, tanıması ve veri alışverişi yapması bu protokoller sayesinde gerçekleşir.
1. IP (Internet Protocol)

Ağ üzerindeki her cihazın sahip olduğu benzersiz bir kimlik numarasıdır. Verinin nereye gideceğini belirler. IPv4 ve IPv6 olmak üzere iki ana türü vardır.

2. Port (Bağlantı Noktası)

 Bir IP adresine gelen verinin, bilgisayar içindeki hangi programa veya servise gideceğini belirleyen sanal kapılardır. 0 ile 65535 arasında numaralandırılırlar. Örneğin, web siteleri genellikle 80 (HTTP) veya 443 (HTTPS) portunu kullanır.

3. DNS (Domain Name System)

İnternetin telefon rehberi gibidir. İnsanların IP (örn: 142.250.185.78) adreslerini ezberlemeleri zordur. DNS ise google.com gibi alan adlarını, bilgisayarın anlayacabileceği IP adreslerine çevirir.

**Veri İletim Protokolleri: TCP ve UDP**

Bu iki protokol verilerin (paketlerin) bir noktadan diğerine nasıl taşınacağını belirler.

4. TCP (Transmission Control Protocol)

 "Güvenilir" iletim protokolüdür. Gönderilen verinin eksiksiz ve sırasıyla ulaştığını garanti eder. Veri kaybolursa tekrar gönderir.

Kullanım Alanları: Web siteleri (HTTP), E-posta (SMTP), Dosya transferi (FTP).

5. UDP (User Datagram Protocol)

 "Hızlı" ama garanti olmayan iletim protokolüdür. Veriyi gönderir ve ulaşıp ulaşmadığını kontrol etmez. Hız, güvenilirlikten daha önemlidir.

Kullanım Alanları: Online oyunlar, Canlı yayınlar, VoIP (Sesli görüşme).

## Paket yapısı nasıl çalışır?
Bir ağ paketi, internette gönderilen verinin en küçük taşıma birimidir.Paket yapısı temel olarak üç bölümden oluşur: Başlık (Header), Yük (Payload) ve Kuyruk (Trailer).

**Paketin Temel Bölümleri**

1- Header(Başlık)

Paketin en ön kısmıdır.Yönlendiricilerin (Router) bu paketi nereye götüreceğini anlamasını sağlar. Header ; Gönderici IP, Alıcı IP, Protokol tipi (TCP mi UDP mi?), Port numarası içerir.

2- Payload(Yük)

Taşınan asıl veridir (Örneğin; bir resmin küçük bir parçası, bir WhatsApp mesajı). Kullanıcıya ulaştırılmak istenen asıl içeriktir.
 
3- Trailer(Kuyruk)

Genellikle paketin en sonunda bulunur. Paketin yolda bozulup bozulmadığını kontrol eder. İçerisinde Hata Kontol Kodlarını (CRC/FCS) içerir.

**Kapsülleme (Encapsulation): Paket Nasıl Oluşur?**

Bilgisayardan çıkan verilerin katman katman paketlenmesine "Kapsülleme"denir.

Öncelikle veriler *uygulama katmanında* ham veri olarak alınır. Sonrasında *taşıma katmanında* ham veriye TCP başlığı eklenir. Eklenen Bilgi: Kaynak Port (bilgisayarınızdaki tarayıcı) ve Hedef Port (80 veya 443). Bu işleme segmentasyon denir. *İnternet Katmanında* ise segmentin önüne IP başlığı eklenir.Eklenen Bilgi: Sizin IP adresiniz (Gönderici) ve Web Sitesinin IP adresi (Alıcı). Bu işleme de Packet denir. Son olarak *ağ erişim katmanında* paketin önüne MAC başlığı ve sonuna Trailer (FCS) eklenir.Eklenen Bilgi: Modeminize veya yönlendiricinize gitmesi için fiziksel adresler. Bu işleme de çerçeveleme denir.

**Alıcı Tarafta Ne Olur? (Decapsulation)**

Veri karşı tarafa ulaştığında işlem tersine döner.

1.Ethernet

Trailer kontrolü yapar ve içindeki IP paketini alır.

2.IP

IP konrolü yapar adres doğruysa içindeki TCP segmentini alır.

3.TCP

Hangi kapıya (Porta) gidecek?" diye bakar. Veriyi doğru uygulamaya (Web Sunucusu yazılımına) teslim eder.

4.Uygulama

Sunucu mesajı alır ve işler.



*Bir ağ kablosundan geçen verinin yapısı tam olarak şöyledir:*

[Ethernet Başlığı] [IP Başlığı] [TCP Başlığı] [ ASIL VERİ (PAYLOAD) ] [Ethernet Kuyruğu]

Her katman, kendinden bir önceki katmanın verisini (başlığıyla birlikte) kendi "Payload"ı olarak kabul eder ve önüne kendi başlığını ekler.

## Ping, traceroute, nslookup ne işe yarar?
1. Ping (Packet Internet Groper):
Ping, bir IP ağı üzerindeki hedef ana makinenin (host) erişilebilirliğini test etmek için kullanılan temel bir ağ yönetim aracıdır. ICMP (Internet Control Message Protocol) protokolünü kullanır.

**Çalışma Prensibi ve İşlevi:**

*Erişilebilirlik Kontrolü:* Kaynak cihaz, hedef IP adresine bir "ICMP Echo Request" (Yankı İsteği) paketi gönderir. Hedef cihaz çalışır durumdayken ve ağ trafiğine açıksa, "ICMP Echo Reply" (Yankı Cevabı) paketi ile yanıt verir.

*Gecikme Süresi (Latency) Ölçümü:* Paketin gönderildiği an ile cevabın alındığı an arasındaki süre hesaplanarak RTT (Round-Trip Time) değeri milisaniye (ms) cinsinden raporlanır.

*Paket Kaybı Analizi:* Gönderilen istek sayısı ile alınan cevap sayısı karşılaştırılarak, ağ üzerindeki paket kaybı oranı (Packet Loss) tespit edilir.

2. Traceroute (Windows ortamında tracert):
Traceroute, kaynak cihazdan hedef cihaza giden veri paketlerinin ağ üzerinde izlediği rotayı (route) belirlemek ve her bir aktarma noktasındaki (hop) gecikmeleri ölçmek için kullanılan bir ağ tanılama aracıdır.

**Çalışma Prensibi ve İşlevi:**

Yol Haritası Çıkarımı: Paketlerin hedefe ulaşana kadar geçtiği tüm yönlendiricilerin (router) IP adreslerini sırasıyla listeler.

TTL (Time-To-Live) Mekanizması: Araç, gönderdiği paketlerin TTL değerini her seferinde 1 artırarak gönderir. TTL süresi dolan her yönlendirici, kaynağa bir "ICMP Time Exceeded" mesajı döndürür. Bu sayede yol üzerindeki tüm düğümler tek tek tanımlanır.

Hata Noktası Tespiti: Veri iletiminin hangi yönlendiricide veya ağ düğümünde kesintiye uğradığı veya yavaşladığı bu komut ile tespit edilir.

3. Nslookup (Name Server Lookup): Nslookup, DNS (Domain Name System) altyapısını sorgulamak, alan adı ile IP adresi arasındaki eşleşmeleri çözümlemek ve DNS kayıtlarını (A, MX, NS vb.) incelemek için kullanılan bir komut satırı aracıdır.

Çalışma Prensibi ve İşlevi:

DNS Çözümleme (Resolution): Bir alan adının (örn: example.com) hangi IP adresine karşılık geldiğini (Forward Lookup) veya bir IP adresinin hangi alan adına ait olduğunu (Reverse Lookup) sorgular.

Sunucu Testi: Varsayılan DNS sunucusunun veya spesifik olarak belirtilen başka bir DNS sunucusunun doğru yanıt verip vermediğini kontrol eder.

Kayıt Türü Sorgulama: Sadece IP adresi değil; e-posta sunucularını belirten MX kayıtları veya alan adı sunucularını belirten NS kayıtları gibi spesifik DNS verilerini görüntülemek için kullanılır.