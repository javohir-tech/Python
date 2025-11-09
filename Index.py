# print("Kiritilgan sonning kvadratini qaytaruvchi dastur");

# savol = "Istalgan son kiriting";
# savol+= "(dasturni to'xtatish uchun 'exit' deb yozing) : ";
# flag = True
# while flag:
#          qiymat = input(savol)
#          if qiymat == 'exit':
#              break
#          else:
#              print(float(qiymat)**2)

# for n in range(1, 11) :
#     if n == 5 :
#         continue
#     print(n**2)
    
son = 0;

while son < 10 : 
    son+=1
    if son == 3 :
        continue
    else: 
        print(son**2)