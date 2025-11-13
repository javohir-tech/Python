import unittest
from name import get_fullname

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        res = get_fullname('javohiR' , 'suvonov')
        self.assertEqual(res , "Javohir Suvonov")
        
    def test_otasi(self) :
        res = get_fullname("javohir" , 'suvonov' , 'alimardon')
        self.assertEqual(res , "Javohir Alimardon Suvonov")
        

unittest.main()


