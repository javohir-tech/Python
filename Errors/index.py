# ^^^^^^^^^^^^^^^ ValueError ^^^^^^^^^^^^^^^^^^^^^
# yosh = int(input("Yosh kiritning>>>"))
# print(yosh)
# try :
#     yosh = int(input('Yoshingizni kiriting>>>'))
# except ValueError:
#     print('Butun son kiriting >>>')
# else:
#     print(f"siz {2025-yosh} da tigulgansiz")

# ^^^^^^^^^^^^^^^^^^ ZeroDivisionError ^^^^^^^^^^^^^^^^

# x,y = 7, 10

# try :
#     res = y/(x-5)
# except:
#     print("0 ga bolsih mumkin emas !!!")
# else:
#     print(res)

# ^^^^^^^^^^^^^^^^^ indexError ^^^^^^^^^^^^^^

# arr = ['olma' , 'nok' , 'anor' , 'shaftoli']

# print(arr[4])

# try :
#     res = arr[4]
#     print(res)
# except IndexError:
#     print(f"bizda faqat {len(arr)} ta meva bor")

# ^^^^^^^^^^^^^^^^^ KeyError ^^^^^^^^^^^^^^^^
# user = {
#     "name": "Javohir Suvonov",
#     "tel": "+998771232904",
#     "email" : "suvonovjavohir625@gmail.com"
# }

# key = "email"
# try:
#     res = user[key]
#     print(res)
# except KeyError:
#     print(f" foydalanuvchini {key} malumoti kiritilmagan");
# import json

#^^^^^^^^^^^^^^^^^ FileNotFoundError ^^^^^^^^^^^^^^^^^^^^^^6

# files = ['talaba1.json' , 'talaba3.json', 'talaba2.json']

# for file in files :
#     try:
#         with open(f"../Data/{file}") as f :
#             res = json.load(f)
#     except FileNotFoundError:
#         pass
#     else:
#         print(res['name'])
     
#^^^^^^^^^^^^^^^^^^^^^^^^Ikkita uchta Expect^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   
# n = input('Son kiriitng>>>')

# try :
#     print(20/int(n))
# except ValueError :
#     print("Butun son kiriting !!!")
# except ZeroDivisionError:
#     print('0 ga bolish mumkin emas !!!')

#^^^^^^^^^^^^^^^^^^^^^ While Bilan ^^^^^^^^^^^^^^^^

# while True :
#     age = input("Yosh kiriting >>>")
#     if age.isdigit() :
#         print(f"siz {2025-int(age)} yilda tug'ilgansiz !!!")
#         break
    
