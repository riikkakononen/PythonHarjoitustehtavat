import random

# Luodaan joukko nimien tallentamiseen

nimet = set()

while True:
    nimi = input('Anna nimi tai lopeta painamalla enteriä: ').strip()
    if nimi == '':
        break
    if nimi in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        print('Uusi nimi.')
        nimet.add(nimi)

# Tulostetaan nimet satunnaisessa järjestyksessä
nimilista = list(nimet)
random.shuffle(nimilista)
print('\nSyötetyt nimet satunnaisessa järjestyksessä: ')
for n in nimilista:
    print(n)