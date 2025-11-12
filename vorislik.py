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
    def __init__(self , name , surname , passport , tyil , talabaId):
            super().__init__(name, surname , passport, tyil)
            self.talabaId = talabaId
    
    def get_id(self):
        return self.talabaId
    
talaba1 = Talaba("Javohir" , "Suvonov" , "FF010212", 2004 , "HN125635")
print(talaba1.get_info())
print(talaba1.get_age(2025))