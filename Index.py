# num = int(input("Sonni kiriting"));

# if num % 2== 0:
#     print("raxmat")
# else:
#     print('bu juft son emas')

# age = float(input("Yoshingizni kiriting?"))

# if age <=4 or age>=60 :
#     price = 0
# elif age<=18:
#     price =10000;
# elif age>18:
#     price = 20000;
    
# print(f"Muzeyga kirish narxi {price}")

# a = float(input("Birinchi son"))
# b = float(input("Ikkinchi son"))

# if a==b :
#     print("Ikkala son teng")
# else :
#     katta = max(a, b)
#     kichik = min(a, b)
#     print(f"{kichik}<{katta}")

# mahsulotlar = ['asal' , "kola" , "pepsi" , "snikers" , "gosht" , "pallmal", "caster" , "parlament"];

# savat = []
# bor_mahsulotlar= [];
# mavjud_emas=[]

# for n in range(5) : 
#     item = input("Savatga qoshing ").lower();
#     savat.append(item)

# if savat :
#     for item in savat :
#         if item in mahsulotlar :
#            bor_mahsulotlar.append(item)
#         else: 
#            mavjud_emas.append(item)
#     if len(mavjud_emas)==0:
#         print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#     else :
#           print("quyidagi mahssulotlar dokonimizda yoq")
#           for x in mavjud_emas :
#            print(x)       
# else:
#     print("savat bosh") 

# users= ['javohir' , 'jalol' , "bek" , 'ulugbek' , 'shaxi'];

# login = input("Loginni kiriting     ").lower()

# if login in users :
#     print('login band')
# else: 
#     print('hush kelipsan ')     

num = int(input('<<<Sonni kiriting>>>'));

for n in range(2 , 11):
    if num % n == 0:
        print(f"{num} soni {n} ga qoldiqsiz bo'linadi")
        
    