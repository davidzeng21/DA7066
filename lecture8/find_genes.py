#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

def read_fasta(f):
    seqs = {}
    for line in f:
        if line[0] == ">":
            acc = line.strip()
            seqs[acc] = ''
        else:
            seqs[acc] += line.strip()
    return seqs


def get_kmer_windows(seq, w):
    return [seq[i:i+w] for i in range(len(seq) - w +1)]


def estimate_gc(kmers):
    return [(kmer.count('C') + kmer.count('G')) / len(kmer) for kmer in kmers]


def get_gene_regions(gc_fractions, threshold):
    regions = []
    curr_region_start = 0
    for i in range(len(gc_fractions) - 1):
        # gene region starts
        if gc_fractions[i] < threshold and gc_fractions[i+1] >= threshold:
            curr_region_start = i+1
        # gene region is over
        elif gc_fractions[i] >= threshold and gc_fractions[i+1] < threshold:
            regions.append( (curr_region_start, i+1) )
    return regions


def print_results(chr_id, regions):
    for start, stop in regions:
        print(chr_id, start, stop)
    
def reverse_complement(seq):
    return seq.translate(str.maketrans("ACGT", "TGCA"))[::-1]

def main(args):
    try:
        assembly = read_fasta(args.assm_file)
    except:
        print("There was an error related to parsing of fasta file. Please check the formatting of the file")

    for chr_id, seq in assembly.items():
        if args.verbose:
            print("Processing chromosome {0}".format(chr_id))
        kmers = get_kmer_windows(seq, args.w) # returns list of k-mers in order
        gc_fractions = estimate_gc(kmers) # estimates GC content per kmer, returns list of floats
        regions = get_gene_regions(gc_fractions, args.gc_fraction)
        print_results(chr_id, regions)
        
        if args.use_rc:
            kmers = get_kmer_windows(reverse_complement(seq), args.w) # returns list of k-mers in order
            gc_fractions = estimate_gc(kmers) # estimates GC content per kmer, returns list of floats
            regions = get_gene_regions(gc_fractions, args.gc_fraction)
            print_results(chr_id, regions)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find gene region \
    in a genome assembly through GC content.", \
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--w', type=int, default = 50,
    help='Window size to calculate GC content from')
    parser.add_argument('--gc_fraction', type=float, default = 0.7,
    help='Threshold for GC content to define gene region')
    parser.add_argument('assm_file', type=argparse.FileType('r'),
    help='input assembly file')
    parser.add_argument('outfile', type=argparse.FileType('w'),
    help='Output CSV-file')
    parser.add_argument('--use_rc', action="store_true",
    help='Use also reverse complements to find genes')
    parser.add_argument('--verbose', action="store_true",
    help='Pring diagnostic output to terminal (stdout)')
    args = parser.parse_args()
    main(args) # Call the main function if run from terminal