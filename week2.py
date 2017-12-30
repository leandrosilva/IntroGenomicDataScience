'''
Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.
     Input: A DNA string Genome.
     Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
'''
def MinimumSkew(Genome):
    skew = 0
    minimumSkew = 0
    minimumSkewIndex = 0
    minimizers = []   

    for i in range(len(Genome)):
        nucleotide = Genome[i]
        if nucleotide == "C":
            skew -= 1
            if skew < minimumSkew:
                minimumSkew = skew
                minimumSkewIndex = i + 1
        elif nucleotide == "G":
            skew += 1
            if skew == 0:
                minimizers.append(minimumSkewIndex)
                minimumSkew = 0
                minimumSkewIndex = 0
    
    if minimumSkew < 0 and minimumSkewIndex > 0:
        minimizers.append(minimumSkewIndex)

    if len(minimizers) == 0:
        minimizers.append(0)

    return minimizers