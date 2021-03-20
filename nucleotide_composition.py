#! /usr/bin/env python3

# This script calculates the nucleotide composition of a DNA sequence

# Assign the DNA sequence variable
dna_sequence = 'ACGGATCCTATCAAATATTTCACATTTTCTATGATCATCTCTATTTTAGGTATTCGGGGAATCCTCCTTAATAGACGAAATATTCCTATTATGTCAATGCCAATTGAATCAATGTTATTAGCTGTGAATTCGAACTTTTTGGTATTTTCCGTTTCTTCGGATGATATGATGGGTCAATCATTTGCTTCATTGGTTCCAACGGTGGCAGCTGCGGAATCCGCTATTGGGTTAGCCATTTTCGTTATTACTTTCCGAGTCCGAGGGACTATTGCTGTAGAATTTATTAATAGCATTCAAGGTTAA'

# Finds the sequence length and prints it
seqlen = len(dna_sequence)
print('The sequence length is: ' + str(seqlen))

# Finds the number of A's, C's, G's and T's in the sequence
numA = dna_sequence.count('A')
numC = dna_sequence.count('C')
numG = dna_sequence.count('G')
numT = dna_sequence.count('T')

# Finds the frequencies of A, C, G, and T
freqA = numA/seqlen
freqC = numC/seqlen
freqG = numG/seqlen
freqT = numT/seqlen

# Prints the frequency of A's, C's, G's and T's in the sequence
print('The frequency of A: ' + str(freqA))
print('The frequency of C: ' + str(freqC))
print('The frequency of G: ' + str(freqG))
print('The frequency of T: ' + str(freqT))
# Prints the G + C content
print('G + C content: ' + str(freqC + freqG))

# Checks that the frequencies sum to one
freqsum = ((numA + numC + numG + numT)/seqlen)
print('The frequency sum should equal 1')
print('The frequency sum is: ' + str(freqsum))
