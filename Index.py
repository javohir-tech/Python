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

mahsulotlar = {}
qiymat = ''
stop = "to'xtatish uchun 'stop' deb yozing"
while qiymat != 'stop' : 
    if qiymat != 'stop' : 
        mahsulot = input(f"mahsulot nomini kiritin {stop} >>> ")
        narxi = input(f"mahsulot narxini kiriting {stop} >>>")
        if mahsulot.lower() == 'stop' or narxi.lower()== "stop" :
            qiymat = 'stop'
            for item, price in mahsulotlar.items():
                print(f"{item} : {price}")
        else:
            mahsulotlar[mahsulot] = narxi

