import unittest
from week1 import ReverseComplement

class Week1ReverseComplementTest(unittest.TestCase):
    
    def test_0(self):
        output = ReverseComplement("AAAACCCGGT")
        self.assertEqual(output, "ACCGGGTTTT")
    
    def test_1(self):
        output = ReverseComplement("ACACAC")
        self.assertEqual(output, "GTGTGT")

if __name__ == '__main__':
    unittest.main()