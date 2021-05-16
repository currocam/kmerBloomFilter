from bloomFilter import BloomFilter
from Bio import SeqIO, Seq, SeqRecord
import pandas as pd 

m = 160000 
p = 0.01 
k=40

bf = BloomFilter(m,p)
bf.info()

kmersDict={}

for read in SeqIO.parse("sequence.fasta", "fasta"):
    string=str(read.seq) 
    nkmers= len(string)-k+1
    if nkmers >=0:
        for i in range(nkmers):
            kmer=string[i:k+i]
            if bf.register(kmer):
                kmersDict[kmer] = kmersDict.get(kmer, 1) + 1
df = pd.DataFrame(list(kmersDict.items()),columns = ['kmer','count'])
df.to_csv ('kmer_count_bloom.csv', index = False, header=True)
