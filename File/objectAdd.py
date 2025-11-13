import pickle
obj1 = {"name" : "Javohir" , "surname" : "Suvonov" , "age" :21 , "tyil" : 2004}
obj2 = {"name" : "Yahyo" , "surname" : "Ergashev" , "age" :21 , "tyil" : 2004}

filename = '../Data/database'

with open(filename , 'wb') as file :
    pickle.dump(obj1 , file)
    pickle.dump(obj2, file)
