import random

# Funktio, joka heittää noppaa, jossa on 'tahkoja' määrä tahkoja.
def heitto(tahkoja):
    return random.randint(1,tahkoja)

# Pääohjelma

tahkojen_maara = int(input('Anna nopan tahkojen määrä: '))
maksimi_silmaluku = int(input(f'Anna nopan maksimisilmäluku: (1-{tahkojen_maara}): '))

while True:
    silmaluku = heitto(tahkojen_maara)
    print(silmaluku)
    if silmaluku == maksimi_silmaluku:
        break