import random

# Kysytään käyttäjältä arpakuutioiden lukumäärä

arpakuutiot = int(input('Anna arpakuutioiden lukumäärä: '))

# Muodostetaan silmukka, joka heittää arpakuutiot

lopputulos = 0

for i in range(arpakuutiot):
    heitot = random.randint(1,6) # Heitetään arpakuutio (arvot 1-6)
    lopputulos += heitot # Lisätään heiton tulos kokonaissummaan

# Tulostetaan silmälukujen summa
print('Arpakuutioiden summa on: ', lopputulos)