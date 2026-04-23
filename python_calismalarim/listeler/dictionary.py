# sıralanabilir key_-value türünde veri saklanabşlir.

"""obj= {
"username": "yarenduman"
"order_total" : 10.000
"date" :'10.10.2026'
}
"""
"""sehirler = ["kocaeli", "istanbul"]
plakalar = [41,34]

# key - value
print(plakalar[0],sehirler[0])
print(plakalar[1],sehirler[1])

print(plakalar[sehirler.index("istanbul")])
print(plakalar[sehirler.index("kocaeli")])"""

# dictionary

plakalar={
    "kocaeli": 41,
    "istanbul": 34,
    "İzmir": 36
}

plakalar["İzmir"] = 35
print(plakalar["kocaeli"])
print(plakalar["İzmir"])
