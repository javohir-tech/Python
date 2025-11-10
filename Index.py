users = []
def userAdd(name , surname , year , address , email=None , tel=None):
    user = {
        "name" : name,
        "surname" : surname, 
        "birthday" : year, 
        "age" : 2025-year, 
        "address" : address, 
        "email address" : email, 
        "telNumber" : tel
    }
    users.append(user)
    return user

name = input("Ismingiz : ")
surname = input("Familya : ")
t_yil = int(input("Tigulgan yilindiz : "))
mazil = input("tugulgan joyigiz : ")
emailManzil =  input("email manzilingiz : ")
telNumber = input("Telefon raqam : ")

res =userAdd(name , surname , t_yil, mazil , emailManzil , telNumber);
print(res)