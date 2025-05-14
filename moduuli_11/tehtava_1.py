class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f'Kirja: {self.nimi}')
        print(f'Kirjoittaja: {self.kirjoittaja}')
        print(f'Sivumäärä: {self.sivumaara}')

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f'Lehti: {self.nimi}')
        print(f'Päätoimittaja: {self.paatoimittaja}')

if __name__ == '__main__':
    lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
    kirja = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

    print('Julkaisun tiedot: \n')
    lehti.tulosta_tiedot()
    print()
    kirja.tulosta_tiedot()