#kursAdi = "Python ile programlama"

#print(kursAdi[-1])

# string concat
# ad = "yaren"
# soyad = "duman"
# yas = 18

# msj = "My name is " + ad + " " + soyad + "." + "I'm" + str(yas) + " years old."
#string format
# mesaj = "My name is {0} {1} . I'm {2} years old.".format(ad, soyad, yas)
# mesaj = "My name is {} {} . I'm {} years old.".format(ad, soyad, yas)
# mesaj = "My name is {a} {s} . I'm {y} years old.".format(a=ad, s=soyad, y=yas)
# print(mesaj)

# f-string

# mesaj1 =f"My name {ad} {soyad}. I'm {yas} years old."

# print(mesaj1)

kurs = "Btk Akademi ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

# 1- ' Btk Akademi ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz.

sonuc = ' Btk Akademi '.strip()
print(sonuc)
# 2- kurs deg tüm karakterleri küçült
sonuc2= kurs.lower()
print(sonuc2)
# web sitede kaç tane nokta var
sonuc3 = website.count('.')
print(sonuc3)
# https ile mi başlıyor website değişkeni
sonuc4 = website.startswith('https')
print(sonuc4)
# website ' tr ' ile mi  bitiyor
sonuc5 = website.endswith('tr')
print(sonuc5)
# kurs değişkeni tamamen karakterlerden mi oluşuyor
sonuc6 = kurs.isalpha()
print(sonuc6)
# kurs değişkenindeki tüm boşlukları - bununla deüiştir
sonuc7 = kurs.replace(' ','-' ).lower()
print(sonuc7)
# website www içeriyor mu
sonuc8 = website.find('www')
print(sonuc8)
# kurs degişkenini listeye cevirin
sonuc9 = kurs.split(' ')
print(sonuc9)
