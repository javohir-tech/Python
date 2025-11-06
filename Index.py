# Loops
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar : 
    print(f"hurmatli {mehmon} , sizni 20 dekaabr kuni nahorki oshga taaklif qilamiz")
    print("Hurmat bilan Yusupovlar oilasi\n")
    
sonlar = list(range(1,11))
sonlar_kvadrati  = []
for son in sonlar :
    sonlar_kvadrati.append(son**2);
print(sonlar_kvadrati)

# dostlar = [];
# print("Dostlarni kiriting")
# for n in range(5) : 
#     dost = input(f"{n+1} dostni kiriting")
#     dostlar.append(dost)
# print(dostlar)

names = ['javohir', 'bek', 'yahyo', 'jaahon', 'mansur']

for name in names : 
    print(f"salom {name}")
    
newNums = list(range(10, 101));
for num in newNums :
    print(num**3)
    
kinolar = []
print('sevimli kinolar')
for movie in range(5):
     newMovie = input(f"{movie+1} kino nomini kiriting")
     kinolar.append(newMovie.strip())
print(kinolar)

metting = []
print('bugun kimlar bilan uchrashdiz')
for peopl in range(5):
    meet = input(f"{peopl+1}  odamni kiriting")
    metting.append(meet)
print(metting)