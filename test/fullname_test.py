import unittest
from fullname import fullName

class FullNameTest(unittest.TestCase) :
    def test_fullname(self) :
        res =  fullName("javohir" , "suvonov")
        self.assertEqual(res , "Javohir Suvonov")
        
    def test_toliq_ism(self) :
        res = fullName("Javohir" , "suvonov" , 'alimardon')
        self.assertEqual(res , "Javohir Alimardon Suvonov")
        
if __name__ == "__main__":
    unittest.main()
    
