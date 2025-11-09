buyurtmalar = []
flag = True
while flag :
    buyurtma  = input("buyutma qiling . Buyurtmani to'xtatish uchun 'exit' deb yozing>>>");
    if buyurtma.lower() == 'exit' :
        flag = False
        print('Buyurtmalar')
        for buyurtma in buyurtmalar :
            print(buyurtma)
    else: 
        buyurtmalar.append(buyurtma)