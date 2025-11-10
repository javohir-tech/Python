# users = []
# def userAdd(name , surname , year , address , email=None , tel=None):
#     user = {
#         "name" : name,
#         "surname" : surname,
#         "birthday" : year,
#         "age" : 2025-year,
#         "address" : address,
#         "email address" : email,
#         "telNumber" : tel
#     }
#     return user

# while True :
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     name = input("Ismingiz : ")
#     surname = input("Familya : ")
#     t_yil = int(input("Tigulgan yilindiz : "))
#     mazil = input("tugulgan joyigiz : ")
#     emailManzil =  input("email manzilingiz : ")
#     telNumber = input("Telefon raqam : ")

#     user = userAdd(name , surname , t_yil, mazil , emailManzil , telNumber);

#     users.append(user)
#     javob = input('davom ettiramizmi (yes/no)');

#     if javob == 'no' :
#         print(users)
#         break


# def maximum(param1, param2, param3):
#     return max(param1, param2, param3)


# res = maximum(1, 2, 3);
# print(res)

# def cercle(radius) :
#     PI = 3.14;
#     return {
#         "radiusi" : radius, 
#         "diametr" : 2*radius, 
#         "perimetr": 2*PI*radius, 
#         "yuzi" : PI*radius**2 
#     }

# javob = int(input("aylana radiusini kiriting : >>>"))
# res = cercle(javob)
# print(res)

def tubSonlarTopish(chegara) : 
    tubSonlar = [];
    i=2;
    while True:
        neto = 0;
        qoshiladigan = i
        for n in range(1 , i) :
            if i % n == 0 :
                neto+=1
            if neto >=2:
                qoshiladigan = 0
                break 
        if qoshiladigan != 0:
            tubSonlar.append(qoshiladigan)
        if len(tubSonlar) == chegara+1 :
            break
        i+=1                
    return tubSonlar 
        
print(tubSonlarTopish(500))
        
