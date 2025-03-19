# Luodaan luokka

class Auto:

    # Funktio

    def __init__(self, r_tunnus, max_nopeus):
        self.rekisteritunnus = r_tunnus
        self.huippunopeus = max_nopeus
        self.nopeus_atm = 0
        self.kuljettu_matka = 0

# Pääohjelma, luodaan olio

uusi_auto = Auto('ABC-123', f'{142} km/h')
print(f'Uuden auton rekisteritunnus on {uusi_auto.rekisteritunnus}, huippunopeus {uusi_auto.huippunopeus},'
      f'tämän hetkinen nopeus {uusi_auto.nopeus_atm} km/h ja kuljettu matka on {uusi_auto.kuljettu_matka} km.')