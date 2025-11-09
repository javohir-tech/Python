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
flag = True;
stop = "to'xtatish uchun 'stop' deb yozing"
while flag : 
    mahsulot = input(f"mahsulotni kiriting {stop}>>> ")
    if mahsulot.lower() == 'stop' :
        for item, narx in mahsulotlar.items():
            print(f"{item} : {narx}")
            break
    price = input(f"mahsulot narxini kiriting {stop}>>> ")
    if mahsulot.lower() == 'stop' :
        flag = False;
        for item, narx in mahsulotlar.items():
            print(f"{item} : {narx}")
    
    mahsulotlar[mahsulot] = int(price);

