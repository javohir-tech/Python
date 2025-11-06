import math
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 

# for car in cars : 
#     if car.lower() !=  'gm' : 
#         # car.upper() 
#         print(car.title())
#     else : 
#         # car.title()
#         print(car.upper())
        
# login = input('Loginni kiriting ');
# if login.lower() == 'admin' :
#     print('Xush kelibsiz, Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi?')
# else:
#     print(f"hush kelipsiz {login}")
    
# a= int(input('a sonni kiriting '))
# b= int(input('b sonni kiriting '))
# if a==b : 
#     print('sonlar teng');

# javob = int(input('sonni kiriting'));
# if javob <0:
#     print('son manfiy');
# else:
#     print('son musbat')

javob = int(input('Sonni kiritng '));

if javob >=0 :
    print(int(math.sqrt(javob)))
else: 
    print('Musbat son kiriting ')
    