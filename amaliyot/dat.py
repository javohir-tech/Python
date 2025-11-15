import datetime as dt
import re

##  1 ) bugundan boshlap 2 hafta oraligi bilan 10 ta sana chiqarish
# bugun = dt.date.today()
# count = 0

# while count <10 :
#     print(bugun)
#     sana += dt.timedelta(days=14)
#     count+=1        

# 2) tugulgan kunga nechi kun va oy qoldi 
# birthday = dt.date(2026 , 4 , 29)
# today = dt.date.today()
# days = (birthday-today).days
# print(f"{days} kun qoldi")
# print(f"{days/30.44} oy qoldi")

## 3) foydalanuvchidan raqamini olish
# msg = "Raqamizni kiriting . "
# phoneAndoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

# while True:
#     res = input(msg)
#     if re.match(phoneAndoza , res):
#         print("qabul qilindi")
#         break
#     else:
#         print("qayta kirit dabba")

## 4) mathdan manzilni olish

matn = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI

Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

pathAndoza = r"https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[\w\-]*)*"

paths = re.findall(pathAndoza , matn)
for p in paths :
    print(p)