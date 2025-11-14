import unittest
from  avto import Avto

class TestAvto(unittest.TestCase) :
    def setUp(self):
        make = 'GM',
        model = 'Malibu'
        rang = 'qora'
        yil = 2020
        self.price = 20000
        self.km = 10000
        self.avto1 = Avto(make ,  model , rang , yil);
        self.avto2 = Avto(make, model, rang , yil, self.price);

    def test_create(self) :
        # hususiyatlarni mavjudligini tekshirish
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.rang)
        self.assertIsNotNone(self.avto1.yil)
        # hususiyatlarni mavjud measligini aniqlash
        self.assertIsNone(self.avto1.narx)
        #km ni tekshiiramiz
        self.assertEqual(0 , self.avto1.get_km())
        # avto 2 ni qiymatini tekshiramiz
        self.assertEqual(self.price , self.avto2.narx)
        
    def test_price(self) :
        self.avto2.add_price(self.price)
        self.assertEqual(self.avto2.narx , self.price)
        
    def test_km(self) :
        self.avto1.add_km(self.km)
        self.assertEqual(self.avto1.get_km() , self.km)
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error) , ValueError)
        self.avto1.add_km(5000)
        self.assertEqual(self.avto1.get_km(), 15000)
    
        
unittest.main()