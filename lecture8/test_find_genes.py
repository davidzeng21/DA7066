import find_genes
seq1 = 'AGCTGGCT'
seq2 = 'GGTC' #Unexpected short seq
seq_empty = '' # dont forget corner cases
w_3 = 3
w_zero = 0 # Bad user parameter
w_long = 5 # Longer than seq2 
w_type = '2' # something else unexpected

assert find_genes.get_kmer_windows(seq1, w_3) == ['AGC','GCT','CTG','TGG','GGC','GCT']
assert find_genes.get_kmer_windows(seq1, w_long) == ['AGCTG','GCTGG', 'CTGGC','TGGCT']
assert find_genes.get_kmer_windows(seq2, w_long) == []
# ... ev. more suitable tests here...

kmers = ['AGCTG','GCTGG', 'CTGGC','TGGCT']
kmers2 = ['AGC','GCT','CTG','TGG','GGC','GCT']
kmers_empty = [] # dont forget corner cases

assert find_genes.estimate_gc(kmers2) == [2/3, 2/3, 2/3,2/3, 1.0, 2/3]
assert find_genes.estimate_gc(kmers) == [0.6, 0.8, 0.8, 0.6]
assert find_genes.estimate_gc(kmers_empty) == []