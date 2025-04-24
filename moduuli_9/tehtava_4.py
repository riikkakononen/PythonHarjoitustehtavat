# Luodaan luokka
import random

class Auto:

    # Metodit

    def __init__(self, r_tunnus, max_nopeus):
        self.rekisteritunnus = r_tunnus
        self.huippunopeus = max_nopeus
        self.kuljettu_matka = 0
        self.nopeus_atm = 0

    def kiihdyta(self, nopeuden_muutos):
        if self.nopeus_atm + nopeuden_muutos < 0:
            self.nopeus_atm = 0 # Varmistetaan, että auton nopeus ei ole negatiivinen.
        elif self.nopeus_atm + nopeuden_muutos <= self.huippunopeus:
            self.nopeus_atm += nopeuden_muutos # Lisätään (tai vähennetään) nopeuden muutos tämänhetkiseen nopeuteen.
        else:
            self.nopeus_atm = self.huippunopeus # Auton nopeus ei voi mennä yli huippunopeuden.

    # Auto kulkee tasaisesti sillä vauhdilla, joka sille on viimeiseksi annettu.
    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus_atm * tunnit



# Pääohjelma

autot = []

for a in range(10):
    autot.append(Auto(f'ABC-{a+1}', random.randrange(100,201)))

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        auto.kiihdyta(random.randrange(-10, 16))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False



# Järjestetään taulukko

# key parametrille annetaan arvo lambda, joka tarkoittaa nimetöntä funktiota, tällä välitetään funktioita toisille funktioille
autot.sort(key=lambda a: a.kuljettu_matka, reverse=True) #reverse=True järjestää listan suurimmasta pienimpään

# Tulostetaan tiedot

print(f'{"Rekisteritunnus":20} {"Huippunopeus":20} {"Matka (km)":20} {"Nopeus (km/h)":20}')
for auto in autot:
    print(f'{auto.rekisteritunnus:20} {auto.huippunopeus:<20} {auto.kuljettu_matka:<20} {auto.nopeus_atm:<20}')