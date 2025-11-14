import unittest
from fullname import fullName

class TestFullname(unittest.TestCase):
    def test_fullname(self) :
        res = fullName('Javohir' , 'suvonov')
        self.assertEqual(res , "Javohir Suvonov")
    
    def test_toliq_ism(self) :
        res = fullName("Javohir" ,"suvonov" , "Alimardon")
        self.assertEqual(res , "Javohir Alimardon Suvonov") 
        
        
if __name__ == "__main__" :
    unittest.main()
    