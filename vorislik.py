class Shaxs:
    def __init__(self, name, surname, passport, tyil):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        info = f"{self.name} {self.surname} "
        info += f"{self.passport} {self.tyil}"
        return info
    
    def get_age(self , year) :
        return year-self.tyil
    
    
class Talaba(Shaxs) :
    def __init__(self , name , surname , passport , tyil , talabaId, qoshimcha, manzil):
            super().__init__(name, surname , passport, tyil)
            self.talabaId = talabaId
            self.kurs =  1
            self.address= manzil
            self.name = qoshimcha 
    
    def get_id(self):
        return self.talabaId
    
    def get_info(self) :
        info = f"{self.name} {self.surname} "
        info+= f"{self.talabaId} {self.kurs}"
        return info
  
class Manzil :
    def __init__(self, uy, kocha , tuman, viloyat):
        self.home = uy;
        self.street = kocha;
        self.town = tuman;
        self.region = viloyat
    
    def  get_address(self):
        return f"{self.home} {self.street} {self.town} {self.region}"            
    
manzil = Manzil(8 , "yoshlik" , "Angren" , "Toshkent")
talaba1 = Talaba("Javohir" , "Suvonov" , "FF010212", 2004 , "HN125635","Salom",  manzil)
print(talaba1.get_info())
print(talaba1.get_age(2025))
print(talaba1.address.get_address())