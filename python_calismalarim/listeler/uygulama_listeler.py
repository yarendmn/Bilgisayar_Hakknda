# araba markaları listesi
markalar = ["Toyota", "Bmv", "Renault", "Mercedes"]

# markalar listesi kaç elemanlı
sonuc = len(markalar)

# listenin ilk ve son elemanı
sonuc1 = markalar[0]
sonuc2 = markalar[-1]

# renault markasını togg ile güncelle
markalar[2] = "Togg"
sonuc3 = "Togg" in markalar
sonuc4 = "Togg" not in markalar

# listenin ilk iki elemanı
sonuc4 = markalar[0:2]

# liste sonuna ekleme
sonuc5 = markalar + ["Ford", "Citroen"]

# listenin son elemanını sil
del markalar[-1]
sonuc6 = markalar

# verilen verileri liste içinde saklama

ogrenci1 = ["Yiğit", "Bilgi", 2010, [70,80,90]]
ogrenci2 = ["Ada", "Bilgi", 2011, [70,70,90]]
ogrenci3 = ["Çınar", "Turan", 2017, [60,60,90]]

ogrenciler = [ogrenci1,ogrenci2,ogrenci3]

# ogrenci yas hesapla
yasYigit = 2026 - ogrenci1[2]
yasAda = 2026 - ogrenci2[2]
yasCinar = 2026 - ogrenci3[2]

print(yasYigit,yasAda, yasCinar)

notYigit = ogrenciler[0][3][0] + ogrenciler[0][3][1] + ogrenciler[0][3][2]

yigitOrt = notYigit/3
print(yigitOrt)