'''
Pattern Counting Problem: ﻿Count the number of times a string appears as a substring in a longer text.
     Input: Strings Text and Pattern.
     Output: Count(Text, Pattern).
'''
def PatternCount(Text, Pattern):
    textLength = len(Text)
    k = len(Pattern)

    count = 0
    for i in range(textLength - k + 1):
        kmer = Text[i : i + k]
        if kmer == Pattern:
            count += 1

    return count

'''
Frequent Words Problem: Find the most frequent k-mers in a string.
     Input: A string Text and an integer k.
     Output: All most frequent k-mers in Text.
'''
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

'''
Reverse Complement Problem: Find the reverse complement of a DNA string.
     Input: A DNA string Pattern.
     Output: Patternrc , the reverse complement of Pattern.
'''
def ReverseComplement(Pattern):
    complementaryStrands = { "A": "T", "G": "C", "T": "A", "C": "G" }

    complementaryStrand = ""
    for strand in Pattern:
        complementaryStrand += complementaryStrands[strand]

    return complementaryStrand[::-1]

'''
Pattern Matching Problem: Find all occurrences of a pattern in a string.
     Input: Two strings, Pattern and Genome.
     Output: All starting positions where Pattern appears as a substring of Genome.
'''
def PatternMatching(Pattern, Genome):
    genomeLength = len(Genome)
    k = len(Pattern)

    kmerPositions = []
    for i in range(genomeLength - k + 1):
        kmer = Genome[i : i + k]
        if kmer == Pattern:
            kmerPositions.append(i)

    return kmerPositions

'''
Clump Finding Problem: Find patterns forming clumps in a string.
     Input: A string Genome, and integers k, L, and t.
     Output: All distinct k-mers forming (L, t)-clumps in Genome.
'''
def ClumpFinding(Genome, k, L, t):
    genomeLenth = len(Genome)

    kmers = []
    for i in range(genomeLenth - L + 1):
        genomeWindow = Genome[i : i + L]
        kmerCounted = []
        for z in range(L - k + 1):
            kmer = genomeWindow[z : z + k]
            if not kmer in kmers and not kmer in kmerCounted:
                kmerCount = PatternCount(genomeWindow, kmer)
                kmerCounted = kmer
                if kmerCount == t:
                    kmers.append(kmer)

    return kmers