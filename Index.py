# buyurtmalar = []
# flag = True
# while flag :
#     buyurtma  = input("buyutma qiling . Buyurtmani to'xtatish uchun 'exit' deb yozing>>>");
#     if buyurtma.lower() == 'exit' :
#         flag = False
#         print('Buyurtmalar')
#         for buyurtma in buyurtmalar :
#             print(buyurtma)
#     else: 
#         buyurtmalar.append(buyurtma)

mahsulotlar = {
    "non" : 3000,
    "gosht" : 75000, 
    "sabzi" :  10000, 
    "bodiring" : 17000, 
    "pamidor" : 20000
}

buyurtmalar = [];
flag =  True,
sum= 0
while flag :
    buyurtma = input(f"mahsulot nomini kiriting . to'xtatish uchun 'stop' deb yozing>>>");
    if buyurtma != 'stop' :
        buyurtmalar.append(buyurtma)
    else:
        for order in buyurtmalar :
            if order in mahsulotlar.keys() :
                print(f"{order} narxi : {mahsulotlar[order]}") 
                sum += mahsulotlar[order]
            else:
                print(f"{order} bizda mavjud emas")
        print(f"jammi summa {sum} so'm")  

