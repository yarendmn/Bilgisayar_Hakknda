# DESİGN PATTERNS (Tasarım Desenleri)

Yazılım tasarım desenleri (design patterns), yazılım geliştirmede sık karşılaşılan problemlere yönelik genel, tekrarlanabilir ve dilden bağımsız çözüm şablonlarıdır. Doğrudan kopyalanıp yapıştırılan hazır kodlar değildir; soruna nasıl yaklaşılacağını gösteren yapılardır.

## Neden Design Pattern kullanılır?
 
Yazılımın çalışır halde olması başlı başına yeterli değildir. Aynı kodu aylar sonra değiştirmek, büyütmek veya başka bir yazılımcıya devretmek istendiğinde çıkabilecek olsaı bir krizi engellemek için kullanılır.

* **Ortak dil:** Koda bakan herkes aynı şekilde anlar.
* **Spagetti kodu önleme:** devasa if-else ler yerine sorumluluklar sınıflara bölünür.
* **Değişime dayanıklılık:** yeni bir özellik eklerken eski çalışan kod bozumamayı sağlar.

## Yaratımsal Desenler (Creational)

### 1. Singleton --Tek Örnek

*İç Mekanizma:* Sınıfın kurucu metodu (constructor) private yapılır, böylece dışarıdan kimse new ile yeni nesne üretemez. Sınıf kendi içinde static bir örnek tutar ve dış dünyaya sadece GetInstance() gibi tek bir erişim kapısı açar. İlk çağrıda nesne oluşur, sonrakilerde hep aynı nesne döner.

*Gerçek Senaryo:* Uygulama genelindeki Loglama (Logger) servisi, veritabanı bağlantı havuzu veya bir oyundaki tekil AudioManager / GameManager.


```
public class Logger
{
    private static Logger _instance;
    private Logger() { }

    public static Logger GetInstance()
    {
        if (_instance == null)
            _instance = new Logger();
        return _instance;
    }

    public void Log(string message) => Console.WriteLine($"[LOG]: {message}");
}

var logger1 = Logger.GetInstance();
var logger2 = Logger.GetInstance();
```
Örnekteki gibi dışarıdan new Logger() yapılmasını engeller, tüm sistemde tek bir nesne döndürür.


*Tuzak / Ne Zaman Kullanılmamalı?* Global değişken gibi davrandığı için sınıflar arasındaki bağımlılıkları gizler ve birim testi (unit test) yazmayı zorlaştırır. Ayrıca çoklu iş parçacığı (multi-threading) ortamında lock mekanizması kurulmazsa aynı anda iki nesne oluşabilir.

### 2. Factory --Nesne Olusturma

*İç Mekanizma:* Nesne üretme kararını ana koddan söküp ayrı bir "Fabrika" sınıfına taşır. Ana kod new Kamyon() veya new Gemi() demek yerine fabrikaya Fabrika.Olustur("Deniz") der; fabrika ise ortak bir arayüz (ITasima) üzerinden doğru nesneyi döndürür.

```
public interface ITasima { void TeslimEt(); }

public class Kamyon : ITasima
{
    public void TeslimEt() => Console.WriteLine("Kara yoluyla teslim edildi.");
}

public class Gemi : ITasima
{
    public void TeslimEt() => Console.WriteLine("Deniz yoluyla teslim edildi.");
}

public class LojistikFabrikasi
{
    public static ITasima Olustur(string tip) => tip switch
    {
        "Kara" => new Kamyon(),
        "Deniz" => new Gemi(),
        _ => throw new ArgumentException("Geçersiz tip")
    };
}

ITasima tasima = LojistikFabrikasi.Olustur("Deniz");
tasima.TeslimEt();

```

Örnekte görüldüğü gibi nesne üretimini (new) ana koddan ayırıp tek bir fabrikaya toplar.

*Gerçek Senaryo:* Farklı veritabanlarına (MySQL, PostgreSQL, SQLite) bağlanan sistemler, ödeme sağlayıcıları veya oyunlarda düşman/kart üreten Spawner yapıları.

*Tuzak / Ne Zaman Kullanılmamalı?* Sistemde sadece 1–2 sabit sınıf varsa ve yenilerinin eklenme ihtimali yoksa, araya fabrika koymak gereksiz dosya ve kod kalabalığı (over-engineering) yaratır.


## Davranışsal Desenler (Behavioral)

### 3. Strategy (Strateji)

*İç Mekanizma:* Aynı işi farklı yollarla yapan algoritmalar, ortak bir arayüz (IOdemeStratejisi) altında bağımsız sınıflara bölünür. Ana sınıf (Sepet) hesaplamayı kendisi yapmaz; kendisine o an verilen strateji nesnesine devreder. Böylece çalışma zamanında (runtime) davranış değiştirebilirsin.

```
public interface IOdemeStratejisi { void Ode(decimal tutar); }

public class KrediKarti : IOdemeStratejisi
{
    public void Ode(decimal tutar) => Console.WriteLine($"Kart ile {tutar} TL ödendi.");
}

public class Havale : IOdemeStratejisi
{
    public void Ode(decimal tutar) => Console.WriteLine($"Havale ile {tutar} TL ödendi.");
}

public class Sepet
{
    private IOdemeStratejisi _strateji;
    public void StratejiSec(IOdemeStratejisi strateji) => _strateji = strateji;
    public void OdemeyiTamamla(decimal tutar) => _strateji.Ode(tutar);
}

var sepet = new Sepet();
sepet.StratejiSec(new KrediKarti());
sepet.OdemeyiTamamla(500);

```

*Gerçek Senaryo:* E-ticarette ödeme yöntemleri (Kredi Kartı, Havale, Kripto), navigasyon uygulamasında rota seçimi (Yürüyüş, Araç, Toplu Taşıma) veya bir oyunda karakterin saldırı/hareket modları.

*Tuzak / Ne Zaman Kullanılmamalı?* Algoritma hiç değişmeyecekse veya sadece iki basit koşul varsa, onlarca küçük sınıf açmak yerine basit bir if bloğu çok daha okunaklıdır.

### 4. Observer (Gözlemci)

*İç Mekanizma:* Bire-çok (one-to-many) abonelik modeli kurar. Yayıncı (Subject), kendisine abone olanların (Observer) listesini tutar. Durumu değiştiğinde listedeki herkese "Durum değişti!" sinyali gönderir; abonelerin bu sinyalle ne yaptığıyla hiç ilgilenmez (gevşek bağlılık / loose coupling).

```
public interface IAbone { void BildirimAl(string mesaj); }

public class Musteri : IAbone
{
    public string Ad { get; }
    public Musteri(string ad) => Ad = ad;
    public void BildirimAl(string mesaj) => Console.WriteLine($"{Ad} bildirim aldı: {mesaj}");
}

public class Urun
{
    private List<IAbone> _aboneler = new();
    public void AboneOl(IAbone abone) => _aboneler.Add(abone);
    public void StogaGir()
    {
        foreach (var abone in _aboneler)
            abone.BildirimAl("Ürün tekrar stokta!");
    }
}

var urun = new Urun();
urun.AboneOl(new Musteri("Yaren"));
urun.StogaGir();

```


*Gerçek Senaryo:* Arayüz (UI) güncellemeleri (örneğin oyuncunun canı azaldığında can barının, ses efektinin ve ekran uyarısının aynı anda tepki vermesi), e-ticarette "Stok gelince haber ver" sistemi.

*Tuzak / Ne Zaman Kullanılmamalı?* Bir nesne yok olurken abonelikten çıkmayı (Unsubscribe) unutursan bellek sızıntısı (memory leak) oluşur. Ayrıca bir gözlemci başka bir yayıncıyı tetiklerse zincirleme reaksiyonları takip etmek zorlaşır.

## Yapısal Desenler (Structural)

### 5. Adapter (Adaptör)

*İç Mekanizma:* Birbiriyle uyumsuz iki arayüzün arasına giren bir "çevirici" (wrapper) sınıfıdır. İstemcinin beklediği arayüzü uygular, arka planda ise uyumsuz olan diğer sınıfın metodunu çağırıp veriyi dönüştürür. İki tarafın da mevcut koduna dokunulmaz.

*Gerçek Senaryo:* Eski (legacy) bir XML servisini modern JSON tabanlı uygulamaya bağlamak veya dışarıdan alınan bir 3. parti API'yi kendi sisteminin standart arayüzüne uydurmak.

```
public interface IJsonServisi { string JsonVeriGetir(); }

public class EskiXmlServisi
{
    public string XmlVeriGetir() => "<veri>Merhaba</veri>";
}

public class XmlToJsonAdapter : IJsonServisi
{
    private readonly EskiXmlServisi _eskiServis;
    public XmlToJsonAdapter(EskiXmlServisi eskiServis) => _eskiServis = eskiServis;

    public string JsonVeriGetir()
    {
        string xml = _eskiServis.XmlVeriGetir();
        return "{ \"veri\": \"Merhaba\" }";
    }
}

IJsonServisi servis = new XmlToJsonAdapter(new EskiXmlServisi());
Console.WriteLine(servis.JsonVeriGetir());

```

*Tuzak / Ne Zaman Kullanılmamalı?* Her iki tarafın da kaynak koduna sahipsen ve doğrudan düzenlemek kolaysa, araya adaptör sıkıştırmak yerine arayüzü baştan temiz tasarlamak daha doğrudur.

### 6. Decorator (Dekoratör)

*İç Mekanizma:* Kalıtım (inheritance) yerine bileşim (composition) kullanır. Dekoratör sınıfı, süslediği nesneyle aynı arayüzü uygular ve içinde o nesnenin bir referansını tutar. Nesneleri soğan kabuğu gibi iç içe sararak (Krema(Sut(Kahve))) çalışma zamanında dinamik özellik ekler.

```
public interface IKahve
{
    string Aciklama();
    double Fiyat();
}

public class SadeKahve : IKahve
{
    public string Aciklama() => "Sade Kahve";
    public double Fiyat() => 50.0;
}

public class SutDecorator : IKahve
{
    private readonly IKahve _kahve;
    public SutDecorator(IKahve kahve) => _kahve = kahve;

    public string Aciklama() => _kahve.Aciklama() + ", Süt";
    public double Fiyat() => _kahve.Fiyat() + 15.0;
}

IKahve kahve = new SadeKahve();
kahve = new SutDecorator(kahve);
Console.WriteLine($"{kahve.Aciklama()} - {kahve.Fiyat()} TL");

```

*Gerçek Senaryo:* Dosya/veri akışlarına (Stream) sırayla sıkıştırma, şifreleme ve tamponlama (buffer) eklemek; bildirim sisteminde aynı anda Email + SMS + Push göndermek veya oyunlarda karaktere geçici güçlendirmeler (buff) takmak.

Tuzak / Ne Zaman Kullanılmamalı? Çok fazla katman iç içe geçtiğinde nesne oluşturma satırı karmaşıklaşır ve hatanın hangi katmandan geldiğini ayıklamak (debug) zorlaşır.