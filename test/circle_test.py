import unittest
from circle import get_perimetr, get_area

class TestCircle(unittest.TestCase):
    def test_circle_ares(self) :
        self.assertEqual(get_area(5) , 78.53981633974483)
        
    def test_circle_perimetr(self) :
        self.assertEqual(get_perimetr(5) , 31.41592653589793)
        

unittest.main()