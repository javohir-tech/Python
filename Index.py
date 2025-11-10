import random 

sonlar = random.sample(range(100) , 10)

def daraja2(x):
    return x**2

def juftmi(x):
    return x%2==0

kvadratlar = list(map(lambda x : x**2 , sonlar))
juftSonlar = list(filter(lambda x: x%2==0 , sonlar))
# print(kvadratlar)
# print(juftSonlar)

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva : len(meva)<=5, mevalar))
print(mevalar_b)