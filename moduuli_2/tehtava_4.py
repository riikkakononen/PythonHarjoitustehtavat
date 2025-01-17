print('Anna kolme kokonaislukua.')

luku1 = int(input('Ensimmäinen kokonaisluku: '))
luku2 = int(input('Toinen kokonaisluku: '))
luku3 = int(input('Kolmas kokonaisluku: '))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print(f'Kokonaislukujen summa: {summa}, tulo: {tulo} ja keskiarvo: {keskiarvo:0.0f}')