class Car :
    def __init__(self , make , model , year , color , price , km =0):
        self.make =  make
        self.model = model;
        self.year = year ;
        self.color = color
        self.price = price
        self.__km = km

    def __str__(self):
        return f"{self.model} narxi : {self.price}"

    def __repr__(self):
        return f"{self.model} narxi : {self.price}"
    
    def __eq__(x, y):
        return x.price == y.price
    
    def __lt__(x,y):
        return x.price < y.price
    
    def __le__(x,y):
        return x.price <= y.price
        
car1 = Car("GM" , "Nexia" ,2015 , "Mokri" , 5000, 450000)
car2 = Car("GM" , "Laceti" ,2018 , "Mokri" , 7000, 250000)
# print(car1)
# print(repr(car1))
# print(car1 == car2)
print(car1 <= car2)

        