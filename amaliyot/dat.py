import datetime as dt

##  1 ) bugundan boshlap 2 hafta oraligi bilan 10 ta sana chiqarish
# bugun = dt.date.today()
# count = 0

# while count <10 :
#     print(bugun)
#     sana += dt.timedelta(days=14)
#     count+=1        

# 2) tugulgan kunga nechi kun va oy qoldi 
birthday = dt.date(2026 , 4 , 29)
today = dt.date.today()
days = (birthday-today).days
print(f"{days} kun qoldi")
print(f"{days/30.44} oy qoldi")

