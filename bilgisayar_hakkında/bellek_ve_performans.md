# Bellek ve Performans Derinliği
## Stack vs Heap 

Stack ve Heap, bilgisayar belleğinin (RAM) programlar çalışırken farklı amaçlar için kullanıldığı iki temel mantıksal ve yapısal bölgedir.

**Stack Nedir?**

Stack, fonksiyonlar içindeki yerel değişkenlerin ve çağrı bilgilerinin saklandığı, boyutu derleme aşamasında belli olan hızlı ve düzenli bir bellek alanıdır

* LIFO mantığıyla çalışır.
* Yönetim otomatiktir.Bir fonksiyon bittiğinde o fonksiyona ait veriler otomatik olarak silinir.
* Hızlıdır çünkü veriler ardışık ve düzenli yerleştirilir.

**Heap Nedir?**

Heap, boyutu önceden bilinmeyen, program çalışırken dinamik olarak ihtiyaç duyulan büyük verilerin veya nesnelerin saklandığı geniş bir bellek havuzudur.

* Karışık ve serbest bir yerleşim mantığıyla çalışır.Bellekte boş olan herhangi bir yere yerleştirilebilir.
* Yönetim genellikle manueldir veya dile bağlı olarak Garbage Collector gibi mekanizmalarla yürütülür.
* Stack'e göre yavaştır çünkü verilere doğrudan değil referans(adresler) üzerinden erişilir.

Stack ve Heap arasındaki temel fark yönetimdir: stack belleği otomatiktir ve boyutu sınırlıdır, heap belleği ise manueldir ve çok daha büyüktür.

## Garbage Collection (GC) nasıl çalışır?
Garbage Collection (GC), bilgisayar bilimlerinde programların kullandığı ve artık ihtiyaç duyulmayan belleği (hafızayı) otomatik olarak temizleyen bir bellek yönetimi mekanizmasıdır.

Çöp toplayıcı (Garbage Collector), Java veya .NET gibi ortamlarda genellikle üç temel adımı izler:

* Mark (İşaretleme): GC, bellekteki (heap) tüm nesneleri tarar. Program tarafından hâlâ kullanılan (erişilebilir) nesneleri işaretler.
* Sweep (Süpürme/Silme): İşaretlenmemiş, yani artık hiçbir referansı kalmayan ölü nesneleri bellekten temizler ve bu alanları boşaltır.  

* Compact (Birleştirme): Silinen nesnelerden arta kalan dağınık boşlukları düzenler. Hayatta kalan nesneleri bir araya getirerek, gelecekteki nesne atamaları için düzenli ve büyük bir boş alan oluşturur.

## Memory Leak nedir, nasıl oluşur?

Memory Leak(Bellek Sızıntısı) bir uygulamanın defalarca bellek ayırması ve ayırdığı belleğin serbest bırakılmamasından kaynaklı olarak bellek kullanımını arttırmaya kümülatif olarak devam etmesidir. 

Bellek sızıntıları, yazılım kodundaki mantıksal hatalar yüzünden ortaya çıkar:

* Öncelikle program çalışmak için geçici olarak RAM'den yer ister. (dillere bağlı olarak `new` veya `malloc` komutlarıyla)

* Sonrasında programın bir sebepten ötürü o veriye veya nesneye ihtiyacı kalmaz.

* Ancak geliştirici kodu yazarken ya bu alanı silmeyi unutur ya da sistem bunu atık olarak algılamaz ve hala arkada bir referans tuttuğu için bellek boşaltılmaz.

* Bu işlem tekrarlandıkça RAM dolar ve RAM doldukça sistem verileri diske atarak RAM'i boşaltmaya çalışır ancak belli bir yerden sonra I/O işlemlerinde de yavaşlamalar olur ve bilgisayar yavaşlayarak çöker. 