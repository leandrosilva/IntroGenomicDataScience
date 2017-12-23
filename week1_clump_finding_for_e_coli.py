def ClumpFindingWithLog(Genome, k, L, t):
    genomeLenth = len(Genome)

    kmers = []
    for i in range(genomeLenth - L + 1):
        print("i:", i, ", WINDOW")
        genomeWindow = Genome[i : i + L]
        kmerCounter = {}
        for z in range(L - k + 1):
            kmer = genomeWindow[z : z + k]
            if not kmer in kmers:
                if kmer in kmerCounter:
                    kmerCount = kmerCounter[kmer] + 1
                else:
                    kmerCount = 1
                kmerCounter[kmer] = kmerCount
                print("z:", z, ", kmer:", kmer, ", count:", kmerCount)
                if kmerCount == t:
                    kmers.append(kmer)
            else:
                print("z:", z, ", kmer:", kmer, "<DONE>")

    return kmers

def TestClumpFindingForEColi():
    print("\nTest >> ClumpFinding for E. coli bacteria")
    
    with open("E_coli.txt", "r") as genomeFile:
        clumps = ClumpFindingWithLog(genomeFile.readline(), 9, 500, 3)

    print("Clumps:", clumps)

if __name__ == '__main__':
    TestClumpFindingForEColi()
