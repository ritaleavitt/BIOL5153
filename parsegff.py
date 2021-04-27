#! /usr/bin/env python3

import csv
import argparse
import re
import numpy as np
from Bio import SeqIO

# This script will parse a GFF file and extract each feature from the genome
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)


# Create and argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

# initializes arrays of exon names and sequences
np_name = np.array([])
np_seq = np.array([])

#Create a function for reverse complements
def rev_comp(genome, strand):
    if strand == '-':
        print(feature)
        print(genome.seq[start:end].reverse_complement())
    else:
        print(feature)
        print("On the '+' strand")


# open and read in GFF file
with open(args.gff, 'r') as gff_in:

    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    # loop over all the lines in our reader object, i.e. parsed file
    for line in reader:
        species = line[0]
        start = int(line[3]) - 1
        end = int(line[4]) + 1
        feature = line[8]
        strand = line[6]
        cds = line[2]
        # finds all the exons
        if 'CDS' in cds :
            # print(species, feature)
            # finds the name and exon number for each exon
            name = re.findall(r"Gene\s\S+\s*e*x*o*n*\s*\d*", feature)
            # creates an array of exon names
            np_name = np.append(np_name, name)
            # creates an array of the exon sequences
            np_seq = np.append(np_seq, str(genome.seq[start:end]))

# Creates a paired array of exon name and sequence
np_exon = np.stack((np_name, np_seq), axis=-1)
# Sorts the exons alphabetically by name
np_exon = np_exon[np.argsort(np_exon[:, 0])]
print(np_exon)
# I'll come back to this and finish it if I can, but this assignment is late as it is, so you may need to grade what's here.
# I'm kind of stuck, but I'll say what I intended to do next, if I could figure it out
# Now that I have the exon name (and number, where applicable) sorted alphabetically,
# I was going to use a loop to compare the names of each subsequent value,
# using another regex to separate, say 'Gene nad7 exon 1' from 'Gene nad7 exon 2'
# and concatenate the sequence for all exons from the same gene in a new array.
# Then create another loop to print the new array values along with the species name