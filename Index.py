family = [
    {
        "who" : "Dadam", 
        "name" : "ALimardon",
        "year" : 1977
    }, 
    {
        "who": "Onam ", 
        "name" : "Xolida", 
        "year" : 1982
    }
]

for item in family :
    print(f"{item["who"]} {item['year']} yilda tug'ilgan")
    item["address"] = "Angren"
    del item["address"]
print(family)


talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

for kalit , qiymat in talaba_0.items() :
    print(f"{kalit} : {qiymat}")

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(sorted(mahsulotlar))
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

for tel in set(telefonlar.values()):
    print(tel)

davlatlar = {
    "Aqsh" : "Washingtosh", 
    "Russia" : "Maskva", 
    "Uzbekistan" : "Toshkent", 
    "Fransiya" : "Paris", 
    "Italiya" : "Rim"
}

davlat = input("Davlatni kiriting >>> ").title()

if davlat in davlatlar.keys() :
    print(davlatlar[davlat])
else: 
    print('fuck is shet')
print(davlatlar.get(davlat , 'fucck is shet'))
for davlat in davlatlar.keys():
    print(davlat)
    
for poytaxt in davlatlar.values():
    print(poytaxt)

taomlar  = {
    "osh" : 20000, 
    "palov": 150000,
    "manti":30000, 
    "somsa" : 10000, 
    "lagmon" : 15000, 
    "rolton" : 1000,
    "chuchvra" : 30000  
}
buyurtmalar = []
jami_summa =0 
print("uchta ovqat buyurtma qiling !")

for n in range(3):
    buyurtma = input(f"{n+1} chi toam ni buyuring >>> ").lower()
    buyurtmalar.append(buyurtma)

for buyurtma in buyurtmalar :
    if buyurtma in taomlar.keys():
        print(f"{buyurtma} narxi {taomlar[buyurtma]} so'm")
        jami_summa+=taomlar[buyurtma]
    else:
        print(f"kechirasiz bizda {buyurtma} yo'q")
print(f"Jammi sizdan {jami_summa} so'm boldi")