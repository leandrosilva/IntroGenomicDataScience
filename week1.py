def PatternCount(Text, Pattern):
    textLength = len(Text)
    k = len(Pattern)

    count = 0
    for i in range(textLength - k + 1):
        kmer = Text[i : i + k]
        if (kmer == Pattern):
            count += 1

    return count

def FrequentWords(Text, k):
    textLength = len(Text)
    
    kmerCounts = {}    
    maxCount = 0

    for i in range(textLength - k + 1):
        pattern = Text[i : i + k] # an actual k-mer
        if not pattern in kmerCounts:
            count = PatternCount(Text, pattern)
            kmerCounts[pattern] = count
            if count > maxCount:
                maxCount = count

    frequentPatterns = []
    for kmer in kmerCounts:
        if kmerCounts[kmer] == maxCount:
            frequentPatterns.append(kmer)
    
    return frequentPatterns

def ReverseComplement(Pattern):
    complementaryStrands = { "A": "T", "G": "C", "T": "A", "C": "G" }

    complementaryStrand = ""
    for strand in Pattern:
        complementaryStrand += complementaryStrands[strand]

    return complementaryStrand[::-1]

def PatternMatching(Pattern, Genome):
    genomeLength = len(Genome)
    k = len(Pattern)

    kmerPositions = []
    for i in range(genomeLength - k + 1):
        kmer = Genome[i : i + k]
        if (kmer == Pattern):
            kmerPositions.append(i)

    return kmerPositions

def TestPatternCount():
    print("\nTest >> PatterCount")

    output = PatternCount("GCGCG", "GCG")
    if (output == 2): print("Test 0: OK")
    else: print("Test 0: FAIL")

    output = PatternCount("ACGTACGTACGT", "CG")
    if (output == 3): print("Test 1: OK")
    else: print("Test 1: FAIL")

    output = PatternCount("AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT", "AAA")
    if (output == 4): print("Test 2: OK")
    else: print("Test 2: FAIL")

    output = PatternCount("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", "TTT")
    if (output == 4): print("Test 3: OK")
    else: print("Test 3: FAIL")

    output = PatternCount("GGACTTACTGACGTACG", "ACT")
    if (output == 2): print("Test 4: OK")
    else: print("Test 4: FAIL")

    output = PatternCount("ATCCGATCCCATGCCCATG", "CC")
    if (output == 5): print("Test 5: OK")
    else: print("Test 5: FAIL")
    
    output = PatternCount("CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA", "CTC")
    if (output == 9): print("Test 6: OK")
    else: print("Test 6: FAIL")

def TestFrequentWords():
    print("\nTest >> FrequentWords")

    output = FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
    if (len(output) == 2) and ("CATG" in output and "GCAT" in output): print("Test 0: OK")
    else: print("Test 0: FAIL")

    output = FrequentWords("TGGTAGCGACGTTGGTCCCGCCGCTTGAGAATCTGGATGAACATAAGCTCCCACTTGGCTTATTCAGAGAACTGGTCAACACTTGTCTCTCCCAGCCAGGTCTGACCACCGGGCAACTTTTAGAGCACTATCGTGGTACAAATAATGCTGCCAC", 3)
    if (len(output) == 1) and ("TGG" in output): print("Test 1: OK")
    else: print("Test 1: FAIL")

    output = FrequentWords("CAGTGGCAGATGACATTTTGCTGGTCGACTGGTTACAACAACGCCTGGGGCTTTTGAGCAACGAGACTTTTCAATGTTGCACCGTTTGCTGCATGATATTGAAAACAATATCACCAAATAAATAACGCCTTAGTAAGTAGCTTTT", 4)
    if (len(output) == 1) and ("TTTT" in output): print("Test 2: OK")
    else: print("Test 2: FAIL")

    output = FrequentWords("ATACAATTACAGTCTGGAACCGGATGAACTGGCCGCAGGTTAACAACAGAGTTGCCAGGCACTGCCGCTGACCAGCAACAACAACAATGACTTTGACGCGAAGGGGATGGCATGAGCGAACTGATCGTCAGCCGTCAGCAACGAGTATTGTTGCTGACCCTTAACAATCCCGCCGCACGTAATGCGCTAACTAATGCCCTGCTG", 5)
    if (len(output) == 1) and ("AACAA" in output): print("Test 3: OK")
    else: print("Test 3: FAIL")
    
    output = FrequentWords("CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC", 5)
    if (len(output) == 3) and ("AAAAT" in output and "GGGGT" in output and "TTTTA" in output): print("Test 4: OK")
    else: print("Test 4: FAIL")

def TestReverseComplement():
    print("\nTest >> ReverseComplement")

    output = ReverseComplement("AAAACCCGGT")
    if (output == "ACCGGGTTTT"): print("Test 0: OK")
    else: print("Test 0: FAIL")

    output = ReverseComplement("ACACAC")
    if (output == "GTGTGT"): print("Test 1: OK")
    else: print("Test 1: FAIL")

def TestPatternMatching():
    print("\nTest >> PatternMatching")

    output = PatternMatching("ATAT", "GATATATGCATATACTT")
    if (output == [1, 3, 9]): print("Test 0: OK")
    else: print("Test 0: FAIL")

    output = PatternMatching("ACAC", "TTTTACACTTTTTTGTGTAAAAA")
    if (output == [4]): print("Test 1: OK")
    else: print("Test 1: FAIL")
    
    output = PatternMatching("AAA", "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT")
    if (output == [0, 46, 51, 74]): print("Test 2: OK")
    else: print("Test 2: FAIL")
    
    output = PatternMatching("TTT", "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT")
    if (output == [88, 92, 98, 132]): print("Test 3: OK")
    else: print("Test 3: FAIL")
    
    output = PatternMatching("ATA", "ATATATA")
    if (output == [0, 2, 4]): print("Test 4: OK")
    else: print("Test 4: FAIL")

def TestPatternMatchingForVibrioCholerae():
    print("\nTest >> PatternMatchingForVibrioCholerae")
    
    genome = open("Vibrio_cholerae.txt", "r").readline()
    kmerPositions = PatternMatching("CTTGATCAT", genome)

    print("Starting positions:", kmerPositions)
    
if __name__ == '__main__':
    TestPatternCount()
    TestFrequentWords()
    TestReverseComplement()
    TestPatternMatching()
    TestPatternMatchingForVibrioCholerae()