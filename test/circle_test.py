import unittest
from circle import get_perimetr, get_area

class TestCircle(unittest.TestCase):
    def test_circle_ares(self) :
        self.assertAlmostEqual(get_area(5) , 78.54 ,2)
        
    def test_circle_perimetr(self) :
        self.assertAlmostEqual(get_perimetr(5) , 31.42, 2)
        

if __name__=="__main__" :
    unittest.main()
    