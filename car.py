class Car:
    """Moshinalar uchun Obyekt yaratish uchun shablon"""

    def __init__(self, make, model, year, color, price, km=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.__km = km

    # def __str__(self):
    #     """ Shu classdan yaratilgan obyektga print bilan
    #     murojat qilinganda qiymat print uchun qiymat qaytaradigan funksiya """
    #     return f"{self.model} narxi : {self.price}"

    def __repr__(self):
        """
        Shu classdan yaratilgan obyektga print bilan
        murojat qilinganda qiymat print uchun qiymat qaytaradigan funksiya"""
        """ 
        Bu ham shunday lekin bu usul bilan ishlash maslahat beriladi 
        koproq funksiya bilan ishlaydi
        """
        return f"{self.model} narxi : {self.price}"

    def __eq__(self, y):
        """
        Obyektlarni obyetlarni malum bir qiymati yoki properysi 
        bilan solishtirganda teng yoki teng emasligi belgilashda ishlayd
        ob1==obj2 qilinganda ishlaydi
        """
        return self.price == y.price

    def __lt__(x, y):
        """
        Obyektlar katta kichikligini aniqlash vaqtida ishga tushadi obj1<obj2
        vaqtida ihga tushadi va obyektlarnini malum bir qiymati bilan solishtiradi
        """
        return x.price < y.price

    def __le__(x, y):
        """ bu ham shunaqa faqat >= yoki <= holatida ishga tushadi 
        """
        return x.price <= y.price


class Salon:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_cars(self, *qiymat):
        for car in qiymat:
            if isinstance(car, Car):
                self.cars.append(car)
            else:
                print("Bu Avto Clasi bilan yaratilmagan !!!")

    def __getitem__(self, index):
        return self.cars[index]

    def __setitem__(self, index, newValue):
        if isinstance(newValue, Car):
            self.cars[index] = newValue

    def __repr__(self):
        return f"{self.name} saloni"

    def __len__(self):
        return len(self.cars)


salon1 = Salon("Javohir Interprses")

car1 = Car("GM", "Nexia", 2015, "Mokri", 5000, 450000)
car2 = Car("GM", "Laceti", 2018, "Oq", 7000, 250000)

salon1.add_cars(car1, car2)

# print(car1)
# print(repr(car1))
# print(car1 == car2)
# print(car1 <= car2)

# print(len(salon1))
# print(salon1[0])
salon1[0] = Car("GM", "Malibu", 2021, "Qora", 17000, 140000)
print(salon1[0])
