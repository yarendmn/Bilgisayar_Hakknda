meyveler = {"elma", "armut", "kiraz", "elma"}
meyveler2 = {"elma", "armut", "kiraz", "kavun"}
# sonuc = meyveler[0] bu olmaz

# for x in meyveler:
#   print(x)

# sonuc = "elma" in meyveler

meyveler.add("karpuz")
meyveler.update(meyveler2)
# meyveler.remove("vişne") # raise and error
meyveler.discard("kavun")
# meyveler.pop() tamamen random siler index olmadığı için
sonuc = meyveler

print(sonuc)