# İŞLETİM SİSTEMİ TEMELLERİ(OS BASİC)
## Kernel nedir?
Bir işletim sistemi çekirdeğidir. Donanım ve yazılımlar arası köprü görür  ve sistem kaynaklarını (CPU, bellek, I/O cihazlarını) yönetir.
*Bellek , süreç yönetimi* gibi bilgisayardaki ana işlemler burada yapılır.
## Süreç (process) – iş parçacığı (thread) farkı
Çalışan her bir programa "Process" denir. Örneğin ayrı iki programı açmak gibi. Thread ise process içindeki alt görevlerdir. Örneğin aynı program içinde farklı sekmeler açmak gibi. Her processin özel bir bellek alanı vardır ve bir process çökerse genellikle diğerini etkilemez. Ancak thread aynı process içinde diğer thread lerle aynı bellek alanını paylaşırlar ve bir thread çöktüğü zaman tüm process kapanabilir.
## Bellek yönetimi nasıl yapılır?
Sınırlı olan RAM kaynağının çalışan işlemler (process) arasında adil,   güvenli ve verimli bir şekilde paylaştırılması sürecidir. Bellek yönetiminin temel amaçları paylaştırma, izolasyon(koruma) ve  verimliliktir.

**Temel Teknikler**

*Paging(Sayfalama)* : Fiziksel belleğin frame denilen eşit parçalara, mantıksal belleğin ise page denilen parçalara bölünmesidir.

*Segmentation(Bölütleme)* : Belleğin mantıksal birimlere (kod, veri, yığın/stack gibi) göre bölünmesidir.

*Sanal Bellek(Virtual Memory)* : RAM yetmediğinde, sabit diskin bir kısmının RAM gibi kullanılmasıdır.

[ İşlem A ] ----\ 
[ RAM ]
                 ---> [ Adres
Çevirici ] ---> [ Fiziksel Adres ]
[ İşlem B ] ----/
## CPU zamanlayıcıları nedir?
Bellekte(RAM) hazır halde aynı anda çalışmak isteyen farklı onlarca işlem (process) olmasına karşın CPU aynı anda çekirdek sayısına göre bir veya birkaç işlem yapabilir.
 Zamanlayıcı da hangi processin işlemciyi ne kadar süreyle kullanacağına ve sıradaki işlemin hangisi olacağına karar veren bir mekanizmadır. Zamanlayıcı CPU verimliliği, her işlemin işlemciden pay almasını ve bilgisayarın hız açısından performansını korumasını sağlar.

**En Yaygın Zamanlama Algoritmaları**

*FCFS(First-Come, First-Served)*

CPU'nun işlemleri gelme sırasına göre işleme aldığı zamanlama algoritmasıdır.İlk gelen işlem ilk yapılır sonra sonraki işlem CPU'ya alınır ve bu işlemler bitene kadar devam eder.

*SJF (Shorest Job First)*

İşlemleri burst time'ı(yürütme süresi) en az olandan en çok olana göre sıralar ve en küçük olandan başlayarak sırayla işleme koyar.

*Round Robin(RR)*

Her işlem için belirli bir zaman dilimi (time quantum) verilir. Süre bitince işlemci sıradaki işleme geçer.

*Priority Scheduling*
 
Her işlem için atanan öncelik sayısına göre CPU en öncelikli olan işlemden itibaren işlemleri sırayla alır.

**Zamanlayıcı Türleri**

İşlemciyi o an kimin kullanıcağına karar veren en hızlı çalışan kısmına "Kısa Vadeli", Bellek dolduğunda bazı işlemleri geçici olarak disk alanına taşıyanlara "Orta Vadeli" ve hangi işlemin hazır kuyruğuna alınacağına karar veren zamanlayıcıya ise "Uzun Vadeli Zamanyalıcı" nedir.