sayilar = [4,4,6,7,80,100]
isimler = ['Yaren', 'Cagan', 'Gökhan']

sonuc = min(sayilar)
sonucH = max(isimler) # alfabetik sıralama

# ekleme
"""sayilar.append(13)
isimler.append('Çınar')

sayilar.insert(-1,100)
sayilar.insert(-3, 30)
sayilar.insert(len(sayilar), 47)"""

# silme

"""sayilar.pop()
sayilar.pop(0)
isimler.remove('Yaren')"""

# sıralama

"""sayilar.sort()
sayilar.reverse()"""

# arama

sonuc = sayilar.index(4)
# sonuc = sayilar
# sonuc = isimler
# sonuc = sayilar.count(4)
print(sonuc)