import unittest
from week1 import PatternCount

class Week1PatternCountTest(unittest.TestCase):
    
    def test_0(self):
        output = PatternCount("GCGCG", "GCG")
        self.assertEqual(output, 2)
    
    def test_1(self):
        output = PatternCount("ACGTACGTACGT", "CG")
        self.assertEqual(output, 3)
    
    def test_2(self):
        output = PatternCount("AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT", "AAA")
        self.assertEqual(output, 4)
    
    def test_3(self):
        output = PatternCount("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", "TTT")
        self.assertEqual(output, 4)
    
    def test_4(self):
        output = PatternCount("GGACTTACTGACGTACG", "ACT")
        self.assertEqual(output, 2)
    
    def test_5(self):
        output = PatternCount("ATCCGATCCCATGCCCATG", "CC")
        self.assertEqual(output, 5)
    
    def test_6(self):
        output = PatternCount("CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA", "CTC")
        self.assertEqual(output, 9)

if __name__ == '__main__':
    unittest.main()