from uuid import uuid4

class Avto:
    __num_avto = 0 
    def __init__(self, make, model, rang, yil, narx, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto +=1

    @classmethod
    def get_avto_num(cls) :
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Mashinani km ni kamaytirip bo'lmaydi!!!")

