import unittest
from week1 import ClumpFinding

class Week1ClumpFindingTest(unittest.TestCase):
    
    def test_0(self):
        output = ClumpFinding("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4)
        self.assertEqual(len(output), 2)
        self.assertTrue("CGACA" in output)
        self.assertTrue("GAAGA" in output)
    
    def test_1(self):
        output = ClumpFinding("AAAACGTCGAAAAA", 2, 4, 2)
        self.assertEqual(output, ["AA"])
        
    def test_2(self):
        output = ClumpFinding("ACGTACGT", 1, 5, 2)
        self.assertEqual(len(output), 4)
        self.assertTrue("A" in output)
        self.assertTrue("C" in output)
        self.assertTrue("G" in output)
        self.assertTrue("T" in output)
        
    def test_3(self):
        output = ClumpFinding("CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG", 3, 25, 3)
        self.assertEqual(len(output), 6)
        self.assertTrue("AAA" in output)
        self.assertTrue("CAG" in output)
        self.assertTrue("CAT" in output)
        self.assertTrue("CCA" in output)
        self.assertTrue("GCC" in output)
        self.assertTrue("TTC" in output)
    
if __name__ == '__main__':
    unittest.main()