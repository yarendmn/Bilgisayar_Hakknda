ogrenciler = {
    101: {
        "Ad": "Yiğit",
        "Soyad": "Bilgi",
        "DoğumYili": 2010,
        "Notlar": (40,80,90)

},
    102:{
        "Ad": "Ada",
        "Soyad": "Bilgi",
        "DoğumYili": 2011,
        "Notlar": (30, 80, 90)
    },
    103:{
        "Ad": "Çınar",
        "Soyad": "Turan",
        "DoğumYili": 2017,
        "Notlar": (70, 70, 70)

    }
}

ogrenciNo = int(input("öğrenci no: "))
ogrenci = ogrenciler[ogrenciNo]
ortalama = (ogrenci["Notlar"][0] + ogrenci["Notlar"][1] + ogrenci["Notlar"][2])/ 3

print(f"{ogrenciNo} numaralı {ogrenci["Ad"]} {ogrenci["Soyad"]} ismindeki öğrencinin yaşı {2026 - ogrenci["DoğumYili"]} ve not ortalaması {ortalama}. ")