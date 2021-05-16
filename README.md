# kmerBloomFilter
A script to extract all kmers appearing more than once in a given genomic sequence in a fasta file using a Bloom filter (a space-efficient probabilistic data structure). It was created for educational purposes. It is inspired by this [article](https://rdcu.be/ckIkj).

## General info
Given a fasta file, the scripts finds all the n-kmers that appears more than once. This serves to reduce the memory space required, since n-kmers that only appear once in the entire genome (mostly for high values of n) are not stored.

Each kmer is passed through the Bloom Filter, which  returns with a probability p if that kmer have been seen before. 

As a test, we have get all 45-kmers of E. Coli genome using different p values (probability of Positive False) and compute  the accuracy of each run. We observed that for 45-kmers appearing a considerable number of times, this method gives accurate results even with high values of p (therefore low processing requirements). 

![boxplot](images/boxplot.svg)

## Technologies
- Python 3.8.5 
- R 4.0.4
