import pickle

with  open("../Data/database", 'rb') as file:
    obj1 = pickle.load(file)
    obj2 = pickle.load(file)


print(obj2)