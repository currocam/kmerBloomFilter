from kmerBloomFilter.bloomFilter import *
from Bio import SeqIO, Seq, SeqRecord
import pandas as pd 

prob=[0.0001, 0.001, 0.005, 0.05, 0.1]

for p in prob:
    m = 160000 
    k=45

    bf = BloomFilter(m,p)
    bf.info()

    kmersDict={}

    for read in SeqIO.parse("test/data/sequence.fasta", "fasta"):
        string=str(read.seq) 
        nkmers= len(string)-k+1
        if nkmers >=0:
            for i in range(nkmers):
                kmer=string[i:k+i]
                if bf.register(kmer):
                    kmersDict[kmer] = kmersDict.get(kmer, 1) + 1
    df = pd.DataFrame(list(kmersDict.items()),columns = ['kmer','count'])
    name_file='test/data/kmer_count_'+str(p)+'.csv'
    df.to_csv (name_file, index = False, header=True)
    print('Está terminado ya la probabilidad {0}'.format(p))

