import random


def son_top(son):
    print(f"1 dan {son} gacha son o'yladim topa olasizmi ?? ")
    num = random.choice(list(range(1, son + 1)))
    count = 0
    javob = int(input(">>"))
    if javob != num:
        count += 1
        while javob != num:
            count+=1
            if javob < num:
                javob = int(
                    input("Xato men oylagan son bundan katta . Yana Harakat qiling : ")
                )
            elif javob > num:
                javob = int(
                    input("Xato men oylagan son bundan kichik . Yana harakat qilip : ")
                )
    if javob == num:
        return count


def sen_top(num):
    arr = list(range(1, num + 1))
    print(f"endi siz 1 dan {num} gacha son o'ylang men topishga harakat qilaman ")
    ruhsat = int(input("boshlaymizmi ha(1) yo'q(0)"))
    flag = True
    count =0 
    if ruhsat == 1:
        while flag:
            oylaganSon = random.choice(arr)
            javob = input(
                f"Siz {oylaganSon} o'ylagansiz : to'g'ri (T) , bundan katta (+) , bundan kichik (-)>>"
            )
            count+=1
            if javob == "+":
                arr = list(filter(lambda x: x > oylaganSon, arr))
            elif javob == "-":
                arr = list(filter(lambda x: x < oylaganSon, arr))
            elif javob.lower() == "t":
                flag = False
                return count
    else:
        return False 
        

def ishlat(num) :
    ruhsat = 1
    while ruhsat == 1:
        javob =son_top(num);
    
        if javob :
            print(f"Tabriklaymiz siz {javob} ta  urunishda topdizngiz !!!")
            javob2 =sen_top(num)
            if javob2 :
                  print(f"biz {javob2} ta urunishda topdik ")
        
        if javob2 == javob :
            print(f"durrang ikkalamiz ham {javob} ta urunishda topdik")
        elif javob2 < javob:
            print(f"men yutdim {javob} ta  urunishda topganman")
        else : 
            print(f"siz yuddingiz {javob2} ta urunishda topgansiz")
        
        ruhsat = int(input(f"yana oynaymizmi ha(1) yo'q (0)"))
        
ishlat(10)
