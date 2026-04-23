markalar = ["opel", "bmv", "togg"]


"""index = 1
for marka in markalar:
    print(f"{index}--{marka}")
    index += 1"""

obj1 = enumerate(markalar,1)
# enumerate önce listeler sonra listedeki elemanları indexler

print(type(obj1))
print(list(obj1))

for marka in enumerate(markalar):
    print(marka)