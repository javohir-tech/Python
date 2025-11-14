from uuid import uuid4


class Avto:
    __num_avto = 0

    def __init__(self, make, model, rang, yil, narx=None, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    @classmethod
    def get_avto_num(cls):
        return cls.__num_avto

    def add_price(self, price):
        self.narx = price

    def get_km(self):
        return self.__km

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("Mashinani km ni kamaytirip bo'lmaydi!!!")
            
    def get_info(self):
        info = f"{self.make.upper()} {self.model.upper()} , "
        info += f"{self.yil}-yil, {self.__km} km yurgan ."
        if self.narx :
            info += f"narxi {self.narx}"
        return info
        