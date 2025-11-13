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
# except:
#     print(f"bizda faqat {len(arr)} ta meva bor")

# ^^^^^^^^^^^^^^^^^ KeyError ^^^^^^^^^^^^^^^^
user = {
    "name": "Javohir Suvonov",
    "tel": "+998771232904",
    "email" : "suvonovjavohir625@gmail.com"
}

key = "email"
try:
    res = user[key]
    print(res)
except:
    print(f" foydalanuvchini {key} malumoti kiritilmagan");
    
