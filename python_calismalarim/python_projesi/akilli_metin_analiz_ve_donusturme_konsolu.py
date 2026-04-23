raw_data = input("Öğrenci verilerini giriniz: ")

# Ornek = isim=Ahmet;soyisim=Yılmaz;yas=21;boy=1.78;sehir=Ankara;okul_no=20231234

n1 = raw_data.find(";")
n2 = raw_data.find(";", n1 + 1)
n3 = raw_data.find(";" , n2 + 1)
n4 = raw_data.find(";", n3 + 1)
n5 = raw_data.find(";", n4 + 1)

# parçaları etiketlerinden ayır

isim = raw_data[5 : n1]
soyisim = raw_data[n1+9 : n2]
yas_str = raw_data[n2+5 : n3]
boy_str = raw_data[n3+5 : n4]
sehir = raw_data[n4+7 : n5]
okul_no = raw_data[n5+9 :]

# string slicing ile gizleme

gizli_isim = isim[0].upper + "*" * (len(isim) -1)

gizli_soyisim = "*" *(len(soyisim) -2 ) + soyisim[-2:]

gizli_okul_no = okul_no[0:2] + "X" * (len(okul_no) - 4) + okul_no[-2:]
# hata yönetimi ve dönüşümler
yas = int(yas_str)
boy = float(boy_str)
durum_mesaji = " Veri başarıyla işlendi."
uyari_mesaji = ""
expect ValueError:
durum_mesaji = "Bazı veriler dönüştürülemedi."
uyari_mesaji = "Uyarı: yas, boy"
# FORMATLI VERİ ÇEKME
print("\n---KULLANICI PROFİLİ---")
print(f"Ad          :{gizli_isim}")
print(f"Soyad        :{gizli_soyisim}")
print(f"Yaş:{yas}")
print(f"Boy           :{boy}m")
print(f"Şehir:{sehir}")
print(f"Okul No        :{gizli_okul_no}")
print(f"\n\nDurum       :{durum_mesaji}")

if uyari_mesaji:
    print(uyari_mesaji)
