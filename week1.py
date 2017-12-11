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
