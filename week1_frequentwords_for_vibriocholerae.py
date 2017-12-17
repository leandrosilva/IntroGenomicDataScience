from week1 import PatternCount

def FrequentWordsWithLog(Text, k):
    textLength = len(Text)
    
    kmerCounts = {}    
    maxCount = 0

    for i in range(textLength - k + 1):
        pattern = Text[i : i + k] # an actual k-mer
        if not pattern in kmerCounts:
            count = PatternCount(Text, pattern)
            kmerCounts[pattern] = count
            print("i:", i, ", pattern:", pattern, ", count:", count)
            if count > maxCount:
                maxCount = count
        else:
            print("i:", i, ", pattern:", pattern, " <DONE>")

    frequentPatterns = {}
    for kmer in kmerCounts:
        if kmerCounts[kmer] == maxCount:
            frequentPatterns[kmer] = maxCount
    
    return frequentPatterns

def TestFrequentWordsForVibrioCholerae():
    print("\nTest >> FrequentWords for Vibrio cholerae bacteria")
    
    with open("Vibrio_cholerae.txt", "r") as genomeFile:
        frequentPatterns = FrequentWordsWithLog(genomeFile.readline(), 9)

    print("Patterns:", frequentPatterns)

if __name__ == '__main__':
    TestFrequentWordsForVibrioCholerae()