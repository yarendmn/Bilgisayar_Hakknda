# Dosya Sistemleri ve Depolama Mantığı

## NTFS – ext4 – APFS farkları

**1.NTFS nedir?**

 Gelişmiş güvenlik, güvenilirlik ve yüksek performansı aynı anda sunmasının yanında modern Windows sistemlerinin temel dosya sistemleri olarak kabul edilen kapsamlı bir dosya sistemidir. Microsoft tarafından geliştirilmiştir.

**2-ext4 nedir?**

Ext4 de NFTS gibi bir dosya sistemidir. Yüksek güvenlik, güvenilirlik ve performansı açısından NFTS ile benzeşse de Linux dağıtımlarında kullanılan bir sistem olması açısından NFTS'den ayrılır.

**APFS nedir?**

AFTS de veri güvenliğini ve bütünlüğünü sağlamaya yönelik olarak Apple tarafından geliştirilmiş modern bir dosya sistemidir.

Esassında hepsi birer dosya sistemi olmasının yanında ancak geliştiriciler, temel kullanım alanları ve öne çıkan özellikleri bakımından bazı noktalarda birbirlerinden ayrışırlar. *Örneğin; Güvenlik ön planda ise NTFS , yüksek performans ve güvenilirlik gerektiren sunucu ortamlarında ext4,  Apple ekosisteminde sorunsuz entegrasyon içinse APFS kullanılabilir.*

## Blok yapısı nedir?

  Dosya sistemlerinde verilerin saklandığı en küçük birimdir.

  Disk alanını daha verimli kullanmak için dosyalar tek parça halinde değil bloklara bölünerek saklanır. Böylece disk alanı daha verimli kullanılmış olur.

## HDD vs SSD Çalışma Prensipleri

Her ikisi de birer veri depolama teknolojisidir.  Ancak HDD'ler dönen diskler ve okuma/yazma kafaları kullanarak çalışırken SDD'ler  NAND flash hücrelerinden oluşan bir dizi hücre grubuna dayalı olarak çalışan ve hücreler veriyi elektrik yüklerini depolayarak saklar,  ayrıca HDD'lere nispeten daha hızlıdır.

SSD'lerin fiziksel yapısı sayesinde daha hızlı ve dayanıklılardır, hareketli parçalar içermediği için daha az mekanik arıza riskine sahiptirler. HDD'ler ise fiziksel hareketler nedeniyle daha kırılgınlardır. Ancak, HDD'ler genellikle daha yüksek depolama kapasitesine sahip olabilirler.

![SDD](https://www.shutterstock.com/image-illustration/ssd-m2-disk-drive-fictional-260nw-2543603681.jpg "SDD görseli")

![HDD](https://www.batuhankilinc.com/wp-content/uploads/2018/11/hdd-gorsel.jpg "HDD görseli")