import random
import math

N = 0 #Kaikkien arvottujen pisteiden lukumaara
n = 0 #Yksikköympyran sisaan osuneiden pisteiden lkm

arvontojen_lkm = 1000000

while N < arvontojen_lkm:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x ** 2 + y ** 2 < 1:
        n += 1
    N += 1

piin_likiarvo = 4*n/N
print(f'Piin likiarvo on {piin_likiarvo} ja ero tarkkaan {math.pi-piin_likiarvo}')
