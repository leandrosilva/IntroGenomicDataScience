import unittest
from week1 import FrequentWords

class Week1FrequentWordsTest(unittest.TestCase):
    
    def test_0(self):
        output = FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
        self.assertEqual(len(output), 2)
        self.assertTrue("CATG" in output)
        self.assertTrue("GCAT" in output)
    
    def test_1(self):
        output = FrequentWords("TGGTAGCGACGTTGGTCCCGCCGCTTGAGAATCTGGATGAACATAAGCTCCCACTTGGCTTATTCAGAGAACTGGTCAACACTTGTCTCTCCCAGCCAGGTCTGACCACCGGGCAACTTTTAGAGCACTATCGTGGTACAAATAATGCTGCCAC", 3)
        self.assertEqual(len(output), 1)
        self.assertTrue("TGG" in output)
    
    def test_2(self):
        output = FrequentWords("CAGTGGCAGATGACATTTTGCTGGTCGACTGGTTACAACAACGCCTGGGGCTTTTGAGCAACGAGACTTTTCAATGTTGCACCGTTTGCTGCATGATATTGAAAACAATATCACCAAATAAATAACGCCTTAGTAAGTAGCTTTT", 4)
        self.assertEqual(len(output), 1)
        self.assertTrue("TTTT" in output)
    
    def test_3(self):
        output = FrequentWords("ATACAATTACAGTCTGGAACCGGATGAACTGGCCGCAGGTTAACAACAGAGTTGCCAGGCACTGCCGCTGACCAGCAACAACAACAATGACTTTGACGCGAAGGGGATGGCATGAGCGAACTGATCGTCAGCCGTCAGCAACGAGTATTGTTGCTGACCCTTAACAATCCCGCCGCACGTAATGCGCTAACTAATGCCCTGCTG", 5)
        self.assertEqual(len(output), 1)
        self.assertTrue("AACAA" in output)
    
    def test_4(self):
        output = FrequentWords("CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC", 5)
        self.assertEqual(len(output), 3)
        self.assertTrue("AAAAT" in output)
        self.assertTrue("GGGGT" in output)
        self.assertTrue("TTTTA" in output)

if __name__ == '__main__':
    unittest.main()