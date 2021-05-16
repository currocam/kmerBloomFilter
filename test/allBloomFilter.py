from Bio import SeqIO, Seq, SeqRecord
import pandas as pd 

k=45
kmersDict={}

for read in SeqIO.parse("test/data/sequence.fasta", "fasta"):
    string=str(read.seq) 
    nkmers= len(string)-k+1
    if nkmers >=0:
        for i in range(nkmers):
            kmer=string[i:k+i]
            kmersDict[kmer] = kmersDict.get(kmer, 0) + 1
df = pd.DataFrame(list(kmersDict.items()),columns = ['kmer','count'])
df.to_csv ('test/data/kmer_countALL.csv', index = False, header=True)
