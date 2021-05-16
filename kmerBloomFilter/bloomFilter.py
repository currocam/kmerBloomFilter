import math
import mmh3
from bitarray import bitarray
 
 
class BloomFilter():
 
    def __init__(self, m, p):
        '''
        m : int
            Número de secuencias esperadas.
        p : float
            Probabilidad aceptable de falso positivo.
        '''
        self.n = self.get_n(m, p)
        self.h = self.get_h(self.n, m)
        self.bitArray = bitarray(self.n)
        self.bitArray.setall(0)
        
    @classmethod
    def get_n(self, m, p):
        n = -(m * math.log(p))/(math.log(2)**2) #Wikipedia
        return int(n)
 
    @classmethod
    def get_h(self, n, m):
        k = (n/m) * math.log(2)
        return int(k)
    
    def info(self):
        print('Este BloomFilter tiene {0} bits'.format(self.n))    
        print('Este BloomFilter tiene {0} funciones hash'.format(self.h))
        
    def add(self, string):
        for i in range(self.h):
            index=mmh3.hash(string, i) % self.n
            self.bitArray[index] = True
 
    def check(self, string):
        for i in range(self.h):
            index = mmh3.hash(string, i) % self.n
            if self.bitArray[index] == False:
                return False
        return True
    
    def register(self, string):
        '''
        Comprueba si la secuencia está presente y, de no estarlo, la añade. 
        '''
        if not self.check(string):
            self.add(string)
            return False
        else:
            return True

if __name__ == "__main__":
    seq1 = 'AAAATGGC'
    seq2 = 'CGCGCGCGTA'
    
    bf=BloomFilter(2, 0.01)
    bf.info()
    
    print(bf.check(seq1))
    print(bf.register(seq2))
    
    bf.add(seq1)
    print(bf.check(seq2))
    print(bf.check(seq1))
