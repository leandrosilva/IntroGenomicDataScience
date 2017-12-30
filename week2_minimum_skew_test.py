
import unittest
from week2 import MinimumSkew

class Week2MinimumSkewTest(unittest.TestCase):
    
    def test_0(self):
        output = MinimumSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT")
        self.assertEqual(output, [11, 24])
        
    def test_1(self):
        output = MinimumSkew("ACCG")
        self.assertEqual(output, [3])
        
    def test_2(self):
        output = MinimumSkew("ACCC")
        self.assertEqual(output, [4])
        
    def test_3(self):
        output = MinimumSkew("CCGGGT")
        self.assertEqual(output, [2])
        
    def test_4(self):
        output = MinimumSkew("CCGGCCGG")
        self.assertEqual(output, [2, 6])
        
    def test_5(self):
        output = MinimumSkew("GGG")
        self.assertEqual(output, [0])
        
    def test_6(self):
        output = MinimumSkew("CGG")
        self.assertEqual(output, [1])

    def test_7(self):
        output = MinimumSkew("CCC")
        self.assertEqual(output, [3])

if __name__ == '__main__':
    unittest.main()