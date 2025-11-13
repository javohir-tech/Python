import pickle

with open('../Data/database' , 'rb') as file :
    obj1 = pickle.load(file);
    obj2 = pickle.load(file);
    # obj3 = pickle.load(file); #EOFError End of File ya'ni faylni oxiriga yetp qoldim degan hato
    
print(obj1)
print(obj2)