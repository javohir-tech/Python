class Talaba :
    def __init__(self , ism , familya , tyil):
        self.name = ism.title();
        self.surname = familya.title();
        self.byear= tyil
        
    def get_name(self) :
        return self.name
    
talaba1 = Talaba("Javohir", "Suvonov" , 2004)
print(talaba1.name)
print(talaba1.get_name())