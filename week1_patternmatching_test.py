import unittest
from week1 import PatternMatching

class Week1PatternMatchingTest(unittest.TestCase):
    
    def test_0(self):
        output = PatternMatching("ATAT", "GATATATGCATATACTT")
        self.assertEqual(output, [1, 3, 9])
    
    def test_1(self):
        output = PatternMatching("ACAC", "TTTTACACTTTTTTGTGTAAAAA")
        self.assertEqual(output, [4])
        
    def test_2(self):
        output = PatternMatching("AAA", "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT")
        self.assertEqual(output, [0, 46, 51, 74])

    def test_3(self):
        output = PatternMatching("TTT", "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT")
        self.assertEqual(output, [88, 92, 98, 132])

    def test_4(self):
        output = PatternMatching("ATA", "ATATATA")
        self.assertEqual(output, [0, 2, 4])

    def test_5(self):
        with open("Vibrio_cholerae.txt", "r") as genomeFile:
            output = PatternMatching("CTTGATCAT", genomeFile.readline())
        self.assertEqual(output, [60039, 98409, 129189, 152283, 152354, 152411, 163207, 197028, 200160, 357976, 376771, 392723, 532935, 600085, 622755, 1065555])

if __name__ == '__main__':
    unittest.main()