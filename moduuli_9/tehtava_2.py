# Luodaan luokka

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

# Pääohjelma, luodaan olio

uusi_auto = Auto('ABC-123', 142)
uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)

print(f'Auton nopeus tällä hetkellä on {uusi_auto.nopeus_atm} km/h.')

uusi_auto.kiihdyta(-200)

print(f'Auton nopeus tällä hetkellä on {uusi_auto.nopeus_atm} km/h.')