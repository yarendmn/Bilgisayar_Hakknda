customers= ["sadik", "ahmet", "yaren", "serdar"]
order_totals = [12000, 6000, 40000, 444]

# customers.append("sadik")
order_totals.append(5000)

sonuc = customers
sonuc = order_totals

"""customers.pop()
order_totals.pop()

sonuc = customers
sonuc = order_totals"""

sonuc = f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0]+ order_totals[4]} liradır."

#  customers.sort()

order_totals.sort()
order_totals.reverse()

sonuc = min(order_totals)

sonuc = customers.count('sadik')

customers.pop(0)
customers.remove("ahmet")
sonuc = customers

# order_totals.clear()

username = input("Müşteri adı: ")
toplam = input("toplam: ")

customers.append(username)
order_totals.append(toplam)

print(customers)
print(order_totals)




print(sonuc)