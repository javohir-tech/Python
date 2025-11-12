class Talaba :
    def __init__(self , ism , familya , tyil):
        self.name = ism.title();
        self.surname = familya.title();
        self.byear= tyil
        self.kurs = 1
        
    def set_kurs(self , kurs):
        self.kurs = kurs
                
    def update_kurs(self):
        self.kurs+=1
                
    def get_name(self) :
        return self.name
    
    def get_fullname(self): 
        return f"{self.name} {self.surname}"
        
    def get_surname(self):
        return self.surname
    
class Fan : 
    def __init__(self, name ):
        self.name = name;
        self.talaba_soni = 0;
        self.talabalar = []
    
    def add_student(self, talaba) :
        self.talaba_soni+=1
        self.talabalar.append(talaba)
    
    def get_name(self) :
        return self.name
    
    def get_talabalar_soni(self) :
        return self.talaba_soni
    
    def get_students(self) :
        return [talaba.get_fullname() for talaba in self.talabalar ]
    
talaba1 = Talaba("Javohir", "Suvonov" , 2004)
talaba2 = Talaba("Yahyo", "Ergashev" , 2005)

matem = Fan("Matemetika")
matem.add_student(talaba1)
matem.add_student(talaba2)
print(matem.get_students())

# print(talaba1.name)
# print(talaba1.get_name())